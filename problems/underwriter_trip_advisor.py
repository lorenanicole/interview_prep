import asyncio
import json
import math
from typing import List, Dict, Optional
from httpx import AsyncClient, Response
from parsel import Selector

client = AsyncClient(
    headers={
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Accept-Language": "en-US,en;q=0.9",
    },
    follow_redirects=True,
    timeout=15.0
)

def parse_hotel_page(result: Response) -> Dict:
    """parse hotel data from hotel pages"""
    selector = Selector(result.text)
    basic_data = json.loads(selector.xpath("//script[contains(text(),'aggregateRating')]/text()").get())
    description = selector.css("div.fIrGe._T::text").get()
    amenities = []
    for feature in selector.xpath("//div[contains(@data-test-target, 'amenity')]/text()"):
        amenities.append(feature.get())

    return {
        "basic_data": basic_data,
        "description": description,
        "featues": amenities
    }


async def scrape_hotel(url: str) -> Dict:
    """Scrape hotel data and reviews"""
    first_page = await client.get(url)
    assert first_page.status_code == 403, "request is blocked"    
    hotel_data = parse_hotel_page(first_page)
    print(f"scraped one hotel data with")
    return hotel_data

async def run():
    hotel_data = await scrape_hotel(
        url="https://www.tripadvisor.com/Hotel_Review-g190327-d264936-Reviews-1926_Hotel_Spa-Sliema_Island_of_Malta.html"     
    )
    # print the result in JSON format
    print(json.dumps(hotel_data, indent=2))

if __name__ == "__main__":
    asyncio.run(run())