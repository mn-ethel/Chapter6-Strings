S=input("Enter a formula:")
opening_parentheses=S.count('(')
closing_parentheses=S.count(')')
if opening_parentheses==closing_parentheses:
    print("The number of  opening parentheses is equal to the number of closing parentheses")
else :
    print("The number of opening parentheses is not equal to the number of closing parentheses ")