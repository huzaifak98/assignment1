'''def arithmetic_operations(oprn1,oprn2,oper):
    if oper=="+":
        print(oprn1+oprn2)
arithmetic_operations(2,3,"+")

def func_with_var_arg(**Ali_imran):
    print(Ali_imran)
func_with_var_arg(Name='Huzaifa')
func_with_var_arg(Name='Huzaifa',Fname='Jawed')
func_with_var_arg(Name='Huzaifa',Fname='Jawed',Age=44)
'''
def adder(*numbers):
        constant=2*9.81*3.142
        def inner():
                total=0
                for number in numbers:
                        total+=number
                print(numbers)
                print(total)
                return constant*total

        return inner
        
inner_fn=adder(1,2)
print(inner_fn())
