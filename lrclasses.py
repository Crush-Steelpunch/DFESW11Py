# Classes

import pdb

class Lettertest:


    def __init__(self,invar="AEIOU"):
        self.letterlist = invar

    def lettertest(self,invar):
        if invar.upper() in self.letterlist:
            return True
        else:
            return False








vowls = Lettertest()

print(vowls.letterlist)
print(getattr(vowls, letterlist))
print(vowls.lettertest("p"))

vertsym = Lettertest("AHIMOTUVWXY")
print(vertsym.letterlist)
print(vertsym.lettertest("p"))







# - attributes, Variables or Collections
# - methods, Procedures / Functions

# Procedure or Fuction
def somename():
    pass # code here

# Variable
var1 = "data"
list1 = [1,2,True]

