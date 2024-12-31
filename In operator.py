S=input("Enter a word:")
L=input("Enter a letter:")
found= False
for i in range (len(S)):
    if S[i]==L:
        found=True
if found:
    print(f"The letter {L} is in the word {S}")
else:
    print(f"The letter{L}is not in the word{S}.")

