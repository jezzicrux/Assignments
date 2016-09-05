'''for numlist in range (2,21):
    if (numlist % 2  == 0):
        print (numlist,"Divisible by 2")
    elif (numlist % 3  == 0):
        print(numlist,"Divisible by 3")
    else:
        print (numlist,"Prime number")'''

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