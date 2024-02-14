import random
import os
from hangman_words import word_list
from hangman_art import logo


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def display_game_state(display, lives):
    clear_screen()
    print(logo)
    from hangman_art import stages
    print(stages[lives])
    print(f"{' '.join(display)}")


chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

print(f'Pssst, the solution is {chosen_word}.')
display = ["_" for _ in range(word_length)] # creating the blanks

while not end_of_game:
    display_game_state(display, lives)
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You've already guessed {guess}")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            display_game_state(display, lives)
            print("You lose.")

    if "_" not in display:
        end_of_game = True
        display_game_state(display, lives)
        print("You win.")


