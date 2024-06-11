import re

Australia = ["Sydney", "Melbourne", "Brisbane", "Perth"]
UAE = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]
India = ["Mumbai", "Bangalore", "Chennai", "Delhi"]

city1 = input('Enter first city name:').strip().title()
city2 = input('Enter second city name:').strip().title()

if re.match(r"^[A-Za-z\s]+$", city1) and re.match(r"^[A-Za-z\s]+$", city2):

    if city1 in Australia and city2 in Australia:
        print('Both are from the same country:Australia.')
    elif city1 in UAE and city2 in UAE:
        print('Both are from the same country:UAE.')
    elif city1 in India and city2 in India:
        print('Both are from the same country:India.')
    else:
        print('Both are not from the same country.')
else:
    print('Error: Please enter valid city names without digits or special characters.')
