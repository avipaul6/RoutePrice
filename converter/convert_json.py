import json
from pprint import pprint

with open('../output/MEL-HKT-2016-11-10-2016-11-24.json') as data_file:    
    data = json.load(data_file)


agent_dictionary= {}
for each_agent in data['Agents']:
	agent_dictionary.update({each_agent['Id'] : each_agent['Name']})

print (agent_dictionary)

def agent_finder(agent_id):
	agent_name = None
	if agent_id in agent_dictionary:
		agent_name = agent_dictionary.get(agent_id)
	return agent_name



def price_finder():
	for each_itineraries in data['Itineraries']:
			# pprint (each_itineraries['PricingOptions'])
		for each_pricing_options in each_itineraries['PricingOptions']:
			print (each_pricing_options['Agents'][0], agent_finder(each_pricing_options['Agents'][0]), each_pricing_options['Price'])


price_finder()

