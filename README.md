
This is a program that collects a list of possible countries that a user would like to visit and the user's max price he is willing to pay to go there(his budget).
This list is located in an excel file and is gotten using sheety api
Using a flight website api, the program checks the list of countries(from the sheet) and compares the user's budget price to the actual cost of the trip on the flight website.
Then when it has gotten a price close to or below the user's budget, it sends over a message through sms that this is the country he can afford to go to.