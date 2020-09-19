import pandas as pd
from sklearn import preprocessing
import numpy as np
import json
import reverse_geocode as rg

dw_keys = ["AFG", "ALB", "DZA", "SDN", "AND", "AGO", "ATG", "ARG", "ARM", "AUS", "AUT", "AZE", "BHS", "BHR", "BGD", "BRB", "BLR", "BEL", "BLZ", "BEN", "BTN", "BOL", "BIH", "BWA", "BRA", "BRN", "BGR", "BFA", "BDI", "KHM", "CMR", "CAN", "CPV", "CAF", "TCD", "CHL", "COL", "COM", "COG", "CRI", "HRV", "CUB", "CYP", "CZE", "CIV", "PRK", "COD", "DNK", "DJI", "DMA", "DOM", "ECU", "SSD", "SLV", "GNQ", "ERI", "EST", "ETH", "FJI", "FIN", "FRA", "GAB", "GMB", "PSE", "GEO", "DEU", "GHA", "GRC", "GRL", "GRD", "GTM", "GNB", "GIN", "GUY", "HTI", "HND", "HUN", "ISL", "IND", "IDN", "IRN", "IRQ", "IRL", "ISR", "ITA", "JAM", "JPN", "JOR", "KAZ", "KEN", "KIR", "KWT", "KGZ", "LAO", "LVA", "LBN", "LSO", "LBR", "LBY", "LIE", "LTU", "LUX", "MAC", "MDG", "PRT", "MWI", "MYS", "MDV", "MLI", "MLT", "MHL", "MRT", "MUS", "MEX", "FSM", "MDA", "MCO", "MNG", "MAR", "MOZ", "MMR", "NAM", "NRU", "NPL", "NLD", "NZL", "NIC", "NER", "NGA", "NOR", "OMN", "PAK", "PLW", "PAN", "PNG", "PRY", "PER", "PHL", "POL", "USA", "QAT", "KOR", "ROU", "RUS", "RWA", "KNA", "LCA", "VCT", "WSM", "SMR", "STP", "SAU", "SEN", "SYC", "SLE", "SGP", "SVK", "SVN", "SLB", "SOM", "ZAF", "ESP", "LKA", "SUR", "SWZ", "SWE", "CHE", "SYR", "TJK", "THA", "MKD", "TLS", "TGO", "TON", "TTO", "TUN", "TUR", "TKM", "TUV", "UGA", "UKR", "ARE", "GBR", "TZA", "URY", "UZB", "VUT", "VEN", "VNM", "YEM", "ZMB", "ZWE", "MNE", "SRB", "HKG", "EGY", "KSV", "CHN", "TWN", "ESH" ]

filenames = ["/Users/Nico/Desktop/hackzurich_data/Twitter/crowdbreaks_tweets_jan_jun_2020_has_geo_coordinates.csv",
"/Users/Nico/Desktop/hackzurich_data/Twitter/crowdbreaks_tweets_jan_jun_2020_has_place.csv"]


def parse_countries():
    country_names =  []
    alpha2_codes = []
    alpha3_codes = []
    population = []
    with open('countries.json') as json_file:
        data = json.load(json_file)
        for c in data:
            country_names.append(c["name"])
            alpha2_codes.append(c["alpha-2"])
            alpha3_codes.append(c["alpha-3"])
            population.append(c["population"])
    
    return (country_names, alpha2_codes, alpha3_codes, population)


def reverse_geocode(df, geolocator, lat_field, lon_field):
    location = geolocator.reverse((df[lat_field], df[lon_field]))
    return location.raw['address']['country']

def process_chunk(df, chunk):
    # Analyze chunk and count country occurences 
    # geolocator = geopy.Nominatim(user_agent='hackzurich')
    # codes = chunk.apply(reverse_geocode, axis=1, geolocator=geolocator, lat_field='latitude', lon_field='longitude')
    # chunk["country_code"] = codes
    
    # Convert lat and long columns to a tuple of tuples
    try:
        coords = tuple(zip(chunk['latitude'], chunk['longitude']))
    except:
        coords = tuple(zip(chunk['estimated_latitude'], chunk['estimated_longitude']))


    results_rg = rg.search(coords)
    codes = [x.get('country_code') for x in results_rg]

    # Insert codes new chunk column
    chunk['codes'] = codes

    # Count number of occurences
    counts = chunk.codes.value_counts()
    for (code, count) in counts.iteritems():
        df.loc[df['Alpha-2'] == code, "Count"] += int(count)

def process_data(filenames):
    country_names, alpha2, alpha3, population = parse_countries()
    
    # Create DataFrame that counts number of tweets per country
    df = pd.DataFrame({"Country": country_names, "Alpha-2": alpha2, "Alpha-3": alpha3, "Population": population, "Count": 0})
    df['Country'] = df['Country'].astype('category')
    df['Alpha-2'] = df['Alpha-2'].astype('category')
    df['Alpha-3'] = df['Alpha-3'].astype('category')

    chunksize = 10 ** 6
    for filename in filenames:
        for chunk in pd.read_csv(filename, chunksize=chunksize):
            process_chunk(df, chunk)


    # Process data
    # Divide number of tweets by country population to "normalize data"
    df["Count per Capita"] = df["Count"] / df["Population"]

    
    # Filter dataframe to contain only countries known by datawrapper
    df = df[df['Alpha-3'].isin(dw_keys)]
    df.reset_index(drop=True, inplace=True)


    # Normalize Data und multiply with 100 to get appropriate range
    column_names_to_normalize = ['Count per Capita']
    x = df[column_names_to_normalize].values
    min_max_scaler = preprocessing.MinMaxScaler()
    x_scaled = min_max_scaler.fit_transform(x)
    df_temp = pd.DataFrame(x_scaled, columns=column_names_to_normalize, index = df.index)
    df["Normalized Count"] = df_temp
    df["Normalized Count"] = df["Normalized Count"] * 100

    # Round numbers to one decimal
    df = df.round(1)

    # Save dataframe to csv file for datawrapper
    header = ["Country", "Alpha-3", "Count", "Count per Capita", "Normalized Count"]
    df.to_csv("twitter_parsed.csv", columns=header, index=False)