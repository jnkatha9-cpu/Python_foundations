import random #import from random library
#generate a random number between 1 and 100
random_number = random.randint (1,100)
#display the random number
print("the random number is:",random_number)
#set the number of attempts
attempts = 10
#keep asking the user while attempts are left
while attempts > 0:
    # ask the user to guess the number
    guess = int(input("Guess the number between 1 and 100: "))

    # compare the guess with the random number
    if guess == random_number:
        print("Correct guess! You win!")
        break

    elif guess > random_number:
        print("Too high!")

    else:
        print("Too low!")

    # reduce the number of attempts
    attempts = attempts - 1

    # display the number of attempts left
    print("You have", attempts, "attempts left")

# if the user runs out of attempts, display the random number
if attempts == 0:
    print("You have run out of attempts! The number was", random_number)