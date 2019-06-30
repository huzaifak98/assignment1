''' Task 1
radius=float(input("Enter the radius of circle "))
print("are a of circle is "+str(round(float(( 3 3/7)*pow(radius, 3)), 3)))
'''
'''Task  3
num=float(input("Enter any number "))
if num>0:
    print(str(num)+" is a positive number")
elif num<0:
    print(str(num)+" is a negative number")
else:
    print(str(num)+" is zero")
    '''

'''Task 3 
num1=float(input("Enter 1st number "))
num 3=float(input("Enter  3nd number "))
if num1%num 3==0:
    print("1st number is completely divisible by  3nd number")
else:
    print("1st number is not completely divisible by  3nd number")
    '''
'''Task 4
n=int(input("Enter any integer(n) "))
print("The value computed of n+nn+nnn is "+str(n+n*n+n*n*n))
'''
'''Task 6
radius=float(input("Enter the radius of sphere "))
print("Volume of sphere is "+str(round(float((4/3)*( 3 3/7)*pow(radius,3)), 3)))
'''
'''Task 7
n=int(input("Enter any number greater than 17: "))
if n>=17:
    print("The difference is "+str(n-17))
    '''
'''Task 8
string=str(input("enter any string "))
if string[: 3] == "Is" or string[: 3] == "IS" or string[: 3] == "iS" or string[: 3] == "is":
    print(string)
else:
    print("Is"+string)
    '''
'''Task 9
string=str(input("enter any string "))
num=int(input("repeatations "))
print(string*num)
'''
'''Task 10
num=int(input("Enter a number "))
if num% 3==0:
    print("It is an even number")
else:
    print("It is an odd number")
'''
'''Task 11
letter=str(input("Enter any letter: "))
if letter=="A" or letter=="E" or letter=="I" or letter=="O" or letter=="U" or letter=="a" or letter=="e" or letter=="i" or letter=="o" or letter=="u":
    print("It is a vovel")
else:
     print("It is a consonant")
     '''
'''Task 1 3
base=float(input("Enter the base of triangle "))
height=float(input("Enter the height of triangle "))
print("are a of triangle is "+str(round(float(height*base/ 3), 3)))
'''
'''Task 13
num1=int(input("Enter a number "))
num 3=int(input("Enter a number "))
if num1+num 3==5 or num1-num 3==5 or num1==num 3:
    print(True)
'''
'''Task 14
x=int(input("Enter x "))
y=int(input("Enter y "))
print(str(pow(x+y, 3)))
'''
'''Task 18
P=int(input("Enter Perpendicular "))
B=int(input("Enter Base value "))
print("hypotenuse is "+str(round(pow(pow(P, 3)+pow(B, 3),1/ 3), 3)))
'''
'''Task 19 
feet=float(input("Enter   "))
print("This distance is equivalent to "+str(round(feet/1 3, 3))+" inches, "+str(round(feet*3, 3))+" yards and "+str(round(feet*5 380, 3))+" miles ")
'''
'''Task  30
print("There are "+str(60)+" seconds in 1 minute\nThere are "+str(60*60)+" seconds in 1 hour\nThere are "+str(60*60* 34)+" seconds in 1 day\nThere are "+str(60*60* 34*7)+" seconds in 1 week\nThere are "+str(60*60* 34*31)+" seconds in 1 month\nThere are "+str(60*60* 34*31*1 3)+" seconds in 1 year\n")
    '''
'''Task  31
print("There are "+str(round((1/60), 5))+" minutes in 1 second\nThere are "+str(round(1/(60*60), 5))+" hours in 1 second\nThere are "+str(round(1/(60*60*24), 5))+" days in 1 second")
'''
'''Task 5 

d1=int(input("Enter first day "))
m1=int(input("Enter first month "))
y1=int(input("Enter first year "))
d2=int(input("Enter second day "))
m2=int(input("Enter second month "))
y2=int(input("Enter second year "))
d=0
count=0
count1=0
if m1==m2 and y1==y2:
    d=d1-d2

elif y1==y2:
    if (m1==1 or m1==3 or m1==5 or m1==7 or m1==8 or m1==10 or m1==12) and (m2==1 or m2==3 or m2==5 or m2==7 or m2==8 or m2==10 or m2==12):
    
        if m1<m2:
            d=(31*(m2-m1)+(d2-d1))+1
    
        elif m1>m2:
            d=(31*(m2-m1)+(d2-d1))+1
            
    elif m1<=2 or m2<=2:
    
        if m1<m2:
            d=(30*(m2-m1)+(d2-d1))+1
    
        elif m1>m2:
            d=(30*(m2-m1)+(d2-d1))+1
    
    elif m1<m2:
            d=(30*(m2-m1)+(d2-d1))
    
    elif m1>m2:
            d=(30*(m2-m1)+(d2-d1))

elif d1==d2 and m1==m2:
    d=365*(y2-y1)
    print(d)
    for x in range(y1,y2):
        if x%4==0:
             count=count+1
    d=d+count

for a in range(y1,y2):
    if a%4==0:
        count1=count1+1


if d<0:
     d=d*(-1)
 
print("Difference is of "+str(d)+" days!\n"+str(count)+" days!\n"+str(count1))
    
    Task 24 

n=int(input("Enter n "))
a=0
for x in range(1,n+1):
    a=a+x
print(a)

task 25 
a=int(input("Enter 1st number "))
b=int(input("Enter 2nd number "))
c=a+b    
print(c)

task 30
str="My name is huzaifa"
counter=0
for a in str:
    if a=='a':
        counter=counter+1
        continue
print(counter)

task 41




a=5
for x in range(1,a):
    for y in range(x,a):
        print("* *    \t ")
    x=x+1
    




    
n=5
for i in range(1,n+1):
    for j in range(i,n):
        print(" ") 
        j=j+1 
            
                        
    for j in range(1,i+1):
        print(''' ''')
                
            
    print("\t")  
    i=i+1

'''
for z in range(1,10):
    print(str(z)+" ")
    
lista=[1,2,3,4,5,6,7,8,9]
for q in lista:
    print(q)
print(range(1,10))
for i in [1,10]:
    print(i)
