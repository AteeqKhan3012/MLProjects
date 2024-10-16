weather_data = [
    {"New Delhi": {"temperature": 25, "humidity": 60, "wind_speed": 10}},
    {"Hyderabad": {"temperature": 28, "humidity": 72, "wind_speed": 6}},
    {"Lucknow": {"temperature": 30, "humidity": 75, "wind_speed": 11}},
    {"Kerala": {"temperature": 38, "humidity": 80, "wind_speed": 16}},
    {"Bengaluru": {"temperature": 36, "humidity": 69, "wind_speed": 13}},
    {"Chennai": {"temperature": 45, "humidity": 76, "wind_speed": 10}},
    {"Jaipur": {"temperature": 39, "humidity": 66, "wind_speed": 15}}
]

print("WELCOME TO THE WEATHER BROADCAST")
print("Below are the options to get the weather report of a city:")
print("1. Get weather report of a specific city")
print("2. Get weather report of cities with temperature above 35°C")
print("3. Exit")

while True:
    choice = input("Enter your choice (1/2/3):")

    if choice == "1":
        print("Below are the options to get the weather report of a city:")
        print("1. New Delhi ")
        print("2. Hyderabad ")
        print("3. Lucknow ")
        print("4. Kerala ")
        print("5. Bengaluru ")
        print("6. Chennai ")
        print("7. Jaipur ")

        city_name = {
            "1": "New Delhi",
            "2": "Hyderabad",
            "3": "Lucknow",
            "4": "Kerala",
            "5": "Bengaluru",
            "6": "Chennai",
            "7": "Jaipur"
        }

        city_option = input("Enter the city's option (1-7): ")

        city_found = False
        for data in weather_data:
            for key, value in data.items():
                if key == city_name[city_option]:
                    print(f"Weather in {key} is:")
                    print(f"Temperature is: {value['temperature']}°C")
                    print(f"Humidity is: {value['humidity']}%")
                    print(f"Wind Speed is: {value['wind_speed']} km/h")
                    city_found = True
                    break        
        if not city_found:
            print("City not found in our database")
            continue            
                   
    elif choice == "2":
        # Filter the cities with temperature above 30°C
        hot_cities = [list(data.keys())[0] for data in weather_data if list(data.values())[0]['temperature'] > 35]
        print("Cities with temperature above 30°C :")
        for city in hot_cities:
            for data in weather_data:
                if list(data.keys())[0] == city:
                    print(f"{city}: {list(data.values())[0]['temperature']}°C")

    else:
        print("Exiting the program")
        break
