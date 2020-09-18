import pandas as pd
import numpy as np
import json
import geopy
import reverse_geocode as rg

filenames = ["/Users/Nico/Desktop/hackzurich_data/Twitter/crowdbreaks_tweets_jan_jun_2020_has_geo_coordinates.csv",
"/Users/Nico/Desktop/hackzurich_data/Twitter/crowdbreaks_tweets_jan_jun_2020_has_place.csv"]


def parse_countries():
    country_names =  []
    alpha2_codes = []
    alpha3_codes = []
    with open('countries.json') as json_file:
        data = json.load(json_file)
        for c in data:
            country_names.append(c["name"])
            alpha2_codes.append(c["alpha-2"])
            alpha3_codes.append(c["alpha-3"])
    
    return (country_names, alpha2_codes, alpha3_codes)


def reverse_geocode(df, geolocator, lat_field, lon_field):
    location = geolocator.reverse((df[lat_field], df[lon_field]))
    return location.raw['address']['country']

def process_chunk(df, chunk):
    # Analyze chunk and count country occurences 
    # geolocator = geopy.Nominatim(user_agent='hackzurich')
    # codes = chunk.apply(reverse_geocode, axis=1, geolocator=geolocator, lat_field='latitude', lon_field='longitude')
    # chunk["country_code"] = codes
    # Convert lat and long columns to a tuple of tuples
    coords = tuple(zip(chunk['latitude'], chunk['longitude']))

    results_rg = rg.search(coords)
    codes = [x.get('country_code') for x in results_rg]

    # Insert codes new chunk column
    chunk['codes'] = codes

    # Count number of occurences
    counts = chunk.codes.value_counts()
    for (code, count) in counts.iteritems():
        df.loc[df['Alpha-2'] == code, "Count"] += int(count)



if __name__ == "__main__":
    country_names, alpha2, alpha3 = parse_countries()
    
    # Create DataFrame that counts number of tweets per country
    df = pd.DataFrame({"Country": country_names, "Alpha-2": alpha2, "Alpha-3": alpha3, "Count": 0})
    df['Country'] = df['Country'].astype('category')
    df['Alpha-2'] = df['Alpha-2'].astype('category')
    df['Alpha-3'] = df['Alpha-3'].astype('category')

    chunksize = 10 ** 6
    for filename in filenames:
        for chunk in pd.read_csv(filename, chunksize=chunksize):
            process_chunk(df, chunk)

    # Save dataframe to csv file
    df.to_csv("twitter_parsed.csv")