## Where is ISS at?

__Requirements:__

 1. Write a server-side script that can get location data for the ISS (You can use the API available to you http://wheretheiss.at/w/developer for data).
 1. Create a web server that serves the data your module provides.
 1. Create a web page that uses your server to update a Google map indicating the corresponding ground-position of the ISS.

__Solution:__

* My solution can be accessed at path: /iss/

__Components__:
 * Python 2.7 - liscense: http://opensource.org/licenses/Python-2.0
 * Django 1.6 - liscense: https://github.com/django/django/blob/master/LICENSE

## Shoots some hoops
 
__Requirements:__

 1. Write a server-side script that can get location data for (5) City of Portland parks within 10 miles of the UA PDX office that have basketball courts (You can use the CivicApps API - City Parks Dataset available to you http://api.civicapps.org/ for data).
 1. Create a web server that serves the data your module provides.
 1. Create a web page that uses your server to update a Google map indicating the corresponding location of parks in relation to the UA PDX office.

__Solution:__

* My solution can be accessed at path: /hoops/

__Components__:
 * Python 2.7 - liscense: http://opensource.org/licenses/Python-2.0
 * Django 1.6 - liscense: https://github.com/django/django/blob/master/LICENSE
 * My solution relies heavily on John D. Cook's distance between two coordinates algorthimn, which has been granted to the public domain, located here: http://www.johndcook.com/python_longitude_latitude.html
