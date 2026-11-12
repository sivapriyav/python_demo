#Destructor
#A destructor also a special method python may call when an object is about to be destroyed
#purpose- perform cleanup operations,close files or connections

class Parent:
    x=10
    def __init__(self):
        print('constructor craeted')

    def __del__(self):
        print('destructor created')

parent1 = Parent()
del parent1
print(parent1.x)