'''
This program is inteded to create a mock class that takes in a city and uses a url and outputs temp and humidity
'''

class Weather:
    def __init__(self, city: str):
        self.temp = 23 
        self.humidity = 45
        #test values; in reality we would get these from an api
    def get_temp(self) -> int:
        return self.temp
    def get_humidity(self) -> int:
        return self.humidity

city = input("Enter a city: ")
someCity = Weather(city)
print(city + "'s humidity is " + someCity.get_humidity())
print(city + "'s temperature is " + someCity.get_temp())
