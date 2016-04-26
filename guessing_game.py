import random
x=random.randint(1,10)
def main():
    print("Welcome to the number guessing game. Please guess a number between 1-10.")
    print(x)
    guess = int(input("What is your number guess? "))
    counter=1
    while counter!=3 and x!=guess:
        if counter!=3 and x!=guess:
            if guess==(x-2) or guess==(x+2):
                print("Warm")
            elif guess==(x-1) or guess==(x+1):
                print("Hot")
            else:
                print("Cold")
            print("Incorrect guess. Please try again.")
            guess = int(input("What is your number guess? "))
            counter=counter+1
            if x == guess:
                print("Congratulation! You won. Thanks for playing.")
            elif counter==3 and x!=guess:
                print("Too many guesses. Please play again.")
main()