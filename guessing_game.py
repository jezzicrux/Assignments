import random
x=random.randint(1,10)
def main():
    print("Welcome to the number guessing game. Please guess a number between 1-10.")
    print(x)
    guess = int(input("What is your number guess? "))
    while x!=guess:
        if x!=guess:
            print("Incorrect guess. Please try again.")
            guess = int(input("What is your number guess? "))
            if x == guess:
                print("Congratulation! You won. Thanks for play.")
main()