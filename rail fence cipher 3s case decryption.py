def decrypt_rail_fence_3(encrypted):
    length = len(encrypted)
    rails = 3  # Number of rails

    # Calculate the number of characters per rail (rounded up)
    chars_per_rail = (length + rails - 1) // rails

    decrypted = [''] * length

    # Fill the rails
    for i in range(rails):
        start = i * chars_per_rail
        end = min((i + 1) * chars_per_rail, length)
        decrypted[i::rails] = encrypted[start:end]

    return ''.join(decrypted)

if __name__ == "__main__":
    user_input = input("Enter the message to be decrypted: ")
    decrypted_message = decrypt_rail_fence_3(user_input)
    print(decrypted_message)

