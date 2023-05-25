import random

def guess_number():
    number = random.randint(1, 100)  # Generate random number between 1 and 100
    attempts = 0
    while True:
        guess = int(input("Guess a number between 1 and 100: "))
        attempts += 1
        if guess == number:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            play_again()
            break
        elif guess < number:
            print("Too low. Try again.")
        else:
            print("Too high. Try again.")
            
def play_again():
    play_again = input("Do you want to play again? Type 'yes' or 'no': ")
    if play_again == "yes":
        guess_number()
    else:
        print("Thank you for playing. Goodbye!")
        
guess_number()

