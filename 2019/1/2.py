import math

file = open("input.txt","r")

sum = 0
fuel = 0

for i in file:
    i = i.rstrip()
    if i:
        sum += math.trunc((int(i)/3)) - 2

fuel = sum
exFuel = 0

while fuel > 0:
    print(fuel)
    fuel = math.trunc((int(fuel)/3)) - 2
    exFuel += fuel

exFuel += sum

print(exFuel)
