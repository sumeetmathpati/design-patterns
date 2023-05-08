from abc import ABC, abstractmethod


class Duck(ABC):
    
    
    # def __init__(self):
    #     quackBehaviour = None
    
    def performFly(self):
        self.flyBehaviour.fly()
    
    def performQuack(self):
        self.quackBehaviour.quack()

    # We can use these setter methods to change the behaviour anytime.

    def setFlyBehaviour(self, fb):
        self.flyBehaviour = fb
    
    def swtQuackBehaviour(self, qb):
        self.quackBehaviout = qb


class FlyBehaviour(ABC):

    @abstractmethod
    def fly():
        pass

class QuackBehaviour(ABC):
    
    @abstractmethod
    def quack():
        pass


class FlyWithWings(FlyBehaviour):
    
    def fly(self):
        print("Flying with wings")

class NoFly(FlyBehaviour):
    
    def fly(self):
        print("Can't fly")


class Quack(QuackBehaviour):
    
    def quack(self):
        print("Flying with wings")

class Squeak(QuackBehaviour):
    
    def quack(self):
        print("squeak")

class MuteQuack(QuackBehaviour):

    def quack(self):
        print("cannot quack")

class MellardDuck(Duck):

    def __init__(self):
        self.flyBehaviour = FlyWithWings()
        self.quackBehaviour = Squeak()
    

    
md = MellardDuck()
md.performFly()
md.setFlyBehaviour(NoFly())
md.performFly()