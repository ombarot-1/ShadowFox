import random

count1 = 0
count6 = 0
count6twotimes = 0

PrivousRoll = None

for x in range(20):
    roll = random.randint(1,6)

    if roll == 6:
        count6 += 1

        if PrivousRoll == 6:
            count6twotimes += 1

    if roll == 1:
        count1 += 1

    PrivousRoll = roll

print(f"Number of times rolled a 6: {count6}")
print(f"Number of times rolled a 1: {count1}")
print(f"Number of times rolled two 6s in a row:{count6twotimes}")