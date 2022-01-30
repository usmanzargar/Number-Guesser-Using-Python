import random

print("Welcome to the Number Guesser!")
prompt = input("Please type a natural number upto which you want to guess: ")

if prompt.isdigit():
    prompt = int(prompt)

    if prompt <= 0 :
        print("Please type a number larger than 0")
        quit()


else :
        print("Please type a number next time")
        quit()


r = random.randrange(0, prompt)
guesses = 0

while True :
    guesses += 1
    guess = input("Make a guess: ")

    if guess.isdigit():
        guess = int(guess)
    else :
        
        print("Please type a number next time.")
        continue

    if guess == r :
        print (" Correct! Congratulations, you have guessed correctly")
        break
    else :
        if guess > r :
            print ("You guessed above the number.")
        else :
            print ("You guessed below the number.")


print(" You got it in", guesses, "guesses")


