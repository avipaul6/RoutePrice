import json
from pprint import pprint

with open('../output/SYD_LHR.json') as data_file:    
    data = json.load(data_file)

for each_itineraries in data['Itineraries']:
		# pprint (each_itineraries['PricingOptions'])
	for each_pricing_options in each_itineraries['PricingOptions']:
		print (each_pricing_options['Agents'], each_pricing_options['Price'])


# for each_agent in data['Agents']:
# 	print (each_agent['Id'], each_agent['Name'])
