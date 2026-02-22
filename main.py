import random
import list_of_words
import logo_stages
# use predefined wordlist

lives = 6

# print some logo.
print(logo_stages.logo)
chosen_word = random.choice(list_of_words.word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []
guessed_letters = []
while not game_over:

    # lives left.
    print(f"****************************{lives}/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()

    # duplicate guess.


    if guess in guessed_letters:
        print(f"You have already guess {guess}")
        continue
    else:
        guessed_letters.append(guess)

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)

    # wrong letter guess

    if guess not in chosen_word:
        print(f"You guessed {guess}. {guess} is not in the word. You lose a life.")
        lives -= 1

        if lives == 0:
            game_over = True

            # show correct word.
            print(f"***********************YOU LOSE**********************")
            print(f"correct word is {chosen_word}")

    if "_" not in display:
        game_over = True
        print(f"IT WAS {chosen_word}!")
        print("****************************YOU WIN****************************")

    # lives left
    print(logo_stages.stages[lives])

