firstlist = []
def main():
    iterations = getIterations()
    getNumbers(iterations)
    sorting_list()


def getIterations():
    return int(input("How many numbers do you want to input? "))

def getNumbers(y):
    for a in range(0, y):
        numberlist = int(input("Enter your number. "))
        firstlist.append(numberlist)

def sorting_list():
    for k in range(len(firstlist)):
        b = 0
        for m in range(len(firstlist) - 1):
            if firstlist[b] > firstlist[b + 1]:
                temp =firstlist[b]
                firstlist[b] = firstlist[b + 1]
                firstlist[b + 1] = temp
            b = b + 1
    print("The min number is:", firstlist[0],"The max number is:", firstlist[len(firstlist)-1])

main()