def main():
    print("Celsius"," Fahernheit")
    a=0
    for a in range(0,101,5):
        celsiustemp=a
        fahrenheittemp=((celsiustemp*9/5) + 32)
        print(celsiustemp,"         ",fahrenheittemp)

main()