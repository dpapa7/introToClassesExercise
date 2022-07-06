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
    

class Fish(Animal):

    """Fish class, inheriting from Animal"""

    def __init__(self,name,age):
        super().__init__(name)
        super().__init__(age)
    
    #behavoir
    def bite():
        print("fish is biting")

animal1 = Fish('porgy',2) 
animal1.bite()

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


# class Vehicle: