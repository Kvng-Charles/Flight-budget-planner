
import requests
SHEETY_ENDPOINT = "https://api.sheety.co/342711153ee6386e0684960bdc9f7151/flightDeals/prices"
# SHEETY_UPDATE_ENPOINT = "https://api.sheety.co/342711153ee6386e0684960bdc9f7151/flightDeals/prices/"


class DataManager:



    def __init__(self):
        self.header = {
            "Authorization": "Bearer bcking"
        }
        self.id = 2
        
        
    # ---------------------- GUIDE ------------------------------#
    #This class is responsible for talking to the Google Sheet.

    #TODO: Collect informantion from the Google sheet.
    # Step 1: Get hold of sheety api.
    # Step 2: Get the information in from the sheety api.
    # Step 3: Send out the received information.

    # -------------------------------------------------------------#

    def get_sheety_city_info(self):
        """ Gets info from google sheets """
        self.response = requests.get(url= SHEETY_ENDPOINT, headers= self.header)
        self.response.raise_for_status()
        results = self.response.json()
        city_list = [ each["city"] for each in results["prices"] if "city" in each]
        return city_list

    
    def update_iata(self, new_dict):
        """ Collect iata codes from dictionary """
        
        for key,value in new_dict.items():
            data = {
                "price" : {
                    "iataCode" : value,
                }
            }
            self.update = requests.put(url= f"https://api.sheety.co/342711153ee6386e0684960bdc9f7151/flightDeals/prices/{self.id}", json= data, headers= self.header)
            self.id += 1
        # self.respons = requests.get(url= SHEETY_ENDPOINT, headers= self.header)
        # self.respons.raise_for_status()
        print(self.update.text)



    def obtain_iata(self):
        self.respond = requests.get(url= SHEETY_ENDPOINT, headers= self.header)
        self.respond.raise_for_status()
        results = self.respond.json()
        iata_dict = { each["city"] : each["iataCode"] for each in results["prices"] if "city" in each}
        return iata_dict


