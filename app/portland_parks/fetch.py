#!/usr/bin/python
import json
import math
import urllib2
from pprint import pprint

class PortlandParksAPIDataProcessor(object):
    portland_parks = []
    portland_basketball_parks = []
    LATITUDE = 45.525368
    LONGITUDE = -122.685879
    COORDS = {'lon': LONGITUDE, 'lat': LATITUDE}
    COUNT = 50
    EARTHS_RADIUS = 3963.1676 
    BASKETBALL_COURT_AMENITY_NAME = 'basketball court'
    PORTLAND_PARKS_API_URL = 'http://api.civicapps.org/parks/near/{lon},{lat}?count={cnt}'

    def distance_between(self, coord1, coord2):
        # Convert latitude and longitude to 
        # spherical coordinates in radians.
        degrees_to_radians = math.pi/180.0
            
        # phi = 90 - latitude
        phi1 = (90.0 - coord1['lat'])*degrees_to_radians
        phi2 = (90.0 - coord2['lat'])*degrees_to_radians
            
        # theta = longitude
        theta1 = coord1['lon']*degrees_to_radians
        theta2 = coord2['lon']*degrees_to_radians
            
        # Compute spherical distance from spherical coordinates.
            
        # For two locations in spherical coordinates 
        # (1, theta, phi) and (1, theta, phi)
        # cosine( arc length ) = 
        #    sin phi sin phi' cos(theta-theta') + cos phi cos phi'
        # distance = rho * arc length
        cos = (math.sin(phi1)*math.sin(phi2)*math.cos(theta1 - theta2) + 
               math.cos(phi1)*math.cos(phi2))
        arc = math.acos( cos )
        distance = arc * self.EARTHS_RADIUS

        return distance

    def get_basketball_parks(self, parks):
        basketball_parks = []
        for park in parks:
            if park.get('amenities') and self.BASKETBALL_COURT_AMENITY_NAME in park['amenities'] and\
               self.distance_between(self.COORDS, {'lon': park['loc'].get('lon'),
                                                   'lat': park['loc'].get('lat')}) <= 10.0:
                basketball_parks.append(park)
            if len(basketball_parks) >= 5:
                break
        return basketball_parks

    def fetch_park_data(self):
        PORTLAND_PARKS_DATA_NAME = 'results'
        # Request a list of Portland Parks near the the given coordinates
        request = urllib2.Request(self.PORTLAND_PARKS_API_URL.\
                                  format(lon=self.LONGITUDE, lat=self.LATITUDE, cnt=self.COUNT)) 
        response = urllib2.urlopen(request)
        response = response.read()
        self.portland_parks = json.loads(response).get(PORTLAND_PARKS_DATA_NAME)
        # Process the list of all parks to find parks within 10 mi of Urban Airship that have basketball courts
        self.portland_basketball_parks = self.get_basketball_parks(self.portland_parks)
        return self.portland_basketball_parks


if __name__ == '__main__':
    portland_parks_data_processor = PortlandParksAPIDataProcessor()
    portland_basketball_parks = portland_parks_data_processor.fetch_park_data()
    pprint(portland_basketball_parks)
    print(len(portland_basketball_parks))
