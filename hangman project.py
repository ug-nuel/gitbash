import random
from hangman_art import stages, logo
from hangman_words import word_list

# # step 1..... getting input from using and comparing with randomly chosen word
print(logo )
chosen_word = random.choice(word_list)
print(f"the chosen word is {chosen_word}")
word_length = len(chosen_word)
display = []

# step 2 replacing chosen word with blanks/underscore
for _ in range(word_length):
    display += "_"
print(display)

# switching the blanks for the letters of the chosen word
lives = 6
end_of_game = False
while not end_of_game:
    guess = input("guess a letter: ").lower()
    # check guessed leter... if right, switches it with position of blank
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    print(display)
    if "_" not in display:
        end_of_game == True
        print("you win")

    # determines number of lives and ends game once incorrect guesses r# aches
    if guess not in chosen_word:
        print(f"you guessed {guess}, that's not in the word.You lose a life")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("you lose!!!")
    print(stages[lives])

