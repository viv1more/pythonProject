travel_log = [
    {
        "Country ": "India", "City": ["Jalgaon", "Nashik", "Pune", "Sambhajinagar"],
        "visits": 15
    },
    {
        "Country ": "Russia", "City": ["Saransk", "Саранск", "Republic of Mordovia", "Volga"],
        "visits": 10
    }
]


def add_new_country(country="Country", city="City", visits="visits"):
    result = ', '.join(city[:-1]) + ' and ' + city[-1]
    print(f"You have Visited {country} {visits} Times")
    print(f"and the Cities You Visited are  {result}")


add_new_country("France", ["Marseilles ", "Nantes", "Biarritz", "Carcassonne"], 5)

add_new_country("India",["Jalgaon", "Nashik", "Pune", "Sambhajinagar", "Mumbai"], 15)
# print(travel_log[1])
