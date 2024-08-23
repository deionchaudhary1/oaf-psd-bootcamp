from abc import ABC, abstractmethod
import requests
from enum import Enum

class Environment(Enum):  
    TEST = 0  
    PROD = 1

class Service(ABC):
    @abstractmethod
    def get_job_data(self):
        pass

class MockService(Service):
    def get_job_data(self):
        '''
        This method generates mock time and temperature data
        that resembles the same output from the Open Meteo API.
        It then puts the data into a 2D array with a marker to signify
        that it is a mock data set.
        '''
        data = '''{
        "__CLASS__": "Adzuna::API::Response::JobSearchResults",
        "results": [
            {
            "salary_min": 50000,
            "longitude": -0.776902,
            "location": {
                "__CLASS__": "Adzuna::API::Response::Location",
                "area": [
                "UK",
                "South East England",
                "Buckinghamshire",
                "Marlow"
                ],
                "display_name": "Marlow, Buckinghamshire"
            },
            "salary_is_predicted": 0,
            "description": "JavaScript Developer Corporate ...",
            "__CLASS__": "Adzuna::API::Response::Job",
            "created": "2013-11-08T18:07:39Z",
            "latitude": 51.571999,
            "redirect_url": "http://adzuna.co.uk/jobs/land/ad/129698749...",
            "title": "Javascript Developer",
            "category": {
                "__CLASS__": "Adzuna::API::Response::Category",
                "label": "IT Jobs",
                "tag": "it-jobs"
            },
            "id": "129698749",
            "salary_max": 55000,
            "company": {
                "__CLASS__": "Adzuna::API::Response::Company",
                "display_name": "Corporate Project Solutions"
            },
            "contract_type": "permanent"
            },
            ... another 19 ads here ...
        ]
        }
        '''
        link = "http://adzuna.co.uk/jobs/land/ad/129698749..."
        return link

class APIService(Service):
    def get_job_data(self):
        '''
        This method asks for user input of the location of where they would
        like to get temperature data from and then makes an API request call for weather and time in that location.
        It puts the data into their respective arrays.
        Finally, puts the data into a 2D array with a marker to signify
        that it is an API data set.
        '''
        what = input("Please enter the job's title: ")
        where = input("Please enter a preffered location: ")
        salary_min = input("Please enter your minimum salary: ")

        url = "https://api.adzuna.com/v1/api/jobs/us/search/1"
        params = {
            "app_id": "a37cffb8",  # replace with your app ID
            "app_key": "7b817d31493e87cf2039cdf3cf24e06e",  # replace with your API key
            "results_per_page": 1,
            "what": what,
            "where": where,
            "salary_min": salary_min
        }

        req = requests.get(url, params=params)
        response = req.json()
        #print(response.json())
            #can display pnly the link to the jobs
        
        if req.status_code == 200:
            link = response[1][7]
            return link

class ServiceFactory(ABC):
    def create_service(self, num):
        '''
        This method generates either an API or Mock Service instance based on
        the input value.
        '''
        if num == Environment.PROD:  
            return APIService()  
        elif num == Environment.TEST:  
            return MockService()





'''
{'__CLASS__': 'Adzuna::API::Response::JobSearchResults', 'results': [{'adref': 'eyJhbGciOiJIUzI1NiJ9.eyJpIjoiNDgxNzA1NDQwOSIsInMiOiJZSE1GWndSYzd4R3laVlQ0OXp2d2Z3In0.83-ruCblnD-mKXYP82apWgvzP3tqETZ3wsUZtn9Ryvc', 'category': {'__CLASS__': 'Adzuna::API::Response::Category', 'tag': 'it-jobs', 'label': 'IT Jobs'}, '__CLASS__': 'Adzuna::API::Response::Job', 'latitude': 37.773969, 'longitude': -122.410448, 'salary_min': 147184.58, 'salary_is_predicted': '1', 'location': {'__CLASS__': 'Adzuna::API::Response::Location', 'display_name': 'SoMa, San Francisco', 'area': 
['US', 'California', 'San Francisco', 'SoMa']}, 'redirect_url': 'https://www.adzuna.com/details/4817054409?utm_medium=api&utm_source=a37cffb8', 'created': '2024-08-08T09:55:35Z', 'contract_type': 'contract', 'salary_max': 147184.58, 'company': {'display_name': 'Welkin Technologies', '__CLASS__': 'Adzuna::API::Response::Company'}, 'description': 'Job Description: Experience in python programming in Windows and Linux environment Experience in managing development lifecycle and moving product from dev, test, QA Experience in unit testing and code reviews Experienced in building and deploying cloud-based production applications Experience with git and structured version control Senior-level experienced in PyWinRM, SCP, Flask, and other python modules Experience in working with Docker and creating and publishing container to release product…', 'id': '4817054409', 'title': 'Python Developer'}], 'count': 139, 'mean': 170501.33}

Example
{
  "__CLASS__": "Adzuna::API::Response::JobSearchResults",
  "results": [
    {
      "salary_min": 50000,
      "longitude": -0.776902,
      "location": {
        "__CLASS__": "Adzuna::API::Response::Location",
        "area": [
          "UK",
          "South East England",
          "Buckinghamshire",
          "Marlow"
        ],
        "display_name": "Marlow, Buckinghamshire"
      },
      "salary_is_predicted": 0,
      "description": "JavaScript Developer Corporate ...",
      "__CLASS__": "Adzuna::API::Response::Job",
      "created": "2013-11-08T18:07:39Z",
      "latitude": 51.571999,
      "redirect_url": "http://adzuna.co.uk/jobs/land/ad/129698749...",
      "title": "Javascript Developer",
      "category": {
        "__CLASS__": "Adzuna::API::Response::Category",
        "label": "IT Jobs",
        "tag": "it-jobs"
      },
      "id": "129698749",
      "salary_max": 55000,
      "company": {
        "__CLASS__": "Adzuna::API::Response::Company",
        "display_name": "Corporate Project Solutions"
      },
      "contract_type": "permanent"
    },
    ... another 19 ads here ...
  ]
}
'''