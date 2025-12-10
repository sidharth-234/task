import random

word = "python"
scrambled = "".join(random.sample(word, len(word)))

print("Unscramble this word:", scrambled)
guess = input("Your guess: ")

if guess == word:
    print("Correct! 🎉")
else:
    print("Wrong! The word was:", word)
