from typing import Iterator, Optional

import requests, json

SEARCH_URL = "http://search.nintendo-europe.com/en/select"

def _search(
        query: str = "*",
        nsuid: str = None,
) -> Iterator[dict]:
    '''
    make query to noe api
    return a iterator of diction
    useful fields: dates_released_dts[0],excerpt:str,game_categories_txt[],
                   language_availability[],nsuid_txt[0],
                   price_discount_percentage_f:float,price_has_discount_b:bool,
                   price_lowest_f:float,price_regular_f:float,
                   product_code_txt[0],title:str,url:str,popularity:int,
                   image_url:str,image_url_h2x1_s:str
    '''
    rows = 200

    params = {
        "fq": "type:GAME AND system_type:nintendoswitch", # filter
        "q": query, # filter
        "rows": rows, # no of results per response
        "sort": "title asc", # sort
        "start": -rows, # offset
        "wt": "json", # format
    }

    if nsuid:
        params["fq"] += f' AND nsuid_txt:"{nsuid}"'

    while True:
        params["start"] += rows
        response = requests.get(url=SEARCH_URL, params=params)

        if response.status_code != 200:
            break

        json = response.json()['response'].get('docs', [])

        if not len(json):
            break

        for data in json:
            yield data

if __name__ == "__main__":
    res = _search()
    for item in res:
        print(json.dumps(item, indent=4, sort_keys=True))
        input("continue?")
