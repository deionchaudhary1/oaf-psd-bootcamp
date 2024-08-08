'''
This program is inteded to use the Open Meteo API
and output an API and Mock plot of temperatures in a location of your choice
'''

from abc import ABC, abstractmethod
import requests
import matplotlib.pyplot as plt
from enum import Enum  

class Environment(Enum):  
    TEST = 0  
    PROD = 1

class Service(ABC):
    @abstractmethod
    def get_weather_data(self):
        pass


class MockService(Service):
    def get_weather_data(self):
        '''
        This method generates mock time and temperature data
        that resembles the same output from the Open Meteo API.
        It then puts the data into a 2D array with a marker to signify
        that it is a mock data set.
        '''
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
        mockArray2d = [dates, temps, 0]
        return mockArray2d


class APIService(Service):
    def get_weather_data(self):
        '''
        This method asks for user input of the location of where they would
        like to get temperature data from and then makes an API request call for weather and time in that location.
        It puts the data into their respective arrays.
        Finally, puts the data into a 2D array with a marker to signify
        that it is an API data set.
        '''
        '''
        base_url = "https://api.open-meteo.com/v1/forecast"  
        params = {}  
        params['latitude'] = latitude    # float  
        params['longitude'] = longitude    # float  
        params['hourly'] = daily_weather_variable    # string with "temperature_2m"  

        response = requests.get(base_url, params=params)
        '''
        latitude = input("Please write your latitude: ")
        longitude = input("Please write your longitude: ")
        response = requests.get(f'https://api.open-meteo.com/v1/forecast?{latitude}=52.52&{longitude}=13.41&hourly=temperature_2m')
        if response.status_code == 200 and 'hourly' in response and 'time' in response and 'temperature_2m' in response:
            dates = response.json()['hourly']['time']
            temps = response.json()['hourly']['temperature_2m']
        apiArray2d = [dates, temps, 1]
        return apiArray2d
        


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


class Handler:
    def __init__(self, service): #the service will be injected
        self.sv = service

    def plot(self):
        '''
        This method takes the data of the given Service and generates a plot
        of the temperature over time.
        '''

        values = []
        values = self.sv.get_weather_data() #error is here; Attribute of service
            #returns the 2d array
        plt.scatter(values[0], values[1])
        if values[2] == 1:
            plt.title("API Service")
        elif values[2] == 0:
            plt.title("Mock Service")
        plt.show()


def main():
    '''
    This main function calls both the Mock and API Services and makes sure
    that it outputs a plot of the temperature over time for both.
    '''
    #API
    api_factory = ServiceFactory()
    api = api_factory.create_service(1) #api is the instance of the API Service
    ans = Handler(api)
    ans.plot() #returns the data

    #MOCK
    mock_factory = ServiceFactory()
    mock = mock_factory.create_service(0)
    mo = Handler(mock)
    mo.plot() #returns the data


if __name__ == "__main__":
    main()

#TO FIX ERROR: the service parameter for the Handler class is a NoneType
    #What I changed:
        #put the plotting in the Handler class, the services just return data - !
        #rename getting() to get_weather_data() - !
        #renamed mockService() to MockService()
        #user input for location and f-string
        #verifying data and include all API data
        #changed Handler's give_out() to plot() - !