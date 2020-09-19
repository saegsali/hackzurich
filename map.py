from datawrapper import Datawrapper
import pandas as pd
ID = '2q8Wx'
dw = Datawrapper(access_token = "lHl9w5VaMTL7dkSwCX3IYlUX4weMkOcLBSlzhnChgjnventUlRdOv2sATiHDxTsK")

df = pd.read_csv("twitter_parsed.csv", sep=',')
new_chart_info = dw.create_chart(title = 'Corona Scare Map', chart_type = 'd3-maps-choropleth', data = df)
#new_chart_info = {'publicId': '2q8Wx', 'language': 'en-US', 'theme': 'default', 'title': 'New world chart 4!', 'type': 'd3-maps-choropleth', 'metadata': {'data': {}}, 'authorId': 252156, 'id': '2q8Wx', 'lastModifiedAt': '2020-09-19T08:09:06.658Z', 'createdAt': '2020-09-19T08:09:06.658Z', 'url': '/v3/charts/2q8Wx'}
print(new_chart_info)

dw.update_description(
    chart_id = new_chart_info['id'],
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
                  "title": "{{ country }}", 
                  "fields": { 
                        "code": "code", 
                        "country": "country", 
                        "value": "value" 
                    } 
            } 

      }
}

dw.update_metadata(new_chart_info['id'], properties)

dw.publish_chart(chart_id = new_chart_info['id'])
