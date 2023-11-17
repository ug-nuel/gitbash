import random
from os import system
print("welcome to the number guessing game!")
print("I'm thinking of a number between 1 and 100\n")
random_number = random.randint(1,100)
print(f"hint: the random number is {random_number}")

def compare(guess):
    global random_number
    if guess > random_number:
        return " too high "
    elif guess < random_number:
        return " too low "
    else:
        print(f"you got it!,  the answer was {random_number}")

end_of_game  = False
while not end_of_game:
    difficulty = input("choose a difficulty. type 'easy' or 'hard':\n")
    if difficulty == 'easy':
        attempts = 10
        while attempts > 0 and not end_of_game:
            print(f"you have {attempts} attempts left to guess the number")
            prompt = int(input("Make a guess: "))
            print(compare(prompt))
            if prompt == random_number:
                end_of_game = True
            else:
                attempts -= 1
                if attempts == 0:
                    print("you ran out of guesses , game over")
                    end_of_game = True

    else:
        attempts = 5
        while attempts > 0 and not end_of_game:
            print(f"you have {attempts} attempts left to guess the number")
            prompt = int(input("Make a guess: "))
            print(compare(prompt))
            if prompt == random_number:
                end_of_game = True
            else:
                attempts -= 1
                if attempts < 1:
                    print("you ran out of guesses , game over")
                    end_of_game = True


