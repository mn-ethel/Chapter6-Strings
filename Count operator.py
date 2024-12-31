word=input("Enter a word:")
letter=input("Enter a letter:")
count=0
for i in range(len(word)):
    if word[i]==letter:
        count=count+1
print(f"The letter {letter} appears {count} times in the word {word}.")


