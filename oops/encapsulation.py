'''Encapsulation is the process of combining data(variables) and methods(functions) into a single unit called a class
 and while controlling access to the data'''

'''Python has 3 common access levels(access modifiers)'''
#public(name = 'Sachin')-can be accessed normally
#protected(_name = 'Sachin')-intended for internal or sub class uses
#private(__name = 'Sachin')-can be accessed only using base class objects

#eg for private variable-password
#eg for private method- balance enquiry using atm card

class Employee:

    def __init__(self,name,salary,password):
        self.name = name #public variable
        self._salary = salary #protected variable
        self.__password = password #private variable


    def display_name(self):
            print(f"Employee name is {self.name}")

    def _display_salary(self):
        print(f"Salary is {self._salary}")

    def __display_password(self):
        print(f"password is: {self.__password}")

    def show_details(self):
        self.__display_password()





e1 = Employee('Siva',40000,'abc1234')

#Accessing public variable and method

print(e1.name)
e1.display_name()

#Accessing protected variable and method

print(e1._salary)
e1._display_salary()

#Accessing private variable and method(By creating another public method inside the class and calling the private variable in the public method)
#e1.__display_password()#cannot access private variable and method directly
e1.show_details()


#Getter and setter methods

#getter method is used to retrieve the value of a private variable
#setter method is used to modify the value of a private variable usually with validation


