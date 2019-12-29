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
    num = (abs(int(size/2) - c-1) + abs(int(size/2) - r-1))
    print("MD is " + str(num))
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

#loop through input file and fill out matrix
for i in file:
    dir = i.split(",")
    for j in dir:
        print("c is: " + str(c) + " r is: " + str(r))
        move = int(j[1:])
        if j[0] == 'R':
            print("move right: " + str(j[1:]))
            right()
        if j[0] == 'L':
            print("move left: " + str(j[1:]))
            left()
        if j[0] == 'U':
            print("move up: " + str(j[1:]))
            up()
        if j[0] == 'D':
            print("move down: " +str(j[1:]))
            down()
    #wire done, reset to central node
    wireNum += 1
    r = int(size/2)
    c = int(size/2)

print(closestMD)
