import math

file = open("input.txt","r")

sum = 0

for i in file:
    i = i.rstrip()
    if i:
        sum += math.trunc((int(i)/3)) - 2

print(sum)
