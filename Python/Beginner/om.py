
try:
    P = float(input('Enter principal amount(INR):'))
    R = float(input('Enter rate of interes(INR):'))
    T = int(input('Enter time(In Years):'))
    print(f'Simple Intrest:{P * R * T / 100}₹')
except:
    print('Error:Enter only digits!')