import requests

headers = {
    'Authorization': 'Bearer lHl9w5VaMTL7dkSwCX3IYlUX4weMkOcLBSlzhnChgjnventUlRdOv2sATiHDxTsK',
    'content-type': 'application/json',
}

data = '{ "title": "Literacy rates in Africa", "type":"d3-maps-choropleth"}'

response = requests.post('https://api.datawrapper.de/v3/charts', headers=headers, data=data)

#response = requests.get('https://api.datawrapper.de/plugin/basemaps')
response = requests.get('https://api.datawrapper.de/plugin/basemaps/africa/ADM0_A3')


headers = {
    'Authorization': 'Bearer lHl9w5VaMTL7dkSwCX3IYlUX4weMkOcLBSlzhnChgjnventUlRdOv2sATiHDxTsK',
    'content-type': 'text/csv',
}

data = 'country,code,literacy-rate country,code,literacy-rate Angola,AGO,71.2 Burundi,BDI,85.5 Benin,BEN,38.4 Burkina Faso,BFA,37.7 Botswana,BWA,88.2 Central African Republic,CAF,36.8 Cote de Ivoire,CIV,43.3 Cameroon,CMR,75 Democratic Republic of Congo,COD,77.2 Congo,COG,79.3 Comoros,COM,78.1 Cape Verde,CPV,88.5 Algeria,DZA,79.6 Egypt,EGY,75.8 Eritrea,ERI,73.8 Ethiopia,ETH,49 Gabon,GAB,83.2 Ghana,GHA,76.6 Guinea,GIN,30.5 Gambia,GMB,55.6 Guinea-Bissau,GNB,59.8 Equatorial Guinea,GNQ,95.2 Kenya,KEN,78 Liberia,LBR,47.6 Libya,LBY,91.4 Lesotho,LSO,79.4 Morocco,MAR,71.7 Madagascar,MDG,64.7 Mali,MLI,33.1 Mozambique,MOZ,58.8 Mauritania,MRT,52.1 Malawi,MWI,66 Namibia,NAM,90.8 Niger,NER,19.1 Nigeria,NGA,59.6 Rwanda,RWA,71.2 Sudan,SDN,58.6 Senegal,SEN,55.6 Sierra Leone,SLE,48.4 Sao Tome and Principe,STP,91.7 Swaziland,SWZ,87.5 Chad,TCD,40 Togo,TGO,66.5 Tunisia,TUN,81.1 Tanzania,TZA,80.4 Uganda,UGA,73.8 South Africa,ZAF,94.6 Zambia,ZMB,85.1 Zimbabwe,ZWE,86.9'

response = requests.post('https://api.datawrapper.de/v3/charts/252156/data', headers=headers, data=data)


headers = {
    'Authorization': 'Bearer lHl9w5VaMTL7dkSwCX3IYlUX4weMkOcLBSlzhnChgjnventUlRdOv2sATiHDxTsK',
    'content-type': 'application/json',
}

data = '{ "metadata": { "axes": { "keys": "code", "values": "literacy-rate" }, "visualize": { "basemap": "africa", "map-key-attr": "ADM0_A3" } } }'

response = requests.post('https://api.datawrapper.de/v3/charts/252156', headers=headers, data=data)


headers = {
    'Authorization': 'Bearer lHl9w5VaMTL7dkSwCX3IYlUX4weMkOcLBSlzhnChgjnventUlRdOv2sATiHDxTsK',
}

response = requests.get('https://api.datawrapper.de/charts/252156/publish', headers=headers)