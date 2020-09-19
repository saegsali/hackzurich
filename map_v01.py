from datawrapper import Datawrapper
import pandas as pd

dw = Datawrapper(access_token = "lHl9w5VaMTL7dkSwCX3IYlUX4weMkOcLBSlzhnChgjnventUlRdOv2sATiHDxTsK")

df = pd.read_csv("test.csv", sep=',')
new_chart_info = dw.create_chart(title = 'New chart 2!', chart_type = 'd3-maps-choropleth', data = df)
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
          "values": "literacy-rate"
      },
      "visualize": {
          "basemap": "africa",
          "map-key-attr": "ADM0_A3"
      }
    }
dw.update_metadata(new_chart_info['id'], properties)

dw.publish_chart(chart_id = new_chart_info['id'])
