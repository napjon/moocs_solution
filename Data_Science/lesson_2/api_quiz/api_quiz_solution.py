import json
import requests
import pprint

def api_get_request(url):
    # In this exercise, you want to call the last.fm API to get a list of the
    # top artists in Spain.
    #
    # Once you've done this, return the name of the number 1 top artist in Spain.
    data = requests.get(url).text
    data = json.loads(data)
    #country_data = data['country']
    pp = pprint.PrettyPrinter(depth = 4)
    #pp.pprint(data)
    top_artists = data['topartists']['artist']
    #[e['name'] for e in top_artists]
    return top_artists[0]['name'] # return the top artist in Spain

