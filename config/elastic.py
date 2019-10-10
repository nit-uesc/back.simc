"""."""
import requests
import json

config = json.load(open('config/elastic_config.json', 'r'))

URL = 'http://localhost:9200/resumes'
# #
delete = requests.delete(URL)


headers = {
    'Content-Type: application/json'
}
put = requests.put(URL, data=config)
