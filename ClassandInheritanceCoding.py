from multiprocessing import AuthenticationError
from unicodedata import name


class Animal:
    
    """Animal Class"""

    def __init__(self, name):
        print("Initializing an animal")
        self.name = name

    #properties    

    @property
    def name(self):
        return self.__name
     
    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @property
    def age(self):
        print("getting age")
        return self.__age
    
    @age.setter
    def age(self, new_age):
        self.__age = new_age

    #behaviors
    def move(self):
        print("Animal is moving")
    
    def eat(self):
        print("Animal is eating")
    
#Animal Subclasses
class Fish(Animal):

    """Fish class, inheriting from Animal"""

    def __init__(self,name):
        print("this is a fish")
        super().__init__(name)

    
    #behavoir
    def bite(self):
        print("fish is biting")

class Snake(Animal):

    def __init__(self,name):
        print("This is a Snake")
        super().__init__(name)

    def hiss(self):
        print("Snake is hissing")
    
    def rattle(self):
        print("snake is rattling")

class person(Animal):

    def __init__(self, name):
        print("This is a person")
        super().__init__(name)

    def speak(self):
        print("person is speaking")


class Book:
    
    """Book Class"""
    
    def __init__(self, title, author):
        print("Initializing a Book")
        self.title = title
        self.author = author 
        

    #properties

    @property
    def title(self):
        return self.__title
    
    @title.setter
    def title(self, newTitle):
        self.__title = newTitle

    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, newAuthor):
        self.__author = newAuthor
    
    @property
    def isbn (self):
        return self.__isbn

    @isbn.setter
    def isbn(self, newISBN):
        self.__isbn = newISBN


    #behaviors
    def read(self):
        print("You are reading!")


class Textbook(Book):

    def __init__(self, title, author):
        super().__init__(title, author)
        print("This is a text book")


    def read(self):
        print("textbook is being read")

    def sleepon(self):
        print("textbook is being used as a pillow")

class AdressBook(Book):
        
    def __init__(self, title, author):
        super().__init__(title, author)
        print("This is an adressbook")

    def lookup(self):
        print("Looking something up in the adressbook")



class Vehicle:

    def __init__(self, type, year, mpg):
        print("Initializing a Vehicle")
        self. type = type
        self.year = year
        self.mpg = mpg 

    #properties
    
    @property
    def type(self):
        return self.__type
    
    @type.setter
    def type(self, newType):
        self.__type = newType

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, newYear):
        self.__year = newYear

    @property 
    def mpg(self):
        return self.__mpg

    @mpg.setter
    def mpg(self, newMPG):
        self.__mpg = newMPG


    #behabiors

    def drive(self):
        print("Vehcile is being driven")

    def stop(self):
        print("Vehicle is stopping")

class Car(Vehicle):

    def __init__(self, type, year, mpg):
        super().__init__(type, year, mpg)

    #behavior
    def honkhorn(self):
        print("Car horn is being honked")

class Bicycke(Vehicle):

    def __init__(self, type, year, mpg):
        super().__init__(type, year, mpg)

    def changeGears(self):
        print("Bike is changing gears")

class Boat(Vehicle):

    def __init__(self, type, year, mpg):
        super().__init__(type, year, mpg)

    def horn(self):
        print("Boat horn is being honked")

class HotAirBalloon(Vehicle):

    def __init__(self, type, year, mpg):
        super().__init__(type, year, mpg)

    def ascend(self):
        print("hot airballoon is ascending")

    def descend(self):
        print("hot airballon is descending")