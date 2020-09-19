from datawrapper import Datawrapper
import pandas as pd

dw = Datawrapper(access_token = "lHl9w5VaMTL7dkSwCX3IYlUX4weMkOcLBSlzhnChgjnventUlRdOv2sATiHDxTsK")

df = pd.read_csv("test2.csv", sep=',')
new_chart_info = dw.create_chart(title = 'New world chart 3!', chart_type = 'd3-maps-choropleth', data = df)
print(new_chart_info)

dw.update_description(
    chart_id = new_chart_info['id'],
    source_name = 'UN Population Division',
    source_url = 'https://population.un.org/wup/',
    byline = 'Your name here!',
)

properties = {
      "axes": {
          "keys": "code",
          "values": "value"
      },
      "visualize": {
          "basemap": "world-2019",
          "map-key-attr": "DW_STATE_CODE"
      }
    }
dw.update_metadata(new_chart_info['id'], properties)

dw.publish_chart(chart_id = new_chart_info['id'])
