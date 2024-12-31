user_message=input("Enter the message to be encrypted:")
first_set=user_message[0::3]
second_set=user_message[1::3]
cipher_result=first_set+second_set
print(f"The rail fence ciper is:{cipher_result}")