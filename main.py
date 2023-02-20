import random

class HangmanGame:
    def __init__(self):
        self.score = 0
        self.guesses = []
        self.max_fails = 10
        self.fails = 0
        self.word = self.select_word()
    def select_word(self):
        language = input("Choose a language between French and English. (fr/en)\n")
        if language.lower() == "fr" or language.lower() == "french":
            with open("words-fr.txt") as dictionary:
                words = dictionary.readlines()
                word = random.choice(words).strip()
                return word
        elif language.lower() == "en" or language.lower() == "english":
            with open("words-en.txt") as dictionary:
                words = dictionary.readlines()
                word = random.choice(words).strip()
                return word
        else:
            print("Language is not supported!")
            self.select_word()
    def play(self):
        while True:
            print("Word: ", end = "")
            for letter in self.word:
                if letter in self.guesses:
                    print(letter, end = "")
                else:
                    print("_", end = "")
            print()
            print("Guesses: ", end = "")
            for letter in self.guesses:
                print(letter, end="")
            print()
            guess = input("Guess a letter: ").lower()
            if guess in self.guesses:
                print("You've already guessed that letter!")
                continue
            self.guesses.append(guess)
            if guess in self.word:
                print("Correct!")
            else:
                self.fails += 1
                print("Incorrect.")
            if set(self.word) <= set(self.guesses):
                print(f"You win! Word: {self.word}")
                self.score +=1
                play_again = input(f"Play again ? (y/n) Current score: {self.score}.\n")
                if play_again.lower() == "y" or play_again.lower() == "yes":
                    self.reset()
                else:
                    print(f"Thank you for playing! You ended up with a score of {self.score}!")
                    break
            elif self.fails >= self.max_fails:
                print("You lose. The word was: ", self.word)
                play_again = input(f"Play again ? (y/n) Current score: {self.score}.\n")
                if play_again.lower() == "y" or play_again.lower() == "yes":
                    self.reset()
                else:
                    print(f"Thank you for playing! You ended up with a score of {self.score}!")
                    break
    def reset(self):
        self.guesses = []
        self.fails = 0
        self.word = self.select_word()

game = HangmanGame()
game.play()
