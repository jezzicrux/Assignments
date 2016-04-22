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
    firstlist.sort()
    listlength = len(firstlist)
    print(firstlist[0],firstlist[listlength-1])


main()