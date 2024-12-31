name=input("Enter your name:")
words=name.split()
capitalized_word=[]
for word in words:
    capitalized_word.append(word.capitalize())
capitalized_name=''.join(capitalized_word)
print(capitalized_name)
