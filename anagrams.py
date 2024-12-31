S=input("Enter a word to generate anagram:")
import random
letters=list(S)
random.shuffle(letters)
anagram=''.join(letters)
print(f"One random anagram of {S} is {anagram}")
