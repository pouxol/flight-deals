from flight_search import FlightSearch
from data_manager import DataManager

data_manager = DataManager()
flight_search = FlightSearch()

data = data_manager.get_data()["prices"]
print(data)

for place in data:
    result = flight_search.searchflight(place["iataCode"])
    lowest_price = place["lowestPrice"]
    for element in result["data"]:
        if lowest_price > element["conversion"]["EUR"]:
            lowest_price = element["conversion"]["EUR"]
    id = place["id"]
    input = {
        "price": {
            "lowestPrice": lowest_price
        }
    }
    data_manager.put_data(input, id)
