import csv, json
from skyscanner.skyscanner import Flights, FlightsCache

import os, sys
import os.path

flights_service = Flights('qu436735388915856462490856761763')
flights_cache_service = FlightsCache('qu436735388915856462490856761763')



def get_result_of_single_query (country, currency, locale, originplace, destinationplace, outbounddate, inbounddate, adults):
    result = flights_service.get_result(
        errors='graceful',
        country=country,
        currency=currency,
        locale=locale,
        originplace=originplace,
        destinationplace=destinationplace,
        outbounddate=outbounddate,
        inbounddate=inbounddate,
        adults=adults).parsed

    return result

def prepare_route_list_batch(list_of_routes):
    '''
    Get the list of routes and save each route value in json
    :return: json files with route price information
    '''
    country = 'AU',
    currency = 'AUD',
    locale = 'en-AU',
    adults = 1

    print (list_of_routes)
    # print (list_of_routes[0])

    result_from_route = get_result_of_single_query(country,
                                                   currency,
                                                   locale,
                                                   list_of_routes[0],
                                                   list_of_routes[1],
                                                   list_of_routes[2],
                                                   list_of_routes[3],
                                                   adults
                                                   )
    create_json_file(result_from_route, list_of_routes[0], list_of_routes[1], list_of_routes[2], list_of_routes[3])

def create_json_file(result, originplace, destinationplace, outbounddate, inbounddate):

        folder_location = '../output/'
        if not os.path.exists(folder_location):
            os.makedirs(folder_location)

        try:
            json_file_name = originplace[:3] + "-" + destinationplace[:3] + "-" + outbounddate + "-" + inbounddate + ".json"
            resultFile = open(os.path.join(folder_location, json_file_name).replace("\\", "/"), mode='w')
            json.dump(result, resultFile)
            print ("json created for %s to %s" % (originplace, destinationplace))
            resultFile.flush()
            resultFile.close()
        except Exception as e:
            print(e)
            pass

def get_route_result():

    with open('../input/route_list.csv', 'rt') as f:
        reader = csv.reader(f)
        for row in reader:
            # print (row)
            prepare_route_list_batch(row)



get_route_result()