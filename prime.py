c=0
x=int(input("Enter a number "))

for a in range(2,x):
    if x%a==0:
        print("Not Prime ")
        c=0
        break
    else:
        c=c+1
        continue
if c>0 or x==2:
    print("Prime")
'''

# taking input from user
number = int(input("Enter any number: "))

# prime number is always greater than 1
if number > 1:
    for i in range(2, number):
        if (number % i) == 0:
            print(number, "is not a prime number")
            break
    else:
        print(number, "is a prime number")

# if the entered number is less than or equal to 1
# then it is not prime number
else:
    print(number, "is not a prime number")
    '''