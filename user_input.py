def main():
    iterations=getIterations()
    getNumbers(iterations)

def getIterations():
    return int(input("How many numbers do you want to input? "))

def getNumbers(y):
    firstlist=[]
    for a in range(0,y):
        numberlist=int(input("Enter your number. "))
        firstlist.append(numberlist)

    q = 0
    minnumber = firstlist[0]
    while q < len(firstlist) - 1:
        q = q + 1
        if firstlist[q] < minnumber:
            minnumber = firstlist[q]
    print("The minimum position integer is", minnumber)

    r = 0
    maxnumber = firstlist[0]
    while r < len(firstlist) - 1:
        r = r + 1
        if firstlist[r] > maxnumber:
            maxnumber = firstlist[r]
    print("The maximum position integer is", maxnumber)

main()