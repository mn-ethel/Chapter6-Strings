integer=input("Enter a large integer:")
reverse=integer[::-1]#reverse the integer for easy grouping
chunks = [reverse[i:i + 3] for i in range(0, len(reverse), 3)]#Insert commas every 3 digits
formatted_number = ",".join(chunks)[::-1]
print(formatted_number)



