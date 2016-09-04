#-*- coding:utf-8 -*-

class Animal(object):
    def run(self):
        print 'Animal is runnging...'

class Dog(Animal):
    pass

class Cat(Animal):
    pass

#继承
d = Dog()
d.run()
c = Cat()
c.run()

#多态(覆盖)

class Dog(Animal):
    def run(self):
        print 'Dog is runngin...'

class Cat(Animal):
    def run(self):
        print 'Cat is runngin...'
d = Dog()
d.run()
c = Cat()
c.run()

#多态的好处

def run_twice(animal):
    animal.run()
    animal.run()

run_twice(Animal())
run_twice(Dog())
run_twice(Cat())
