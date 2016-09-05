def main():
    print("Welcome to the Program! Please enter the value of A,B,C and X at the corresponding prompts")
    everythingValid=True
    while(everythingValid==True):
        try:
            the_program_correct()
            everythingValid = False
        except:
            print("Invalid Input: Please try again")
            everythingValid=False

def the_program_correct():
    A=int(input("What is the value of A? "))
    B=int(input("What is the value of B? "))
    C=int(input("What is the value of C? "))
    Xvalue = int(input("What is the value of X? "))
    totalvalue=((A*(Xvalue**2))+(B*Xvalue)+(C))
    print("The following quadratic was entered: ",end="")
    print(A,end="")
    print("X^2+",end="")
    print(B,end="")
    print("X+",end="")
    print(C)
    print("The value of the quadratic is",totalvalue)

main()