# 1. Create a variable named pi and store the value 22/7 in it. Now check the data type of this variable.
pi = 22/7
print(type(pi))

# 3. Store the principal amount, rate of interest, and time in different variables and then calculate the Simple Interest
# for 3 years. Formula: Simple Interest = P x R x T / 100

try:
    P = float(input('Enter principal amount(INR):'))
    R = float(input('Enter rate of interes(%):'))
    T = int(input('Enter time(In Years):'))
    print(f'Simple Intrest:{P * R * T / 100}₹')
except:
    print('Error:Enter only digits!')