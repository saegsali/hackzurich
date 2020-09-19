import pandas as pd
import numpy as np
import json

with open('cantons.json') as json_file:
    CANTONS_DICT = json.load(json_file)
    WORD_LIST = CANTONS_DICT.keys()
    WORD_SET = set(WORD_LIST)

def words_in_string(a_string):
    return WORD_SET.intersection(a_string.split())


def find_keywords(row):
    matches = words_in_string(str(row["fulltext"]))
    for match in matches:
        postal = CANTONS_DICT[match]
        row[postal] = 1
    return row

def count(row):
    row["Total"] = df[row.name].sum()
    row["Corona Related"] = (df[row.name] & df["Corona"]).sum()
    return row

df = pd.read_csv("/Users/Nico/Desktop/hackzurich_data/SMD/zwao_output.csv")
df["fulltext"] = df["ht"].astype("str") + " " + df["sm"].astype("str") + " " + df["tx"].astype("str")
ch_data = pd.read_csv("switzerland_data.csv")
codes = ch_data["Postal"].values

# Add columns and initialize to 0
for col in codes:
    df[f"{col}"] = 0
df["Corona"] = 0

# Apply keywords
df = df.apply(find_keywords, axis=1)

# Count total mentions of canton and news related to Corona
news_data = pd.DataFrame(index=codes)
news_data["Corona Related"] = 0
news_data["Total"] = 0

news_data = news_data.apply(count, axis=1)
print(news_data)







