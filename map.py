from datawrapper import Datawrapper
import pandas as pd
ID = '7nMGn'
dw = Datawrapper(access_token = "lHl9w5VaMTL7dkSwCX3IYlUX4weMkOcLBSlzhnChgjnventUlRdOv2sATiHDxTsK")

df = pd.read_csv("twitter_parsed.csv", sep=',')
new_chart_info = dw.create_chart(title = 'Corona Scare Map', chart_type = 'd3-maps-choropleth', data = df)
#new_chart_info = {'publicId': '2q8Wx', 'language': 'en-US', 'theme': 'default', 'title': 'New world chart 4!', 'type': 'd3-maps-choropleth', 'metadata': {'data': {}}, 'authorId': 252156, 'id': '2q8Wx', 'lastModifiedAt': '2020-09-19T08:09:06.658Z', 'createdAt': '2020-09-19T08:09:06.658Z', 'url': '/v3/charts/2q8Wx'}
print(new_chart_info)

dw.update_description(
    #chart_id = new_chart_info['id'],
    chart_id = ID,
    source_name = 'Crowdbreaks',
    source_url = 'https://www.crowdbreaks.org/',
    byline = '',
)

properties = {
      "axes": {
          "keys": "code",
          "values": "value"
      },
      "visualize": {
          "basemap": "world-2019",
          "map-key-attr": "DW_STATE_CODE",
          "tooltip": { 
                "body": "scare level: {{ value }}", 
                  "title": "{{ Country }}", 
                  "fields": { 
                        "code": "code", 
                        "Country": "Country", 
                        "value": "value" 
                    } 
            },
        "gradient": {
        "stops": [
          {
            "p": 0,
            "v": 0
          },
          {
            "p": 0.25,
            "v": 0.21175258672962177
          },
          {
            "p": 0.5,
            "v": 1.0358334534177065
          },
          {
            "p": 0.75,
            "v": 4.514756946019832
          },
          {
            "p": 1,
            "v": 100
          }
        ],
        "colors": [
          {
            "c": "#feebe2",
            "p": 0
          },
          {
            "c": "#fcc5c0",
            "p": 0.2
          },
          {
            "c": "#fa9fb5",
            "p": 0.4
          },
          {
            "c": "#f768a1",
            "p": 0.6
          },
          {
            "c": "#c51b8a",
            "p": 0.8
          },
          {
            "c": "#7a0177",
            "p": 1
          }
        ],
        "domain": [
          0,
          0.2,
          0.4,
          0.6,
          0.8,
          1
        ]
      },
      "zoomable": True

      }
}

#dw.update_metadata(new_chart_info['id'], properties)
#dw.publish_chart(chart_id = new_chart_info['id'])

dw.update_metadata(ID, properties)
dw.publish_chart(ID)