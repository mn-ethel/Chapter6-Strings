letters='abcdefghijklmnopqrstuvwxyz'
for i in range (len(letters)):
    new_letters=letters[i:]+letters[:i]
    print(new_letters)
