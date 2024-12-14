
caratteri_speciali = ['ã', 'â', 'æ', 'è', 'ë', 'î', 'ï', 'œ', 'ù', 'û', 'ÿ',
                     'ñ', 'ă', 'ș', 'ț', 'ö', 'õ', 'å', 'ì', 'ò', 'ß', 'ä',
                      'ã', 'ã', '¿','¡']

articoli = [
    " a ", " an ", " the ", "s ", "i ",
    " um ", " uma ", " o ", "a ", " os ", " as ",
    " un ", " une ", " le ", " la ", " les ", " l'", " des ",
     "una", " el ", " los ", " las ", " unos ", " unas ",
    "o ", " unii ", " unele ", " cel ", " cea ", " cei ", " cele ",
    " een ", " de ", " het ", " deze ", " die ",
    " üks ", " teine ", " see ", " need ", " see ",
    " il ", " lo ", " i ", " gli ", " un' ", " uno ",
    " ein ", " eine ", " der ", " die ", " das ", " einige "
]

ngrams = [
    "th", "he", "in", "er", "an", "re", "nd", "at", "on", "not", "op", "ou", "es",
        "ti", "to", "it", "is", "of", "le", "de", "la", "bij", "et", "se", "un", "or",
        "te", "nt", "ce", "el", "ech", "em", "na", "di", "so", "ei", "ue", "een", "io",
        "que", "ra", "me", "su", "va", "ni", "po", "ea", "nh", "ij", "ing", "ar", "sh",
        "ng", "je", "for", "n't", "ent", "boa ", "bem ", " bem", "are", "how", "how ", "wie"
        "hoe", "j'", "t'", "l'" , "ing" , "ng", "'s", "Não", "ão" , "ça ", "ai", "ch", "gn", "ui"
        "gh", "șa", "ța", "c'", "m'"
]

saluti = [
    "Hello", "Hi", "Good morning", "Good afternoon", "Good evening", "how are", # English
    "Olá", "Oi", "Bom dia", "Boa tarde", "Boa noite","tudo bem", "como",  # Portuguese
    "Bonjour", "Salut", "Bonsoir", "Coucou", "Allô", "ça va",  # French
    "Hola", "Buenos días", "Buenas tardes", "Buenas noches", "Qué tal", "cómo", "está", # Spanish
    "Bună", "Salut", "Bună dimineața", "Bună ziua", "Bună seara",  # Romanian
    "Hallo", "Hoi", "Goedemorgen", "Goedemiddag", "Goedenavond", "hoe gaat",  # Dutch
    "Ciao", "Buongiorno", "Salve", "Buonasera", "Buonanotte", "come stai",  # Italian
    "Hallo", "Guten Morgen", "Guten Tag", "Guten Abend", "Servus"  # German
]
saluti = list(map(str.lower, saluti))

pronomi_soggetivi = [
    "i ", "you ", "he ", "she ", "it ", "we ", "they ",
    "eu ", "tu ", "ele ", "ela ", "você ", "nós ", "eles ", "elas ",
    "je ", "tu ", "elle ", "on ", "nous ", "vous ", "ils ", "elles ",
    "yo ", "tú ", "él ", "ella ", "usted", "nosotros", "nosotras", "vosotros", "vosotras", "ellos ", "ellas ", "ustedes ",
    "eu ", "tu ", "el ", "ea ", "noi ", "voi ", "ei ", "ele ",
    "ik ", "jij ", "u ", "hij ", "zij ", "het ", "wij ", "jullie ", "zij ",
    "mina ", "sina ", "tema ", "meie ", "teie ", "nemad ",
    "io ", "tu ", "lui ", "lei ", "esso ", "noi ", "voi ", "loro ",
    "ich ", "du ", "er ", "sie ", "es ", "wir ", "ihr ", "sie "
]

features = caratteri_speciali + ngrams + saluti + articoli + pronomi_soggetivi