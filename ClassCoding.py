from multiprocessing import AuthenticationError
from unicodedata import name


class Animal:
    
    """Animal Class"""

    def __init__(self, name, age):
        print("Initializing an animal")
        self.name = name
        self.age = age


    #properties    

    @property
    def name(self):
        return self.__name
     
    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, new_age):
        self.__age = new_age

    #behaviors
    def move():
        print("Animal is moving")
    
    def eat():
        print("Animal is eating")
    

class Book:
    
    """Book Class"""
    
    def __init__(self, title, author, isbn):
        print("Initializing a Book")
        self.title = title
        self.author = author 
        self.isbn = isbn

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
    def read():
        print("You are reading!")


class Vehicle:

    """Vehicle Class"""

    def __init__(self, make, model, year, mpg):
        print("Initializing a Vehicle")
        self.make = make
        self.model = model
        self.year = year
        self.mpg = mpg

    #properties
    @property
    def make(self):
        return self.__make

    @make.setter
    def make(self, newMake):
        self.__make = newMake


    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, newModel):
        self.__model = newModel

    @property
    def year(self):
        return self.__year

    @year.setter
    def setter(self,newYear):
        self.__year = newYear


    @property
    def mpg(self):
        return self.__mpg

    @mpg.setter
    def setter(self, newMPG):
        self.__mpg = newMPG

    #behaviors
    def drive():
        print("Car is driving")

    def brake():
        print("Car is braking")