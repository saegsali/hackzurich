from datawrapper import Datawrapper
#import datawrapper as Datawrapper
import pandas as pd

dw = Datawrapper(access_token = "lHl9w5VaMTL7dkSwCX3IYlUX4weMkOcLBSlzhnChgjnventUlRdOv2sATiHDxTsK")

df = pd.read_csv("https://raw.githubusercontent.com/chekos/datasets/master/data/datawrapper_example.csv", sep=';')
new_chart_info = dw.create_chart(title = 'New chart 2!', chart_type = 'd3-bars-stacked', data  = df)
new_chart_info

dw.update_description(
    chart_id = new_chart_info['hERfG'],
    source_name = 'UN Population Division',
    source_url = 'https://population.un.org/wup/',
    byline = 'Your name here!',
)

dw.publish_chart(chart_id = new_chart_info['hERfG'])