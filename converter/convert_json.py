import json
from pprint import pprint

import sqlite3 as lite
import sys

con = lite.connect('../output/routeprice.db')

# with con:
# 	cur = con.cursor()
# 	cur.execute('SELECT SQLITE_VERSION()')
# 	data = cur.fetchone()
# 	print ("SQLite version: %s" % data)

with open('../output/SYD-DPS-2016-11-10-2016-11-24.json') as data_file:
    data = json.load(data_file)


agent_dictionary= {}
for each_agent in data['Agents']:
	agent_dictionary.update({each_agent['Id'] : each_agent['Name']})

# print (agent_dictionary)

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


# def flight_details():
# 	flight_itinerary_dictionary = {}
# 	for all_flight_legs in data['Legs']:
# 		for all_flights in all_flight_legs['FlightNumbers']:
# 			flight_itinerary_dictionary.update ({all_flight_legs['Id'] : 
# 				   [all_flight_legs['Directionality'],
# 				   all_flight_legs['Departure'],
# 				   all_flight_legs['Arrival'],
# 				   all_flight_legs['Duration']]
# 				   })
# 	return flight_itinerary_dictionary

def flight_details():
	with con:
		cur = con.cursor()
		cur.execute("DROP TABLE IF EXISTS itinerary")
		cur.execute("CREATE TABLE IF NOT EXISTS itinerary(id_db INTEGER PRIMARY KEY AUTOINCREMENT, id TEXT, Directionality TEXT, Departure TEXT, Arrival TEXT, Duration int);")
		for all_flight_legs in data['Legs']:
			for all_flights in all_flight_legs['FlightNumbers']: 
				cur.execute("INSERT INTO itinerary (id, Directionality, Departure, Arrival, Duration) VALUES (?, ?, ?, ?, ?);", (all_flight_legs['Id'], 
					all_flight_legs['Directionality'], all_flight_legs['Departure'], all_flight_legs['Arrival'], all_flight_legs['Duration']
					)
				)	

		con.commit()

# price_finder()

flight_details()
