#Its a programming approach in which we organise our code using classes and objects

#Realworld example-
#A car category has properties(brand,color,model,speed) and behaviors(start,stop,accelerate,break)
#Each car object under the category can have its own properties and behaviors(objects:swift,bmw)
#In real oops programming properties are represented using attributes
#Behaviours are represented using methods(functions inside oops class)

#objects are instances of class

#class is the blueprint of object

#Terms in OOPS-class,objects,attributes,methods

#Advantages:
#1. Code reusablity,
#2. code maintainability,
#3. encapsulating data and methods
#4. organising entire code script

class CarClass:
    color = 'Black'
    model = 'electric'

    def start(self): #self refers to the current object using which we import the method
        print('Engine started')

    def stop(self,distance):
        self.distance = distance #instance variable is created used in other methods inside class.can be used anywhere inside class
        print(f"car stopped at {distance}")

    def detail(self):
        print(f"car started and stopped at {self.distance}km")


car1 = CarClass()#Creating objects
# print(color)#cannot access variables inside class directly
print(car1.color)

car2 = CarClass()
print(car2.model)

car1.speed = '100kmph'
print(car1.speed)

car1.start()
car2.start()

car1.stop(20)
car2.stop(50)

car1.detail()
car2.detail()

#in this case value 10 is reused inside detail method this is possible bcs both stop and detail are invoked using car1





