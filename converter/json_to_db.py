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


def agent_details():

	with con:
		cur = con.cursor()
		cur.execute("CREATE TABLE IF NOT EXISTS Agents(id_db INTEGER PRIMARY KEY AUTOINCREMENT, Id TEXT, Name TEXT);")
		for each_agent in data['Agents']:
			cur.execute("INSERT INTO Agents (Id, Name) VALUES (?, ?);", (each_agent['Id'], each_agent['Name']))	
		
		con.commit()

	# agent_dictionary= {}
	# for each_agent in data['Agents']:
	# 	agent_dictionary.update({each_agent['Id'] : each_agent['Name']})

# print (agent_dictionary)

def place_details():
	with con:
		cur = con.cursor()
		cur.execute("CREATE TABLE IF NOT EXISTS Place (id_db INTEGER PRIMARY KEY AUTOINCREMENT, Id TEXT, Code TEXT, Name TEXT, Type Text);")
		for each_place in data['Places']:
			cur.execute("INSERT INTO Place (Id, Code, Name, Type) VALUES (?, ?, ?, ?);", (each_place['Id'], each_place['Code'], each_place['Name'], each_place['Type']))
		
		con.commit()

	# for each_place in data['Places']:
	# 	print (each_place['Id'], each_place['Code'], each_place['Name'], each_place['Type'])

# def agent_finder(agent_id):
# 	agent_name = None
# 	if agent_id in agent_dictionary:
# 		agent_name = agent_dictionary.get(agent_id)
# 	return agent_name

# def price_data():
# 	with con:
# 		cur = con.cursor()
# 		cur.execute("CREATE TABLE IF NOT EXISTS Price (id_db INTEGER PRIMARY KEY AUTOINCREMENT, Agent_Id TEXT, Price TEXT);")
# 		for each_itineraries in data['Itineraries']:
# 			for each_pricing_options in each_itineraries['PricingOptions']:
# 				cur.execute("INSERT INTO Price (Agent_Id, Price) VALUES (?, ?);", (each_pricing_options['Agents'][0], each_pricing_options['Price']))
		
# 		con.commit()

def itineraries_data():
	with con:
		cur = con.cursor()
		cur.execute("CREATE TABLE IF NOT EXISTS Itineraries (id_db INTEGER PRIMARY KEY AUTOINCREMENT, Agent_Id TEXT, Price TEXT, InboundLegId TEXT, OutboundLegId TEXT);")
		for each_itineraries in data['Itineraries']:
			for each_pricing_options in each_itineraries['PricingOptions']:
				cur.execute("INSERT INTO Itineraries (Agent_Id, Price, InboundLegId, OutboundLegId) VALUES (?, ?, ?, ?);", (each_pricing_options['Agents'][0], each_pricing_options['Price'], 
					each_itineraries['InboundLegId'], each_itineraries['OutboundLegId'],))
		
		con.commit()


	# for each_itineraries in data['Itineraries']:
	# 	for each_pricing_options in each_itineraries['PricingOptions']:
	# 		print (each_pricing_options['Agents'][0], agent_finder(each_pricing_options['Agents'][0]), each_pricing_options['Price'])


# def price_finder():
# 	for each_itineraries in data['Itineraries']:
# 			# pprint (each_itineraries['PricingOptions'])
# 		for each_pricing_options in each_itineraries['PricingOptions']:
# 			print (each_pricing_options['Agents'][0], agent_finder(each_pricing_options['Agents'][0]), each_pricing_options['Price'])

def carriers_data():
	with con:
		cur = con.cursor()
		cur.execute("CREATE TABLE IF NOT EXISTS Carriers (id_db INTEGER PRIMARY KEY AUTOINCREMENT, Id TEXT, Name TEXT, Code TEXT);")
		for each_carrier in data['Carriers']:
			cur.execute("INSERT INTO Carriers (Id, Name, Code) VALUES (?, ?, ?);", (each_carrier['Id'], each_carrier['Name'], each_carrier['Code']))
		
		con.commit()

	# for each_carrier in data['Carriers']:
	# 	print (each_carrier['Code'], each_carrier['Id'], each_carrier['Name'])

def flight_details():
	flight_itinerary_dictionary = {}
	for all_flight_legs in data['Legs']:
		for all_flights in all_flight_legs['FlightNumbers']:
			print (all_flights['FlightNumber'], all_flights['CarrierId'], 
				all_flight_legs['Id'], 
				all_flight_legs['Directionality'], 
				all_flight_legs['Departure'], 
				all_flight_legs['Arrival'], 
				all_flight_legs['Duration'], 
				all_flight_legs['DestinationStation']
				)

	# 		flight_itinerary_dictionary.update ({all_flight_legs['Id'] : 
	# 			   [
	# 			   all_flights['FlightNumber'],
	# 			   all_flights['CarrierId'],

	# 			   all_flight_legs['Directionality'],
	# 			   all_flight_legs['Departure'],
	# 			   all_flight_legs['Arrival'],
	# 			   all_flight_legs['Duration'],
	# 			   all_flight_legs['DestinationStation']
	# 			   ]
	# 			   })
	# return flight_itinerary_dictionary

def leg_details():
	with con:
		cur = con.cursor()
		cur.execute("CREATE TABLE IF NOT EXISTS Legs(id_db INTEGER PRIMARY KEY AUTOINCREMENT, id TEXT, Directionality TEXT, Departure TEXT, Arrival TEXT, Duration int, DestinationStation TEXT, OriginStation TEXT, FlightNumber TEXT, CarrierId TEXT);")
		for all_flight_legs in data['Legs']:
			for all_flights in all_flight_legs['FlightNumbers']: 
				cur.execute("INSERT INTO Legs (id, Directionality, Departure, Arrival, Duration, DestinationStation, OriginStation, FlightNumber, CarrierId) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);", (all_flight_legs['Id'], 
					all_flight_legs['Directionality'], all_flight_legs['Departure'], all_flight_legs['Arrival'], all_flight_legs['Duration'], 
					all_flight_legs['DestinationStation'], all_flight_legs['OriginStation'], all_flights['FlightNumber'], all_flights['CarrierId']
					)
				)	

		con.commit()

# price_finder()

# leg_details()
# print (flight_details())

# agent_details()
# price_data()
# carriers_data()

# itineraries_data()
place_details()