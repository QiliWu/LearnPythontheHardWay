# Animal is-a object
class Animal(object):
    pass

# class Dog has a __init__which takes self and name parameters
class Dog(Animal):

    def __init__(self,name):
        # from self get the name attribute and set it to name.
        self.name = name

# class Cat has a __init__ that takes self and name parameters
class Cat(Animal):

    def __init__(self,name):
        #from self get name attribute and set it to name
        self.name = name

# class Person has a __init__ that takes self and name parameters
class Person(object):

    def __init__(self,name):
        # from self get name attribute and set it to name
        self.name = name

        # Person has-a pet of some kind
        self.pet = None

# Employee is person. class employee has a __init__ that takes self,name,salary parameters.
class Employee(Person):

    def __init__(self,name,salary):
        #from Employee's parent class get __init__function and call it with parameters self, name
        super(Employee, self).__init__(name)
        #from self get salary attribute and set it to salary
        self.salary = salary

# fish is object
class Fish(object):
    pass

# salmon is Fish
class Salmon(Fish):
    pass

# Halibut is fish
class Halibut(Fish):
    pass


# rover is a dog
rover = Dog("Rover")

# satan is a cat
satan = Cat("Satan")

# mary is a person
mary = Person("Mary")

#from mary get the pet attribute and set it to satan
mary.pet = satan

#set frank to an instance of class employee
frank = Employee("Frank", 120000)

# from frank get pet attribute and set it to rover
frank.pet = rover

# set flipper to an instance of class fish
flipper = Fish()

# set course to an instance of class salmon
course = Salmon()

# set harry to an instance of class Halibut
harry = Halibut()

