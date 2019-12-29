#Manhattan distance of closest crossed wire
#open wire directions input file
file = open("input.txt","r")

#size for matrix size, r and c to track current row and col
size = 20000
r = int(size/2)
c = int(size/2)

#store closest Manhattan Distance
closestMD = size
wireNum = 1

#move keeps count of # of moves to make
move = 0

#init matrix
arr = [['.'] * size for i in range(size)] 

#init starting point from which wires traverse matrix and calc distance from
arr[r][c] = 'o'

def printCross():
    global c, r, closestMD
    print("location of cross: " + str(c) + ", " + str(r))
    num = (abs(int(size/2) - c) + abs(int(size/2) - r))
    if num < closestMD:
        closestMD = num

def right():
    global c, r, move, wireNum
    while move > 0:
        c += 1
        if arr[r][c] == str(wireNum):
            continue
        elif arr[r][c] == '.':
            arr[r][c] = str(wireNum)
        else:
            arr[r][c] = 'X'
            printCross()
        move -= 1
    arr[r][c] = str(wireNum)

def left():
    global c, r, move, wireNum
    while move > 0:
        c -= 1
        if arr[r][c] == str(wireNum):
            continue
        elif arr[r][c] == '.':
            arr[r][c] = str(wireNum)
        else:
            arr[r][c] = 'X'
            printCross()
        move -= 1
    arr[r][c] = str(wireNum)

def up():
    global c, r, move, wireNum
    while move > 0:
        r -= 1
        if arr[r][c] == str(wireNum):
            continue
        elif arr[r][c] == '.':
            arr[r][c] = str(wireNum)
        else:
            arr[r][c] = 'X'
            printCross()
        move -= 1
    arr[r][c] = str(wireNum)

def down():
    global c, r, move, findInt
    while move > 0:
        r += 1
        if arr[r][c] == str(wireNum):
            continue
        elif arr[r][c] == '.':
            arr[r][c] = str(wireNum)
        else:
            arr[r][c] = 'X'
            printCross()
        move -= 1
    arr[r][c] = str(wireNum)

#loop through input file and fill out matrix
for i in file:
    dir = i.split(",")
    for j in dir:
        print("c is: " + str(c) + " r is: " + str(r))
        move = int(j[1:])
        if j[0] == 'R':
            right()
        if j[0] == 'L':
            left()
        if j[0] == 'U':
            up()
        if j[0] == 'D':
            down()
    #wire done, reset to central node
    wireNum += 1
    r = int(size/2)
    c = int(size/2)

print(closestMD)
