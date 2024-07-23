'''
This program is inteded to create a mock class that takes in a city and uses a url and outputs temp and humidity
'''

class Weather:
    def __init__(self, city: str):
        self.temp = 23 
        self.humidity = 45
        #test values; in reality we would get these from a url
    def get_temp(self):
        return self.temp
    def get_humidity(self):
        return self.humidity
    
someCity = Weather("Barcelona")
print(someCity.get_humidity())
print(someCity.get_temp())
