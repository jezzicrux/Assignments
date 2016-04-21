def main():
    print("Celsius"," Fahernheit")
    a=0
    while a<=100:
        celsiustemp=a
        fahrenheittemp=((celsiustemp*9/5) + 32)
        print(celsiustemp,"         ",fahrenheittemp)
        a=a+5
main()
