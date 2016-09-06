'''for numlist in range (2,21):
    if (numlist % 2  == 0):
        print (numlist,"Divisible by 2")
    elif (numlist % 3  == 0):
        print(numlist,"Divisible by 3")
    else:
        print (numlist,"Prime number")'''

'''Finding prime numbers from 2-100 with while loop'''
a=2
while a<=100:
    if (a/2 >1 and a % 2 == 0):
        a=a+1
    elif (a/3 >1 and a % 3 == 0):
        a = a + 1
    elif (a/5 >1 and a % 5 == 0):
        a = a + 1
    elif (a/7 >1 and a % 7 == 0):
        a = a + 1
    elif (a/9 >1 and a % 9 == 0):
        a = a + 1
    else:
        print(a, "Prime number")
        a = a + 1

'''Finding prime numbers from 2-100 with for loop'''
for b in range (2,101):
    if (b / 2 > 1 and b % 2 == 0) or (b / 3 > 1 and b % 3 == 0) or (b / 5 > 1 and b % 5 == 0) or (b / 7 > 1 and b % 7 == 0) or (b / 9 > 1 and b % 9 == 0):
        print(end="")
    else:
        print(b, "Prime number")

'''Finding prime numbers from 2-100 with while loop (condensed)'''
a=2
while a<=100:
    if (a/2 >1 and a % 2 == 0) or (a/3 >1 and a % 3 == 0) or (a/5 >1 and a % 5 == 0) or (a/7 >1 and a % 7 == 0) or (a/9 >1 and a % 9 == 0):
        a = a + 1
    else:
        print(a, "Prime number")
        a = a + 1
