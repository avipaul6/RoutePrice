# RoutePrice
To find out flight pricing for different routes

This tool uses skyscanner API to get flight price data

You will need skyscanner API key to use this. 

#How to run the code
For now to run this code, go to collector directory and run
`python collect_flight_status.py` 

#editing routes
to change the routes, change `route_list.csv` in input folder. Please note the date format for this

#date format
It is important to note that the date format for live pricing must be in `YYYY-MM-DD` format to work. Else you will get an error

#to do
1. Enable running code from start.py
2. Convert json to csv file for selected value
3. Run json - csv converter once json is created
4. Create test 

