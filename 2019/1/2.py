import math

file = open("input.txt","r")

sum = 0
fuel = 0
exFuel = 0

#have to add extra fuel for each module, then add total fuel for all modules at the end
for i in file:
    i = i.rstrip()
    if i:
        print(i)
        fuel = math.trunc((int(i)/3)) - 2
        exFuel = fuel
        while fuel > 0:
            fuel = math.trunc((int(fuel)/3)) - 2
            if fuel > 0:
                print(fuel)
                exFuel += fuel
        sum += exFuel

print(sum)
