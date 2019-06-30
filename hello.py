''''''
a=int(input("Enter 1st number "))
b=int(input("Enter 2nd number "))
operator=input("Enter operator from the following +,-,/,*,% \n")
if operator=='+':
    print(a+b)
elif operator=='-':
    print(a-b)
elif operator=='*':
   print(a*b)
elif operator=='/':
    print(a/b)
elif operator=='%':
    print(a%b) 
'''
if False:
    print("True")
    print("True")
    print("True")
    print("True")
    print("True")

else:
    print("false")
    print("false")
    print("false")
    print("false")
    print("false")
print("Other")'''
'''
isCNICvalid=input("Do you have CNIC ")

if isCNICvalid.lower() =='yes':
    gender=input("Gender ")
    if gender.lower()=='male':
        print("Goto Booth A")
    elif gender.lower() =='Female':
        print("Goto B")
else:
        print("Go home!")
'''