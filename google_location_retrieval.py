"""Google_Location_Retrieval

Author: Kathleen Brown
Prepared For: BuzzFeed Recruiting Team
Date: 03/30/2018

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
    status = private ( please reach out to me to access this, I just didn't
                want to have my code accessable by other possible
                participants )

Comments:
    * Using Python for the dynamic libraries for handling JSON objects
    * Hooking project to source control for my own benefit as well as
        offering recruiters the chance to see how my code develops
    * Since only 'Green Bay' was given as a search filter, I'm going with
        Green Bay, Wisconsin. Normally would ask for clarification for
        built in searches
    * Played around a bit with the URL, will be a good reference for
        knowing how the JSON object is built later
    * Using the urllib2 for opening the url link

Resources:
    * https://developers.google.com/maps/documentation/geocoding/start?hl=en_US
    * https://docs.python.org/2/library/urllib2.html
    
Todos:
    * DONE: Sign-in to Google Console and retrieve API key
    * Connect to the API using the given link to retrieve JSON object
    * Parse returned JSON object to give desired output
    
"""

#!/usr/bin/env python

from urllib.request import urlopen

api_key = 'AIzaSyDNTiZF0xoVU2eVAfQNdGPdmsv7Wa0pgqg'
address = 'address=Green+Bay'
start_point = 'http://maps.googleapis.com/maps/api/geocode/json'

# create the full search url to pass to urlopen
url = start_point + "?" + address + "&key=" + api_key

read_obj = urlopen(url)



