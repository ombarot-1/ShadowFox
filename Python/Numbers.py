# 1. Write a function that takes two arguments, 145 and 'o', and uses the `format` function to return a formatted string.
#  Print the result. Try to identify the representation used.
number = 145
character = 'o'

formatted_string = "{:0>5}{}".format(number, character)
print(formatted_string)

# 2. In a village, there is a circular pond with a radius of 84 meters. Calculate the area of the pond using the formula:
#  Circle Area = π r^2. (Use the value 3.14 for π) Bonus Question: If there is exactly 1.4 liters of water in a square
#  meter, what is the total amount of water in the pond? Print the answer without any decimal point in it. Hint: Circle
#  Area = π r^2 Water in the pond = Pond Area Water per Square Meter
pi = 3.14
r = 84
sm = 1.4
area = pi * r * r

print(f'The total amount of water in the pond:{int(area*sm)} liters')
# 3. If you cross a 490meterlong street in 7 minutes, calculate your speed in meters per second. Print the answer without
# any decimal point in it. Hint: Speed = Distance / Time
print(f'Speed in meters per second:{int(490/(7*60))}')