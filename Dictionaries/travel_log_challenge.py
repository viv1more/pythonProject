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

def add_new_country(country= "Country", city ="City", visits = "visits"):
    a=', '.join(city)

    print(f"You have Visited {a}")
    print(f"You have Visited {country} {visits} Times")





add_new_country("France", ["Marseilles ", "Nantes", "Biarritz",  "Carcassonne"],5)

# print(travel_log)