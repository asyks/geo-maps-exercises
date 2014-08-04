#!/usr/bin/python
import json
import urllib2
from pprint import pprint

class ISSAPIDataProcessor(object):
    iss_detail_data = None
    ISS_SATELLITES_LIST_URL = 'https://api.wheretheiss.at/v1/satellites'
    ISS_SATELLITE_DETAIL_URL = 'https://api.wheretheiss.at/v1/satellites/%s'

    def fetch_iss_data(self):
        ISS_RESPONSE_DATA_NAME = 'iss'
        # Request a list of ISS satellites
        request = urllib2.Request(self.ISS_SATELLITES_LIST_URL) 
        response = urllib2.urlopen(request)
        response = response.read()
        satellites = json.loads(response)
        # Retrieve the id of the satellite with name 'iss' from the response data
        iss_data = (satellite for satellite in satellites 
                    if satellite.get('name') == ISS_RESPONSE_DATA_NAME) 
        iss_id = int(iss_data.next().get('id'))
        iss_detail_data = None
        if iss_id is not None:
            # If the iss_id is not None then try retrieving detailed info on the satellite with that id
            request = urllib2.Request(self.ISS_SATELLITE_DETAIL_URL % iss_id) 
            response = urllib2.urlopen(request)
            response = response.read()
            iss_detail_data = json.loads(response)
            self.iss_detail_data = iss_detail_data
        return iss_detail_data 

    def fetch_iss_lat_long_data(self):
        iss_detail_data = self.fetch_iss_data()
        latitude, longitude = iss_detail_data.get('latitude'), iss_detail_data.get('longitude')
        return latitude, longitude 
        

if __name__ == '__main__':
    iss_data_processor = ISSAPIDataProcessor()
    latitude, longitude = iss_data_processor.fetch_iss_lat_long_data()
    pprint(iss_data_processor.iss_detail_data)
    print('latitude: %s, longitude: %s' % (latitude, longitude))
