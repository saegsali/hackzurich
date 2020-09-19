import pandas as pd
import numpy as np
import json
import os

with open('keywords.json') as json_file:
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
    row["Total"] += df[row.name].sum()
    row["Corona Related"] += (df[row.name] & df["Corona"]).sum()
    return row



# Initialize necessary dataframes
ch_data = pd.read_csv("switzerland_data.csv")
codes = ch_data["Postal"].values

news_data = pd.DataFrame(index=codes)
news_data["Corona Related"] = 0
news_data["Total"] = 0

# Loop through files in SMD folder
directory = "/Users/joelasper/Documents/data_hackzurich/hackzurich/SMD/data_export"
for filename in os.listdir(directory):
    print(filename)
    if filename.endswith(".csv"): 
        path = os.path.join(directory, filename)

        # Read news data and process
        df = pd.read_csv(path)
        df["fulltext"] = df["ht"].astype("str") + " " + df["sm"].astype("str") + " " + df["tx"].astype("str")
        
        # Reset columns to 0
        for col in codes:
            df[f"{col}"] = 0
        df["Corona"] = 0
        
        # Apply keywords
        df = df.apply(find_keywords, axis=1)

        # Count total mentions of canton and news related to Corona
        news_data = news_data.apply(count, axis=1)

news_data["Ratio"] = news_data["Corona Related"] / news_data["Total"] * 100
print(news_data)
news_data.to_csv("smd_data.csv", index=True)









