# -*- coding: utf-8 -*-
"""

This program demonstrates the capability of the Yelp Fusion API
by using the Search API to query for businesses by a search term and location,
and the Business API to query additional information about the top result
from the search query.



"""
from __future__ import print_function

import argparse
import json
import pprint
import requests
import sys
import urllib


# This client code can run on Python 2.x or 3.x.  Your imports can be
# simpler if you only need one of those.
try:
    # For Python 3.0 and later
    from urllib.error import HTTPError
    from urllib.parse import quote
    from urllib.parse import urlencode
except ImportError:
    # Fall back to Python 2's urllib2 and urllib
    from urllib2 import HTTPError
    from urllib import quote
    from urllib import urlencode


# OAuth credential placeholders that must be filled in by users.
# You can find them on
# https://www.yelp.com/developers/v3/manage_app
CLIENT_ID = 'KPFZgpg3seQJlXpTW0w_-A'
CLIENT_SECRET = 'eQerfaqoKOJEVM2WXQ3Catfl0rYFhbhUeqaymFR2ujZX8ctgK7CSqvGiEPysascE'


# API constants, you shouldn't have to change these.
API_HOST = 'https://api.yelp.com'
SEARCH_PATH = '/v3/businesses/search'
BUSINESS_PATH = '/v3/businesses/'  # Business ID will come after slash.
AUTO_PATH = '/v3/autocomplete'
TOKEN_PATH = '/oauth2/token'
GRANT_TYPE = 'client_credentials'


# Defaults for our simple example.
DEFAULT_TERM = 'dinner'
DEFAULT_TEXT = 'dinner'
DEFAULT_LOCATION = 'San Francisco, CA'
SEARCH_LIMIT = 3


def obtain_bearer_token(host, path):
    """Given a bearer token, send a GET request to the API.

    Args:
        host (str): The domain host of the API.
        path (str): The path of the API after the domain.
        url_params (dict): An optional set of query parameters in the request.

    Returns:
        str: OAuth bearer token, obtained using client_id and client_secret.

    Raises:
        HTTPError: An error occurs from the HTTP request.
    """
    url = '{0}{1}'.format(host, quote(path.encode('utf8')))
    assert CLIENT_ID, "Please supply your client_id."
    assert CLIENT_SECRET, "Please supply your client_secret."
    data = urlencode({
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'grant_type': GRANT_TYPE,
    })
    headers = {
        'content-type': 'application/x-www-form-urlencoded',
    }
    response = requests.request('POST', url, data=data, headers=headers)
    bearer_token = response.json()['access_token']
    return bearer_token


def request(host, path, bearer_token, url_params=None):
    """Given a bearer token, send a GET request to the API.

    Args:
        host (str): The domain host of the API.
        path (str): The path of the API after the domain.
        bearer_token (str): OAuth bearer token, obtained using client_id and client_secret.
        url_params (dict): An optional set of query parameters in the request.

    Returns:
        dict: The JSON response from the request.

    Raises:
        HTTPError: An error occurs from the HTTP request.
    """
    url_params = url_params or {}
    url = '{0}{1}'.format(host, quote(path.encode('utf8')))
    headers = {
        'Authorization': 'Bearer %s' % bearer_token,
    }

    print(u'Querying {0} ...'.format(url))

    response = requests.request('GET', url, headers=headers, params=url_params)

    return response.json()


def search(bearer_token, text):
    """Query the Autocomplete API by a search text

    Args:
        text (str): The search term passed to the API.

    Returns:
        dict: The JSON response from the request.
    """

    url_params = {
        'text': text.replace(' ', '+'),
        'latitude': 32.826382, # NG coordinates
        'longitude': -117.129813,
    }
    return request(API_HOST, AUTO_PATH, bearer_token, url_params=url_params)


def get_businesses(bearer_token, businesses):
    """Query the Business API by business ID's.

    Args:
        businesses (dict): The businesses from autocomplete, contains name and id

    Returns:
        dict: The JSON response from the request.
    """

    # businesses
    business_path = BUSINESS_PATH + business_id

    return request(API_HOST, business_path, bearer_token)

    responses = []
    for business in businesses:
        response = {}

        business_id = business['id']

        business_path = BUSINESS_PATH + business_id

        # business api call
        business_meta = request(API_HOST, business_path, bearer_token)

        # name
        response['name'] = business['name']

        # business address
        response['location']['address1'] = business_meta['location']['address1']

        # business city
        response['location']['city'] = business_meta['location']['city']

        # business rating
        response['rating'] = business_meta['rating']

        # business image
        response['image_url'] = business_meta['image_url']

        responses.append(response)

    return responses


# def query_api(text):
def get_autocomplete(text):
    """Queries the API by the input values from the user.

    Args:
        text (str): The search text to query.
    """
    bearer_token = obtain_bearer_token(API_HOST, TOKEN_PATH)

    response = search(bearer_token, text)

    businesses = response.get('businesses')

    if not businesses:
        return

    responses = get_businesses(bearer_token, businesses)

    return responses
