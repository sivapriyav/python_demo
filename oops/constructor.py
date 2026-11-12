'''Constructor is a special method that is automatically created or invoked
when an object is created.
Purpose
1.Initialise object attributes
2.Assign initial value to variable
3.Perform invocation
'''


class Parent:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        print('Constructor created')

    def display(self):
        print(self.name,self.age)
        print("Parent display")


p1 = Parent('Reshma',20)#when an aobject is created automatically a constructor is created

p1.display()#constructor is invoked without explicit creation

p2 = Parent('Reshma',30)
p2.display()
