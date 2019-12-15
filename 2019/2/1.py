file = open("input.txt","r")

ctr = 0
opsArr = []

#read inputs into dictionary
for i in file:
    ops = i.split(',')
    for j in ops:
        j.rsplit()
        opsArr.append(int(j))

#replace pos 1 with 12 and pos 2 with 2
opsArr[1] = 12
opsArr[2] = 2

#perform computations (1 = x+y and 2 = x*y where x & y are positions in the dict)
while opsArr[ctr] != 99:
    if opsArr[ctr] == 1:
        print(ctr)
        opsArr[opsArr[ctr+3]] = opsArr[opsArr[ctr+1]] + opsArr[opsArr[ctr+2]]
        ctr += 4

    if opsArr[ctr] == 2:
        print(ctr)
        opsArr[opsArr[ctr+3]] = opsArr[opsArr[ctr+1]] * opsArr[opsArr[ctr+2]]
        ctr += 4

#print position 0
print(opsArr[0])
