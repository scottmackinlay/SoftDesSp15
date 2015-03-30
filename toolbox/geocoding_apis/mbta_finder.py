"""
Geocoding and Web APIs Project Toolbox exercise

Find the MBTA stops closest to a given location.

Full instructions are at:
https://sites.google.com/site/sd15spring/home/project-toolbox/geocoding-and-web-apis
"""

import urllib   # urlencode function
import urllib2  # urlopen function (better than urllib version)
import json
from pprint import pprint

# Useful URLs (you need to add the appropriate parameters for your requests)
GMAPS_BASE_URL = "https://maps.googleapis.com/maps/api/geocode/json"
MBTA_BASE_URL = "http://realtime.mbta.com/developer/api/v2/stopsbylocation"
MBTA_DEMO_API_KEY = "wX9NwuHnZU2ToO7GmGR9uw"
data={u'stop': [{u'distance': u'0.0463778711855412',
            u'parent_station': u'place-bbsta',
            u'parent_station_name': u'Back Bay',
            u'stop_id': u'Back Bay',
            u'stop_lat': u'42.347158',
            u'stop_lon': u'-71.075769',
            u'stop_name': u'Back Bay'},
           {u'distance': u'0.0535630360245705',
            u'parent_station': u'place-bbsta',
            u'parent_station_name': u'Back Bay',
            u'stop_id': u'70014',
            u'stop_lat': u'42.34735',
            u'stop_lon': u'-71.075727',
            u'stop_name': u'Back Bay - Outbound'},
           {u'distance': u'0.0535630360245705',
            u'parent_station': u'place-bbsta',
            u'parent_station_name': u'Back Bay',
            u'stop_id': u'70015',
            u'stop_lat': u'42.34735',
            u'stop_lon': u'-71.075727',
            u'stop_name': u'Back Bay - Inbound'},
           {u'distance': u'0.0535630360245705',
            u'parent_station': u'',
            u'parent_station_name': u'',
            u'stop_id': u'place-bbsta',
            u'stop_lat': u'42.34735',
            u'stop_lon': u'-71.075727',
            u'stop_name': u'Back Bay'},
           {u'distance': u'0.0535630360245705',
            u'parent_station': u'place-bbsta',
            u'parent_station_name': u'Back Bay',
            u'stop_id': u'11384',
            u'stop_lat': u'42.34735',
            u'stop_lon': u'-71.075727',
            u'stop_name': u'Dartmouth St @ Back Bay Sta'},
           {u'distance': u'0.0535630360245705',
            u'parent_station': u'place-bbsta',
            u'parent_station_name': u'Back Bay',
            u'stop_id': u'23391',
            u'stop_lat': u'42.34735',
            u'stop_lon': u'-71.075727',
            u'stop_name': u'Back Bay Station'},
           {u'distance': u'0.0535630360245705',
            u'parent_station': u'place-bbsta',
            u'parent_station_name': u'Back Bay',
            u'stop_id': u'176',
            u'stop_lat': u'42.34735',
            u'stop_lon': u'-71.075727',
            u'stop_name': u'Dartmouth St opp Back Bay Sta'},
           {u'distance': u'0.0910642221570015',
            u'parent_station': u'',
            u'parent_station_name': u'',
            u'stop_id': u'71855',
            u'stop_lat': u'42.348245',
            u'stop_lon': u'-71.076218',
            u'stop_name': u'Stuart St @ Dartmouth St'},
           {u'distance': u'0.150986462831497',
            u'parent_station': u'',
            u'parent_station_name': u'',
            u'stop_id': u'1395',
            u'stop_lat': u'42.345156',
            u'stop_lon': u'-71.074969',
            u'stop_name': u'Dartmouth St @ Appleton St'},
           {u'distance': u'0.164772421121597',
            u'parent_station': u'',
            u'parent_station_name': u'',
            u'stop_id': u'1384',
            u'stop_lat': u'42.345018',
            u'stop_lon': u'-71.074771',
            u'stop_name': u'Dartmouth St @ Appleton St'},
           {u'distance': u'0.167072579264641',
            u'parent_station': u'',
            u'parent_station_name': u'',
            u'stop_id': u'178',
            u'stop_lat': u'42.349373',
            u'stop_lon': u'-71.076911',
            u'stop_name': u'Saint James Ave @ Dartmouth St'},
           {u'distance': u'0.176442056894302',
            u'parent_station': u'',
            u'parent_station_name': u'',
            u'stop_id': u'179',
            u'stop_lat': u'42.347595',
            u'stop_lon': u'-71.079984',
            u'stop_name': u'Ring Rd @ Huntington Ave'},
           {u'distance': u'0.212157785892487',
            u'parent_station': u'place-coecl',
            u'parent_station_name': u'Copley',
            u'stop_id': u'70154',
            u'stop_lat': u'42.349974',
            u'stop_lon': u'-71.077447',
            u'stop_name': u'Copley - Inbound'},
           {u'distance': u'0.212157785892487',
            u'parent_station': u'place-coecl',
            u'parent_station_name': u'Copley',
            u'stop_id': u'175',
            u'stop_lat': u'42.349974',
            u'stop_lon': u'-71.077447',
            u'stop_name': u'Boylston St @ Dartmouth St'},
           {u'distance': u'0.212157785892487',
            u'parent_station': u'',
            u'parent_station_name': u'',
            u'stop_id': u'place-coecl',
            u'stop_lat': u'42.349974',
            u'stop_lon': u'-71.077447',
            u'stop_name': u'Copley'}]}

# A little bit of scaffolding if you want to use it

def get_json(url):
    """
    Given a properly formatted URL for a JSON web API request, return
    a Python JSON object containing the response to that request.
    """
    f = urllib2.urlopen(url)
    response_text = f.read()
    response_data = json.loads(response_text)
    return response_data

def get_lat_long(place_name):
    """
    Given a place name or address, return a (latitude, longitude) tuple
    with the coordinates of the given place.

    See https://developers.google.com/maps/documentation/geocoding/
    for Google Maps Geocode API URL formatting requirements.
    """
    url= GMAPS_BASE_URL+'?'+urllib.urlencode({'address':place_name})
    coor_pair= get_json(url)["results"][0]["geometry"]["location"]
    return [coor_pair[u'lat'],coor_pair[u'lng']]


def get_nearest_station(latitude, longitude):
    """
    Given latitude and longitude strings, return a (station_name, distance)
    tuple for the nearest MBTA station to the given coordinates.

    See http://realtime.mbta.com/Portal/Home/Documents for URL
    formatting requirements for the 'stopsbylocation' API.
    """
    url=MBTA_BASE_URL+'?'+urllib.urlencode({'api_key':"wX9NwuHnZU2ToO7GmGR9uw",'lat':latitude,'lon':longitude,'format':'json'})
    f = urllib2.urlopen(url)
    response_text = f.read()
    response_data = json.loads(response_text)
    return response_data

def find_stop_near(place_name):
    """
    Given a place name or address, print the nearest MBTA stop and the 
    distance from the given place to that stop.
    """
    coor_pair=get_lat_long(place_name)
    data=get_nearest_station(coor_pair[0],coor_pair[1])
    print data['stop'][0]['distance']+' miles to',data['stop'][0]['stop_name']

find_stop_near("Ashburton Park Boston")
