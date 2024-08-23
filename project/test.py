import requests

'''
what = input("Please enter the job's title: ")
where = input("Please enter a preffered location: ")
salary_min = input("Please enter your minimum salary: ")
'''


url = "https://api.adzuna.com/v1/api/jobs/us/search/1"
params = {
    "app_id": "a37cffb8",  # replace with your app ID
    "app_key": "7b817d31493e87cf2039cdf3cf24e06e",  # replace with your API key
    "results_per_page": 1,
    "what": "Developer",
    "where": "San Francisco",
    "salary_min": "30000"
}

req = requests.get(url, params=params)
response = req.json()
#print(response.json())
#can display pnly the link to the jobs
        
if req.status_code == 200:
    link = response[1]
    print(link)