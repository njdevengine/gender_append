#pip install gender-guesser
#enrich a dataset with guessed genders


import pandas as pd
path = "/Users/input/filepath//"
df = pd.read_csv(path+"facebook_audience.csv",encoding = "latin1")

import gender_guesser.detector as gender
d = gender.Detector()
print(d.get_gender(u"Bob"))

genders = []
for i in list(df.fn):
    gen = d.get_gender(i)
    genders.append(gen)
    
#{'andy', 'female', 'male', 'mostly_female', 'mostly_male', 'unknown'}

cleaned = []
for i in genders:
    if i == "andy":
        cleaned.append("")
    elif i == "mostly-female":
        cleaned.append("F")
    elif i == "mostly-male":
        cleaned.append("M")
    elif i == "female":
        cleaned.append("F")
    elif i == "male":
        cleaned.append("M")
    else:
        cleaned.append("")
