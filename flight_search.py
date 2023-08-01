
import requests

TEQUILA_ENDPOINT = "https://api.tequila.kiwi.com/locations/query"

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    
    def __init__(self, city_list):
        self.city = city_list
        self.tequila_header = {
            "apikey" : "pbdEAKSrnttHBB0NN2JJs34DFdjGb8HM"
        }
        self.process_city_name(self.city)


    def process_city_name(self,name):
        """ Makes use of city names to get the iata code """
        self.city_dict = {item : self.get_iata(item) for item in name}


    def get_iata(self, city):
        """ Gets the IATA codes of locations """
        self.tequila_paramas = {
                    "location_types" : "city",
                    "term" : city,
                }
        
        self.tequila_response = requests.get(url= TEQUILA_ENDPOINT, params= self.tequila_paramas, headers= self.tequila_header)
        self.tequila_response.raise_for_status()
        receive = self.tequila_response.json()
        self.iata_code = receive["locations"][0]["code"]
        return self.iata_code

