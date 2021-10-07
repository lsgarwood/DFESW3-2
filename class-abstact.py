from abc import ABC, abstractmethod

class Bird(ABC):
    fly = True
    babies = 0

    def noise(self):
        return "Squawk"

    def reproduce(self):
        self.babies += 1

    @abstractmethod
    def eat(self):
        pass

    extinct = False

class Owl(Bird):

    def reproduce(self):
        self.babies += 6
        return self.babies

    def eat(self):
        return "Peck peck"

class Dodo(Bird):
    fly = False
    extinct = True
    babies = 0

    def eat(self):
        return "Nom nom"

    def reproduce(self):
        if not self.extinct:
            self.babies += 1
            return self.babies

class Budgie(Bird):
    babies = 0

    def fly(self):
        return 'too lazy to fly!'

    def eat(self):
        return 'gobble gobble'
    
    def noise(self):
        return 'trill trill'

reddodo = Dodo()
bluedodo = Dodo()
greyowl = Owl()
brownowl = Owl()
smudgiebudgie = Budgie()
bobbudgie = Budgie()

print(reddodo.noise())
print(bluedodo.reproduce())
print(greyowl.reproduce())
print(brownowl.eat())
print(smudgiebudgie.eat())
print(bobbudgie.fly())




