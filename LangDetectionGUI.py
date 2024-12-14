from idlelib.pyparse import trans

import joblib
import pandas
import numpy
from tkinter import *
import sklearn
from LanguagePredictionModel import LanguageModel

root = Tk()

model = LanguageModel()

def detectClick():
    text = inputText.get()
    if text.strip() == "":
        print()
    else:
        detection = model.predict(text)
        translation.config(text="The language is: "+ detection)


root.geometry("505x300")
myLabel = Label(root, text="Insert text", font=("Helvetica", 15),  justify="center")
myLabel.grid(row= 1, column= 1, padx=5, pady=5)
inputText = Entry(root, width = 70, justify="center", font=("Helvetica", 10))
inputText.grid(row =2, column= 1, padx=5, pady=5)
myButton = Button(root, text = "detect", padx=20, pady=20, command=detectClick)
myButton.grid(row=3, column= 1, padx=5, pady=5)
translation = Label(root, text ="The language is: ", font=("Helvetica", 10), justify="center")
translation.grid(row = 4, column = 1, padx=5, pady=5)


blank_space =  Label(root, text = "        ")
blank_space.grid(row = 0, column = 1, padx=5, pady=5)

root.mainloop()











