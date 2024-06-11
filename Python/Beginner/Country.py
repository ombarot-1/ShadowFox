import re

Australia = ["Sydney", "Melbourne", "Brisbane", "Perth"]
UAE = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]
India = ["Mumbai", "Bangalore", "Chennai", "Delhi"]

city = input('Enter city name: ').strip()


if re.match(r"^[A-Za-z]+$", city):
    
    NC = city.title()
    
    if NC in Australia:
        print(f'{city} is in Australia.')
    elif NC in UAE:
        print(f'{city} is in UAE.')
    elif NC in India:
        print(f'{city} is in India.')
    else:
        print('Error: Data is not available!')
else:
    print('Error: Please enter a valid city name without digits or special characters.')
