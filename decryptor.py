encrypted_message=input("Enter the encrypted message:")
mid=(len(encrypted_message)+1)//2
even_letters=encrypted_message[:mid]
odd_letters=encrypted_message[mid:]
original_message=[]
for i in range(mid):
    original_message=original_message.append(even_letters[i])
    if i <len(odd_letters):
        original_message=original_message.append(odd_letters[i])
        final=''.join(original_message)
        print(f"Decrypted message:{final}")

