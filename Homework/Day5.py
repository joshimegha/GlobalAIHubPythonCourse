class Animal:
    def __init__(self, type='Animal', legNumber=0):
        self.type = type
        self.legNumber = legNumber

    def setLeg(self, legNumber):
        self.legNumber = legNumber
    def getLeg(self):
        return self.legNumber

    def describe(self):
       print( "%s has %d legs, and it is a pet animal." %(self.type, self.legNumber) )

class Dogs(Animal):
    def makeSound(self):
        print("Dog make sounds like Bow! Bow! Bow!")

class Cats(Animal):
  def makeSound(self):
    print("Cat make sounds like Meow! Meow! Meow!")


dog1 = Dogs()    
print( dog1.legNumber )   
dog1.setLeg(2)    
print( dog1.legNumber )  

dog2 = Dogs('Dog', 4)  
dog2.describe()   
dog2.makeSound()


cat1 = Cats()    
print( cat1.legNumber )   
cat1.setLeg(2)    
print( cat1.legNumber )  

cat2 = Cats('Cat', 4)  
cat2.describe()   
cat2.makeSound()

