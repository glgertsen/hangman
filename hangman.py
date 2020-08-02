import random

def import_words(word_file):
    with open(word_file,"r") as f:
        words = f.readlines()
        words = [x.strip() for x in words if len(x.strip()) > 4]
        return words

def choose_word(word_list):
    return random.choice(word_list)

def generate_blanks(word):
    
    blanks = "_ " * len(word)
    
    return blanks.strip()

def check_letter(word, letters):
    guess = ""
    for c in word:
        if c not in letters:
            guess += "_ "
        else:
            guess += c
            guess += " "

    return(guess.strip())

def get_guess(letters):
    
    while True:
        guess = input("Enter the letter you would like to guess: ")
    
        if not guess.isalpha() or len(guess) != 1:
            print("Please enter a letter.")
            continue

        if guess in letters:
            print("This letter has already been guessed. Please select a new letter")
            continue
            
        return guess.lower()

def main():

    letters = []

    word_list = import_words("word_list.txt")
    chosen_word = choose_word(word_list)
    current_letters = generate_blanks(chosen_word) 
    
    while '_' in current_letters:
        print(current_letters)
        guessed_letter = get_guess(letters)
        letters.append(guessed_letter)
        current_letters = check_letter(chosen_word, letters)

    print("You guessed the word! The word was \"" + chosen_word + "\"!")


if __name__ == "__main__":
    main()