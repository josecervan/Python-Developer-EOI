import abc
from abc import ABCMeta


class Vehicle(metaclass=ABCMeta):

    @abc.abstractmethod
    def who_are_you(self):
        print("I'm a vehicle and also an abstract method")


class Car(Vehicle):

    def __init__(self):
        super().__init__()

    def who_are_you(self):
        super(Car, self).who_are_you()
        print("I'm a car")


car = Car()
car.who_are_you()