user_message=input("Enter the message to be encrypted:")
even_letters=user_message[0::2]#get the evn indices letters
odd_letters=user_message[1::2]#get the odd indices letters
encrypted_message=even_letters+odd_letters
print(f"Encrypted message:{encrypted_message}")





