from abc import ABC,abstractmethod
# abc Abstract Base Class
class Animal(ABC):

    babies = 0

    def noise(self):
        return sound

    @abstractmethod
    def eat(self):
        pass





class Dog(Animal):

    def noise():
        return "woof"

    def eat(self):
        return chewing

class Cat(Animal):

    def noise():
        return "meow"

    def eat(self):
        return "yums"

Clifford = Dog()

Poppet = Cat()