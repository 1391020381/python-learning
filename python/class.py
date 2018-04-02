# -*- coding:utf-8 -*-
class Student(object):

    def __init__(self,name,score):
        self.name = name
        self.score = score

    def print_score(self):
         print('%s:%s' %(self.name, self.score))   
bart = Student('Bart Simpson',59)
lisa = Student('Lisa Simpson',87)
bart.print_score()
lisa.print_score()  
class Animal(object):
    def run(self):
        print('Animal is runing.....')
class Dog(Animal):
    def run(self):
        print('Dog is running....')

    def eat(self):
        print('Eating meat ...')    
class Cat(Animal):
     def run(self):
         print('Cat is running....')  
dog = Dog()
dog.run()
cat = Cat()
cat.run()  
def run_twice(animal):
    animal.run()
    animal.run()  
run_twice(Animal())
run_twice(Dog())                  