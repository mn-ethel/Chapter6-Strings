R=input("Enter a word:")
W=input("Enter a word:")
if len(R)!=len(W):
    print("Please enter words with the same number of characters!")
else:
    result=''.join(r+w for r,w in zip(R,W))
    print(result)