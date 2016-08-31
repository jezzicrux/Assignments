def main():
    temp = int(input("What’s the temperature outside?"))
    if (temp > 60) and (temp < 90):
        print("It's nice out")
    elif temp >= 90:
        print("It's too hot out there. Fine AC")
    elif (temp <= 60) and (temp> 30):
        print("It's chilly, but good.")
    elif temp <= 30:
        print("It's freezing. Time for some hot coco!")
main()