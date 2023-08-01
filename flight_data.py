
import requests
import datetime as d
from data_manager import DataManager

KIWI_ENDPOINT = "https://api.tequila.kiwi.com/v2/search"

class FlightData(DataManager):
    #This class is responsible for structuring the flight data.


    def __init__(self):
        super().__init__()
        
        self.now = d.datetime.now()
        self.tomorrow = self.now.day + 1
        self.year = self.now.year
        self.six_month = self.now.month + 3
        self.month = self.now.month
        self.flight_list = []
        self.header = {
            "Authorization": "Bearer bcking"
        }
        self.kiwi_header = {
            "apikey" : "pbdEAKSrnttHBB0NN2JJs34DFdjGb8HM",
        }


    def iata(self):
        """ Gets iata code from data manager. """
        iatadict = self.obtain_iata()

        for key,value in iatadict.items():
            self.flight_list.append(self.compare_flight(value))
        return self.flight_list


    def compare_flight(self,iata):
        self.kiwi_params = {
            "fly_from" : "LON", 
            "fly_to" : iata,
            "date_from" : f"{self.tomorrow}/{self.month}/{self.year}",
            "date_to" : f"{self.tomorrow}/{self.six_month}/{self.year}",
        }

        self.response = requests.get(url= KIWI_ENDPOINT, params= self.kiwi_params, headers= self.kiwi_header)
        self.response.raise_for_status()
        city_price = self.response.json()["data"][0]["price"]
        city_iata = self.response.json()["data"][0]["cityCodeTo"]
        city = self.response.json()["data"][0]["cityTo"]
        new_dict = {"city" : city,
                    "city_iata_code": city_iata,
                    "destination_price": city_price}
        return new_dict
        
    

