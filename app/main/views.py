import json

from django.views.generic import TemplateView
from django.http import StreamingHttpResponse

from iss.fetch import ISSAPIDataProcessor
from portland_parks.fetch import PortlandParksAPIDataProcessor

class HomeView(TemplateView):
    template_name = 'index.html'

class ISSLocationView(TemplateView):
    template_name = 'iss_map_page.html'

def retrieve_iss_lat_long(request):
    iss_data_processor = ISSAPIDataProcessor()
    iss_data_dict = iss_data_processor.fetch_iss_data()
    return StreamingHttpResponse(json.dumps(iss_data_dict),
                                            content_type='application/json')

class PortlandParksView(TemplateView):
    template_name = 'portland_parks_map_page.html'

def retrieve_portland_basketball_parks(request):
    portland_parks_data_processor = PortlandParksAPIDataProcessor()
    portland_basketball_parks_data_dict = portland_parks_data_processor.fetch_park_data()
    return StreamingHttpResponse(json.dumps(portland_basketball_parks_data_dict),
                                            content_type='application/json')
