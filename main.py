#Python and Classes

#Everything in python is an object, even functions.

#a function and a metghod both execute a ablock of code
#the diferenee is thta a method belongs to an object.

#len(´test´) - function
#´test´.upper() - method

#test = ´a´
#print(dir(test))

#def test():
  #pass

#a = test()
#print(dir(a))

'''
def add(a,b):
  return a + b

class Test:
  def __init__(self,add_function): #this is being called and passed through
    self.add_function = add_function
test = Test(add_function = add)
print(test.add_function(10,65)) # a + b passed
'''

#Pratice

class Monster:
  def __init__(self,func):
    self.func = func

class Attacks:

  def bite(selfe):
        print("The monster bit you!")
    
  def strike(self, strike):
        print("The monster struck you!" )
      
  def slash(self, slash):
        print("The monster sliced your face in half!")
    
  def kick (self,kick):
        print("The monster kicked you!" )
      
monster = Monster(func = Attacks().bite) #make Attacks into an object by adding brackets, so python doesnt get confused returning a class.

 # OR
attacks = Attacks()
monster = Monster(func = attacks.bite)
monster.func()

  


'''
mo = Monster() #Classes are usually written in CamelCase, variables are usually written in snake_case
print(monster.health)
print(monster.energy)
monster.attack(999)
monster.attack(99)
'''
