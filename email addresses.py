number=int(input("How many email addresses do you want to enter?"))
S=input("Enter email address:")
e_list=[]
prof_count=0
student_count=0
for i in range(number):
    e_list.append(S)
    if S[-16:-12]=='prof':
        prof_count=prof_count+1
    elif S[-16:-12]=='dent':
        student_count=student_count+1
    else:
        print("Invalid input please check the email you have entered")
print("The number of professor email accounts is,",prof_count)
print("The number of student email accounts is,",student_count)



