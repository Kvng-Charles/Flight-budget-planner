
from twilio.rest import Client



AUTHTOKEN = "YOUR AUTH TOKEN FROM TWILIO API"
ACCOUNT_SID = "YOUR ACCOUNT SID FROM TWILIO API"

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    

    def __init__(self, list_of_cities):
        self.city_list = list_of_cities
        self.send_sms()



    def send_sms(self):
        client = Client(ACCOUNT_SID, AUTHTOKEN)
        message = client.messages \
            .create(
            body = f"{self.city_list}",
            from_= "+12706122295",
            to = "THE NUMBER CONNECTED TO YOUR TWILIO API"
        )

