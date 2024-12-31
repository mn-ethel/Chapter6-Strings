S=input("Enter some text:")
length=len(S)
print("The length of the string is,", length)
repeat=S*10
print(repeat,sep=",")
first_character=S[0]
print("The first character of the string is,",first_character)
first_three_characters=S[0:3]
print("The first three characters of the string are,",first_three_characters)
last_three_characters=S[-3: ]
print("The last three characters of the string are,",last_three_characters)
string_backwards=S[::-1]
print("The string backwards is,",string_backwards)
if length >=7:
 seventh_character=S[6]
 print ("The seventh character of the string is",seventh_character)
else:
    print("The number of character is less than seven")
missing_characters=S[1:-1]
print("The string minus the first and last character is ,", missing_characters)
upper_case=S.upper()
print("The string in uppercase characters is,",upper_case)
replacement=S.replace('a','e')
print("The replacement of \'a\' with \'e\' ,gives :",replacement)
Space_replace=length*' '
print("Character replacement with space is:",Space_replace)







