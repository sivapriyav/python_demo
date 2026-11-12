#Polymorphism means one name with many forms
#It allows same method name(function) or operator to be behave differently depending on the object.
#The builtin polymorphic operator in python is '+' (for numbers it perform addition and for string it perform concatenation)

class Parent:
    def skill(self):
        print("Teaching skill")

class Child1(Parent):

    def skill(self):
        super().skill()
        print("singing")

class Child2(Parent):
    def skill(self):
        print("Dancing")
        super().skill()

c1 = Child1()
# c1.skill()

c2 = Child2()
c2.skill()

#In python the type of polymormphism it supports is method overriding.
# Its the scenario in which same method is defined(with a different performance) in both parent and child classes(using inheritance)


#Method overloading
#Same method is used more than once in a class.There is no inheritance in this case.Not supported in python.Only the final method is considered

class Parent:

    def addition(self,a,b):
        print("Addition of numbers")

    def addition(self,a,b):
        print(a+b)

p1 = Parent()
p1.addition(5,4)
p1.addition(2,3)