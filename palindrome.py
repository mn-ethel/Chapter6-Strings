S=input("Enter a word:")
forward=S[0:]
backward=S[::-1]
if forward==backward:
    print ("The word" ,S, "is a palindrome")
else:
    print("The word", S, "is not a palindrome")