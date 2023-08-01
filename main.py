
#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager

my_travels = DataManager()
# new_list = my_travels.get_sheety_city_info()

# search = FlightSearch(new_list)
# iata_dict = search.city_dict
# my_travels.update_iata(iata_dict)

check_flight = FlightData()
my_flight_list = check_flight.iata()

my_sms = NotificationManager(my_flight_list)

