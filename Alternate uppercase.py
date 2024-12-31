S = input("Enter a word: ")
result = ''.join(c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(S))
print(result)
