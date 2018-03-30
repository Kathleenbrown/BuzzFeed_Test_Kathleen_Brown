"""Google_Location_Retrieval

Author: Kathleen Brown
Prepared For: BuzzFeed Recruiting Team
Date: 03/30/2018
Python Distro: 3.5.4
Compiling & Running Instructions:
    Compiling and execution handled through built-in Python Interpretor (Shell)

Problem:
    Using the Google Maps API, retrieve the JSON response after
    applying a query parameter filter to the geocode endpoint. Then take
    the reponse and transform it to produce the expected output:

         Green Bay
         ID: <insert place_id here>
         Latitude: <insert latitude here>
         Longitude: <insert longitude here>

    Starting Endpoint = http://maps.googleapis.com/maps/api/geocode/json


Google Maps Geocoding API: 
    API key = AIzaSyDNTiZF0xoVU2eVAfQNdGPdmsv7Wa0pgqg
    Example Given:
        https://maps.googleapis.com/maps/api/geocode/json
        ?address=1600+Amphitheatre+Parkway,+Mountain+View,+CA&key=YOUR_API_KEY
    Green Bay URL:
        https://maps.googleapis.com/maps/api/geocode/json?address=Green+Bay
        &key=AIzaSyDNTiZF0xoVU2eVAfQNdGPdmsv7Wa0pgqg

Source Control:
    url = https://github.com/Kathleenbrown/BuzzFeed_Test_Kathleen_Brown
    status = private ( please reach out to me to access this, didn't want
                       to leave public in case of other participants )

Comments:
    * Using Python for the dynamic libraries for handling JSON objects
    * Hooking project to source control for my own benefit as well as
        offering recruiters the chance to see how my code develops
    * Since only 'Green Bay' was given as a search filter, I'm going with
        Green Bay, Wisconsin. Normally would ask for clarification for
        built in searches
    * Played around a bit with the URL, will be a good reference for
        knowing how the JSON object is built later
    * Using the urllib2 for opening the url link and storing html
    * Importing the json library for easy access to the data type
    * In order to print the JSON object, need to encode with utf-8
    * Encountered Error: "Requests to this API must be over SSL", after
        googling this error, found out that the entry point was http://
        instead of https://
    * While the location (Green Bay) you are searching for is hardcoded
        currently, since I have the URL split the way it is, this allows
        for easy modifications if later you wanted to prompt the user for
        a city/address and have it run that location instead.

Resources:
    * https://developers.google.com/maps/documentation/geocoding/start?hl=en_US
    * https://docs.python.org/2/library/urllib2.html
    * https://docs.python.org/2/library/json.html
    
Todos:
    * DONE: Sign-in to Google Console and retrieve API key
    * DONE: Connect to the API using the given link to retrieve JSON object
    * DONE: Parse returned JSON object to give desired output
    
"""

#!/usr/bin/env python

# included libraries
from urllib.request import urlopen
import json
import codecs

# name of city to search for
address = 'Green Bay'

api_key = 'AIzaSyDNTiZF0xoVU2eVAfQNdGPdmsv7Wa0pgqg'
start_point = 'https://maps.googleapis.com/maps/api/geocode/json'

# create the full search url to pass to urlopen
url = start_point + "?address=" + address.replace(" ", "+") + "&key=" + api_key

# the html is then stored in read_obj
read_obj = urlopen(url)

# adding read to endcode the JSON object to utf-8
reader = codecs.getreader("utf-8")

# load in the JSON object for output
json_data = json.load(reader(read_obj))

# prints out all expected output
print(address, end='\n\n')
print("ID: ", end='')
print(json_data['results'][0]['place_id'], end='\n\n')
print("Latitude: ", end='')
print(json_data['results'][0]['geometry']['location']['lat'], end='\n\n')
print("Longitude: ", end='')
print(json_data['results'][0]['geometry']['location']['lng'])



