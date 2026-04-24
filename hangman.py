from words import words
import random


def get_char_map(word):
    char_map = {}
    for i in range(len(word)):
        if word[i] == " ":
            continue
        if word[i] not in char_map:
            char_map[word[i]] = []
        char_map[word[i]].append(i)

    return char_map


def guess_the_word(words):
    is_won = False
    selected_word = random.choice(words)
    char_map = get_char_map(selected_word)
    guess_count = 0
    match_count = len(char_map)
    result_word = [" " if ch == " " else "_" for ch in selected_word]

    while guess_count < 10:
        input_char = input("\n Guess a character a-z: ")
        guess_count += 1
        if input_char not in char_map:
            print("Incorrect guess")
            continue

        match_count -= 1
        positions = char_map[input_char]
        for pos in positions:
            result_word[pos] = input_char

        if match_count == 0:
            is_won = True
            print(f"\n You guessed it right, the word is {selected_word}")
        else:
            temp = " ".join(result_word)
            print(f"Word: {temp}")
   
    if not is_won:
        print(f"You lost, the selected word was {selected_word}")


if __name__ == "__main__":
    guess_the_word(words)
