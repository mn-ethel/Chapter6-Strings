S=input("Enter a word:")
L=input("Enter a letter:")
found=False # Track if the letter is found
for i in range(len(S)):
    if S[i]==L:
        print(f"The first occurrence of the letter {L}in {S} is at position {i}")
        found=True
        break # break the loop once the first occurrence of the letter is found.
    if not found: # if there is no occurrence of the letter in the word
        print(f"There is no occurrence of letter {L} in {S}")
