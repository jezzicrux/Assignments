a=2
while a<=100:
    if a % 2 == 0:
        a=a+1
    elif a % 5 == 0:
        a=a+1
    else:
        print(a , "Oh no!")
        a=a+1