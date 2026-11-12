#Its the concept in which 1 class acquires the properties and methods of another class.
#The first class is known as- parent,base,super
#second class is known as - base,child,inherited class
#A child class can reuse the code of a parent class without writing it again

class parent:
    networth = '10 cr'

    def skill(self):
        print("Teaching skill")

class child(parent):

    def job(self,jobtitle):
        print('My job is '+jobtitle)


child1 = child()
child1.skill()
print(child1.networth)
child1.job('HR')

#Types of inheritance

'''
1.Single inheritance-one parent-one child
2.Multiple inheritance-multiple parent-one child
3.Multilevel inheritance-A child class becomes a parent class for another class
4.Hierarchial inheritance-single parent-different child
5.Hybrid inheritance-combination of 2 or more types of inheritance
'''

#Multiple inheritance

class A:
    pass

class B:
    pass

class C(A,B):
    pass

c1 = C()

#Multilevel inheritance

class A:
    pass

class B(A):
    pass

class C(B):
    pass

c1 = C()

#Hierarchial inheritance

class Parent:
    def display(self):
        print("Parent display")

class Child1(Parent):
    pass

class Child2(Parent):
    pass


c1 = Child1()
c2 = Child2()

c1.display()
c2.display()








