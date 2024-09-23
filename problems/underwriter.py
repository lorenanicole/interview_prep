# from flask import Flask
from fastapi import FastAPI, Request
from collections import OrderedDict
from tripadvisorapi.api import TripadvisorApi
import requests
import urllib.parse
import uvicorn
from pyngrok import ngrok
# from contextlib import asynccontextmanager
# from loguru import logger
from pydantic import BaseModel
from geopy.geocoders import Nominatim


key = "64EB5A2A0E0A4343882C97AFA61631A3"
api = TripadvisorApi(key)

class Cache:
    def __init__(self, max_size):
        self.max_size = max_size
        self.cache_values = OrderedDict([])
        self.hits = 0
        self.misses = 0

    def get(self, key):
        if key in self.cache_values:
            self.hits += 1
            self.cache_values.move_to_end(key)
            return self.cache_values[key]
        else:
            self.misses += 1
            return -1

    def put(self, key, value):
        self.cache_values[key] = value
        self.cache_values.move_to_end(key)

        if len(self.cache_values) > self.max_size:
            self.cache_values.popitem(last=False)

    def __repr__(self):
        return f"Cache: {self.cache_values}, Misses: {self.misses}, Hits: {self.hits}"
        


# app = Flask(__name__)
cache = Cache(128)
NGROK_AUTH_TOKEN = '2lrrdmqaucPiVnbBGyfPLytWezM_6eDLJj1rqG4mL6e7ZB9Qt'
# NGROK_DOMAIN = 'https://crisp-splendid-cockatoo.ngrok-free.app'
NGROK_EDGE = 'edghts_2lrs2vkTKqaujls98pcVfagKcVC'
APP_PORT = 8000

# @asynccontextmanager
# async def lifespan(app: FastAPI):
#     logger.info("Setting up Ngrok Tunnel")
#     # ngrok.set_auth_token(NGROK_AUTH_TOKEN)
#     ngrok.set_auth_token(NGROK_AUTH_TOKEN)
#     ngrok.forward(
#         addr=APP_PORT,
#         labels=NGROK_EDGE,
#         proto="labeled",
#     )
#     yield
#     print('Public URL:', ngrok.public_url)
#     logger.info("Tearing Down Ngrok Tunnel")
#     ngrok.disconnect()

class BusinessRequest(BaseModel):
    name: str
    address: str | None = None

app = FastAPI() # lifespan=lifespan)

geolocator = Nominatim(user_agent="my_user_agent")

@app.get('/hello')
def get_hello():
    return {'hello': 'world'}

# Requirement 1.) WebAPI 
# @app.route('/business', methods=['GET'])
@app.get('/business')
def get_business(business_request: BusinessRequest, request: Request):
    referer = request.headers.get('referer')
    print(f'Here is referer: {referer}')
    business_name = business_request.name
    address = business_request.address
    # Requirement 2.) Check if processed business
    
    data = scrape_location_data('Chicago')
    # ("latitude is :-" ,loc.latitude,"\nlongtitude is:-" ,loc.longitude)
    
    # Requirement 3.) Get trip advisor data
    # Allow async processing
    # https://tripadvisor-content-api.readme.io/reference/overview

    # url = f"https://api.content.tripadvisor.com/api/v1/location/search?searchQuery={urllib.parse.quote_plus(business_name)}&category=hotel&language=en&key=64EB5A2A0E0A4343882C97AFA61631A33"
    # headers = {"Content-Type": "application/json", "X-TripAdvisor-API-Key": key} # "referer": referer}
    # response = requests.get(url, headers=headers)
    


    

    # for review in soup.find_all("div", {"class": "review-container"}):

    # Requirement 4.) Call data science API
    # to get on inferences

def scrape_location_data(query):
    """
    scrape search location data from a given query.
    e.g. "New York" will return us TripAdvisor's location details for this query
    """
    print(f"scraping location data: {query}")
    # the graphql payload that defines our search
    # note: that changing values outside of expected ranges can block the web scraper
    payload = [
            {
                "variables": {
                    "request": {
                        "query": query,
                        "limit": 10,
                        "scope": "WORLDWIDE",
                        "locale": "en-US",
                        "scopeGeoId": 1,
                        "searchCenter": None,
                        # note: here you can expand to search for differents.
                        "types": [
                            "LOCATION",
                            # "QUERY_SUGGESTION",
                            # "RESCUE_RESULT"
                        ],
                        "locationTypes": [
                            "GEO",
                            "AIRPORT",
                            "ACCOMMODATION",
                            "ATTRACTION",
                            "ATTRACTION_PRODUCT",
                            "EATERY",
                            "NEIGHBORHOOD",
                            "AIRLINE",
                            "SHOPPING",
                            "UNIVERSITY",
                            "GENERAL_HOSPITAL",
                            "PORT",
                            "FERRY",
                            "CORPORATION",
                            "VACATION_RENTAL",
                            "SHIP",
                            "CRUISE_LINE",
                            "CAR_RENTAL_OFFICE",
                        ],
                        "userId": None,
                        "context": {},
                        "enabledFeatures": ["articles"],
                        "includeRecent": True,
                    }
                },
                # Every graphql query has a query ID that doesn't change often:
                "query": "84b17ed122fbdbd4",
                "extensions": {"preRegisteredQueryId": "84b17ed122fbdbd4"},
            }
        ]

    # we need to generate a random request ID for this request to succeed
    import random
    import string
    random_request_id = "".join(
        random.choice(string.ascii_lowercase + string.digits) for i in range(180)
    )
    headers = {
        "X-Requested-By": random_request_id,
        "Referer": "https://www.tripadvisor.com/Hotels",
        "Origin": "https://www.tripadvisor.com",
    }
    # result = await client.post(
    #     url="https://www.tripadvisor.com/data/graphql/ids",
    #     json=payload,
    #     headers=headers,
    # )
    import json
    result = requests.get(
        "https://www.tripadvisor.com/data/graphql/ids",
        json=payload,
        headers=headers,
    )
    return result


if __name__ == "__main__":
    ngrok.set_auth_token("2lrrdmqaucPiVnbBGyfPLytWezM_6eDLJj1rqG4mL6e7ZB9Qt")
    public_url = ngrok.connect(APP_PORT).public_url
    # app.add_middleware(
    #     TrustedHostMiddleware, allowed_hosts=[public_url] 
    # )
    # curl -X GET 'https://15b9-68-250-115-105.ngrok-free.app/business' -H 'Content-Type: application/json' -d '{"name": "Hotel Robey", "address": "Chicago"}'

    print(f"ngrok tunnel {public_url}")
    uvicorn.run(app, port=APP_PORT, forwarded_allow_ips=[public_url])
