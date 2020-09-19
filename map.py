from datawrapper import Datawrapper
import pandas as pd
import requests

DW_TOKEN = "lHl9w5VaMTL7dkSwCX3IYlUX4weMkOcLBSlzhnChgjnventUlRdOv2sATiHDxTsK"
dw = Datawrapper(access_token = DW_TOKEN)
DATA_PATH = "twitter_parsed.csv"

def update_properties(ID):
    dw.update_description(
        chart_id = ID,
        source_name = 'Crowdbreaks',
        source_url = 'https://www.crowdbreaks.org/',
        byline = '',
    )

    properties = {
      "axes": {
          "keys": "Alpha-3",
          "values": "Normalized Count"
      },
      "visualize": {
          "basemap": "world-2019",
          "map-key-attr": "DW_STATE_CODE",
          "tooltip": { 
                "body": "scare level: {{ Normalized_Count }}", 
                  "title": "{{ Country }}", 
                  "fields": { 
                        "ISO Code": "Alpha-3", 
                        "Country": "Country", 
                        "Normalized_Count": "Normalized Count" 
                    } 
            },
        "gradient": {
        "stops": [
          {"p": 0, "v": 0},
          {"p": 0.25,"v": 0.21175258672962177},
          {"p": 0.5,"v": 1.0358334534177065},
          {"p": 0.75,"v": 4.514756946019832},
          {"p": 1,"v": 100}
          ],
        "colors": [
          {"c": "#feebe2","p": 0},
          {"c": "#fcc5c0","p": 0.2},
          {"c": "#fa9fb5","p": 0.4},
          {"c": "#f768a1","p": 0.6},
          {"c": "#c51b8a","p": 0.8},
          {"c": "#7a0177","p": 1}
        ],
        "domain": [0,0.2,0.4,0.6,0.8,1]
      },
      "zoomable": True
      }
    }
    dw.update_metadata(ID, properties)



def create_new_map():
    df = pd.read_csv(DATA_PATH, sep=',')
    new_chart_info = dw.create_chart(title = '', chart_type = 'd3-maps-choropleth', data = df)
    print(new_chart_info)

    dw.update_description(
        chart_id = new_chart_info['id'],
        source_name = 'Crowdbreaks',
        source_url = 'https://www.crowdbreaks.org/',
        byline = '',
    )

    update_properties(new_chart_info["id"])
    dw.publish_chart(chart_id = new_chart_info['id'])


def update_map(ID, csv_file = "twitter_parsed.csv"):
    df = pd.read_csv(csv_file, sep=',')
    dw.add_data(ID, df)
    update_properties(ID)
    dw.publish_chart(ID)


#dw.update_metadata(ID, properties)
#dw.publish_chart(ID)