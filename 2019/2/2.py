import sys

noun = 0
verb = 0

for noun in range(100):
    for verb in range(100):
        #read inputs into dictionary
        file = open("input.txt","r")
        ctr = 0
        opsArr = []
        for i in file:
            ops = i.split(',')
            for j in ops:
                j.rsplit()
                opsArr.append(int(j))

        #replace pos 1 with 12 and pos 2 with 2
        opsArr[1] = noun
        opsArr[2] = verb

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

        if opsArr[0] == 19690720:
            sys.exit('noun: ' + str(noun) + ' verb: ' + str(verb))
        else:
            print('still computing - val is ' + str(opsArr[0]) + ' noun: ' +str(noun) + ' verb: ' + str(verb))
