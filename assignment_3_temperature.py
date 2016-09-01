def main():
    tempprogram()

def tempprogram():
    x="cookies"
    a=True
    while(a==True):
        fahrenheittemp = int(input("What is the current temperature in Fahrenheit? "))
        celsiustemp = ((fahrenheittemp - 32) * (5 / 9))
        print("The temperature is ", fahrenheittemp, " in Fahrenheit and ", celsiustemp, " in Celsius.")
        answer = input("Would you like to convert another temperature? ")
        if answer == 'Yes' or answer=='yes':
            a=True
        else:
            a= False

main()