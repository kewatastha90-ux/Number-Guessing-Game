import random

# Computer will choose a random number between 1 and 100
secret_number = random.randint(1, 100)
attempts = 0

print("--- Welcome to the Number Guessing Game! ---")
print("I have thought of a number between 1 and 100. Try to guess it!")

while True:
    # Taking input from the user
    guess = int(input("Your Guess: "))
    attempts += 1
    
    # Checking if the guess is correct, too high, or too low
    if guess < secret_number:
        print("Too low! Try a bigger number.")
    elif guess > secret_number:
        print("Too high! Try a smaller number.")
    else:
        print(f"Congratulations! You guessed the correct number in {attempts} attempts.")
        break
