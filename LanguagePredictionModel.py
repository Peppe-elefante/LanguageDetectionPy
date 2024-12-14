import joblib

from features import features

class LanguageModel:
    def __init__(self):
        self.ensemble = joblib.load('C:/Users/ACER/Desktop/ML/MLprogetto/language_detection_model.pkl')

    def _transformation(self, sentences, special_chars):
        res = []
        sentences = list(map(str.lower, sentences))
        for sentence in sentences:
            sent_vector = [0 for _ in range(len(special_chars))]
            for index, char in enumerate(special_chars):
                if char in sentence:
                    sent_vector[index] = 1
                else:
                    sent_vector[index] = 0
            res.append(sent_vector)
        return res

    def _top_three(self, X):
        res = ""
        probabilities = self.ensemble.predict_proba(X)
        labels = self.ensemble.classes_
        dic_languages = [dict(zip(labels, prob)) for prob in probabilities]
        for pred in dic_languages:
            sorted_pred = dict(sorted(pred.items(), key=lambda item: item[1], reverse=True)[:3])
            other = 100
            for key, value in sorted_pred.items():
                sorted_pred[key] = round(value * 100, 2)
                other -= sorted_pred[key]
                res += key + " = " + str(sorted_pred[key]) + '%\n'
            res += "Other = " + str(round(other, 2)) + "%\n"

        return res

    def predict(self, sentence):
        if isinstance(sentence, list):
            for phrase in sentence:
                phrase += " "
            sentence = self._transformation(sentence, features)
        else:
            sentence += " "
            sentence = self._transformation([sentence], features)

        for prediction in self.ensemble.predict(sentence):
            print("the prediction is: " + prediction)

        return self._top_three(sentence)