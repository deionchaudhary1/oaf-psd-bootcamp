'''
This is where my project will be.
Right now, it is testing my API call
'''

import requests

url = "https://api.adzuna.com/v1/api/jobs/us/search/1"
params = {
    "app_id": "a37cffb8",  # replace with your app ID
    "app_key": "7b817d31493e87cf2039cdf3cf24e06e",  # replace with your API key
    "results_per_page": 10,
    "what": "python developer",
    "where": "San Francisco"
}

response = requests.get(url, params=params)
print(response.json())