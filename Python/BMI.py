try:
    height = float(input('Enter height in meters:'))
    weight = float(input('Enter weight in kilograms:'))

    if height <= 0 or weight <= 0:
        print('Error:Enter valid value!')
    
    else:
        BMI = weight / (height)**2
        if BMI >= 30:
            print("Obesity")
        elif BMI >= 25:
            print("Overweight")
        elif BMI >= 18.5:
            print("Normal")
        else:
            print("Underweight")

except:
    print('Error:Enter only digits!')