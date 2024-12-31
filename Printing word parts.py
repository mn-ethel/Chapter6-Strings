S=input("Enter a word with the letter 'a':")
if 'a' in S:
    locate_a=S.index('a')
    first_part=S[:locate_a+1]
    second_part=S[locate_a+1:]
    print(first_part)
    print(second_part)

