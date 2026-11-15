import random

computer = random.randint(1,100)
print(computer)
attempt = 0
while True:

    user_guess = input("Enter Your Guess(1-100): ")
    try:
        user_guess = int(user_guess)

        if user_guess < 1 or user_guess > 100:
            print("Out of range! Please guess a number between 1 and 100.")
            continue
        attempt += 1
                
        if user_guess == computer:
            print(f"You Guessed it right in {attempt} attempts!")
            break

        elif user_guess < computer:
            print("Guess Higher!")
            

        else: 
            print("Guess Lower!")
           
    except ValueError:
        print("Invalid input! Please enter a valid number.")