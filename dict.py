'''student={"Name":"Huzaifa","Fname":"Jawed"}
print(student["Name"])
student["Age"]=21
print("Name" in student)
my_key="Contact"
student[my_key]="0335-3459429"
print(student.keys())
print(student.values())
print(student.items())
for value in student.values():
    print(value)
for k,v in student.items():
    print(str(k)+"|"+str(v)+"|")

tpl=(2,4,6)
a,b,c=tpl


students=[]

while True:
    print("Press 1 to Add Student")
    print("Press 2 to Delete Student")
    print("Press 3 to Search Student")
    print("Press 4 to Edit Student")
    print("Press 5 to print all Student")
    print("Press 6 to Exit")
    option=input("Enter choice ")
    if option=='6':
        break
    elif option=='1':
        student={}
        student["Name"]=input("S1tudent Name: ")
        student["Father Name"]=input("Student Father Name: ")
        student["Age"]=input("Student Age: ")
        student["Contact#"]=input("Student Contact#: ")
        students.append(student)
        continue
    elif option=='5':
        for a in students:
            print(a)
        continue
    elif option=='2':
        name=input("Enter name to delete the record ")
        ind=0
        if name==student["Name"]:
            del students[student[ind]]
            break
        ind+=1
        continue
    '''

''''list1=[
    {
        "Name":"Huzaifa" 
    },
    {
        "Name":"hammad"
    },
    {
        "Name":"Ahmed"    
    }
]
print(list1[2])

dict1={
    "Name":"Jawed",

    "Status":"Married",
    "Child":{"1Name":"Huzaifa","2Name":"Hamza"}
}
x=int(input("which one "))
print(dict1["Child"][str(x)+"Name"])
'''
dict={"1":"Sir Inam","2":"hamza","3":"hammad"}
print(dict["1"])
dict["4"]="nehal"
print(dict["4"])
print(dict)
for x in dict.keys():
    print(x)
for x in dict.values():
    print(x)
dict["1"]="Sir Huzaifa"
for x,y in dict.items():
    print(f"{x} is  {y}")
lst_dict=[{"1":"Sir Inam","2":"hamza","3":"hammad"},{"4":"Sir Inam","5":"hamza","6":"huzaifa"}]
print(lst_dict[1]["6"])
print(len(lst_dict))