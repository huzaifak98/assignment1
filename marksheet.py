   
   
    
   
'''   sub1=int(input("Enter English marks "))
sub2=int(input("Enter Urdu marks "))
sub3=int(input("Enter Maths marks "))
sub4=int(input("Enter Physics marks "))
print("      MARKSHEET ") 
print(" ========================")
print("| Eng\t\t"+str(sub1)+" \t |")
print("| Urd\t\t"+str(sub2)+" \t |")
print("| Mat\t\t"+str(sub3)+" \t |")
print("| Phy\t\t"+str(sub4)+" \t |")
per=(sub1+sub2+sub3+sub4)/4
if(per>=80):
    Grade=("A+")
elif(per>=70 and per<80):
    Grade=("A")
elif(per>=60 and per<70):
    Grade=("B")
elif(per>=50 and per<60):
    Grade=("C")
else:
    Grade=("F")
print("|\t    \t    \t | \n| Grade:"+str(Grade)+" Per:"+str(per)+"%\t |")
print(" ========================")
   




      Download SmartGit 18.2 default settings  non commercial use
Remote 
   
   var1="string"
print(var1)
var1=14
print(var1)

num=55
if num>55:
    print(">")
elif num==55:
    print("55")
else :
    print("<")


print(range(10))

var=list(range(10))
print(var)


for item in range(1,11):
    print(item*2,end= | )
   
   for i in range(1,51):
    if i%2==0:
        print(i,"is even")
    else:
        print(i,"is odd")   
   
rev_value=list(range(50,-1,-1))
print("num",rev_value,"is odd")



   
   list2=list1
numlist1=[1,2,3,4,5,6]
print(list1)
print(list2)
list1.append("10")
print(list1)
print(list2)
a=list1.pop(2)
print(a)
print(list1)
print(list2)
   
   list1=["My","name","is","usman","is"]
for b in list1:
    if b=="is":
        (list1.remove("is"))

print(list1)
   
   a=1
print(a+1)
for name in range(2,81):
    if 73%name==0:
        print("not prime")
    else:
        print("prime")
    
           
   
tuple1=(1,"hello",44,44,44,44)
print(tuple1[0:4])
print(tuple1.index(44))
d=0
for c in tuple1:
    if c==44:
        print(tuple1.index(c))
   
   mylist=[1,2,3,4,5]
mylist2=[]
for x in mylist:
    for y in range(1,5):
        print(x,y)
       2 dafa inputs    

   x=int(input("Enter first number "))
y=int(input("Enter secod number "))

for a in range(x,y+1):
    for b in range(1,11):
        print(str(a)+" x "+str(b)+" = "+str(a*b))
    print("--------------")
   
   lista=[1,2,3,4,5,6,7,8,9]
for q in lista:
    print(q)
'''   
a=int(input("Enter a number to generate its table: "))
for b in range(1,11):
        print(str(a)+" x "+str(b)+" = "+str(a*b))
print("--------------")
