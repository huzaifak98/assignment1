class Patient():
    def __init__(self , name , age , cnic,fname="not specified"):
        print("I am a constructor")
        self.name=name
        self.age=age
        self.cnic=cnic
        self.fname=fname
        self.__height="5.6"
    
    def info(self):
        print(f'My name is {self.name} and age is {self.age}')
        self.age=22
        print(self.age)
        
    def change_age(self, ageadd):
        self.age+=ageadd
    
    def retrn(self,name):
        self.name=name
        return self.name

obj1=Patient("Huzaifa",21,4210110420011)
obj2=Patient("Hammad",20,4210110420011,"shams")
obj2.info()
obj2.change_age(2)
print(obj1.retrn("Ahmed"))
