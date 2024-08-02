'''
This program is inteded to use the Open Meteo API
and output an API and Mock plot of temperatures in the next 24 hours
'''

from abc import ABC, abstractmethod
import requests
import matplotlib.pyplot as plt

class Service(ABC):
    @abstractmethod
    def getting(self):
        pass

class mockService(Service):
    def getting(self):
        #create a 
        dates = ["2024-08-02T02:00",
      "2024-08-02T03:00",
      "2024-08-02T04:00",
      "2024-08-02T05:00",
      "2024-08-02T06:00",
      "2024-08-02T07:00",
      "2024-08-02T08:00",
      "2024-08-02T09:00",
      "2024-08-02T10:00",
      "2024-08-02T11:00",
      "2024-08-02T12:00",
      "2024-08-02T13:00",
      "2024-08-02T14:00",
      "2024-08-02T15:00",
      "2024-08-02T16:00",
      "2024-08-02T17:00",
      "2024-08-02T18:00",
      "2024-08-02T19:00",
      "2024-08-02T20:00",
      "2024-08-02T21:00",
      "2024-08-02T22:00",
      "2024-08-02T23:00",
      "2024-08-03T00:00",
      "2024-08-03T01:00"]
        temps = [19.4, 18.8, 18.2, 17.8, 17.7, 17.7, 17.9, 18, 18.1, 18.6, 18.8, 18.8, 18.9, 19.2, 19.4, 19.6, 19.4, 19.5, 19.4, 19, 18.5, 18, 17.6, 17.3]
        plt.scatter(dates, temps)
        plt.title("Mock Service")
        plt.show()


class APIService(Service):
    def getting(self):
        response = requests.get("https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&hourly=temperature_2m")
        dates = response.json()['hourly']['time'][0:24]
        temps = response.json()['hourly']['temperature_2m'][0:24]
        plt.scatter(dates, temps)
        plt.title("API Service")
        plt.show()


class ServiceFactory(ABC):
    def create_service(self, num):
        #if num = 1, then APIService, if num = 0, then mockService
        if num == 1:
            return APIService()
        elif num == 0:
            return mockService()


class Handler:
    def __init__(self, service): #the service will be injected
        self.sv = service

    def give_out(self):
        self.sv.getting()
        #calls the class methods, no matter if its from the API or Mock

def main():
    #API
    api_factory = ServiceFactory()
    api = api_factory.create_service(1) #api is the instance of the API Service
    ans = Handler(api)
    ans.give_out() #returns the data

    #MOCK
    mock_factory = ServiceFactory()
    mock = mock_factory.create_service(0) #api is the instance of the API Service
    mo = Handler(mock)
    mo.give_out() #returns the data
    

if __name__ == "__main__":
    main()
