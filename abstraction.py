from abc import ABC,abstractmethod
class Animal(ABC):
    @abstractmethod
    def move(self):
        pass
    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def move(self):
        print('Dog is walking')
    def speak(self):
        print('Dog is Barking(bho bho bhobhobho)')

class Horse(Animal):
    def move(self):
        print('Horse is Runing')
    def speak(self):
        print('Horse is hihihihihi')

d=Dog()
d.move()
d.speak()
h=Horse()
h.move()
h.speak()