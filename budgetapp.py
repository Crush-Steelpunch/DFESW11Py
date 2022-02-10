# Goal: “Create a Budget class  DONE 
# that can instantiate objects based on different budget categories 
# like food, clothing, and entertainment.  DONE
# These objects should allow for depositing DONE
# and withdrawing  DONE
# funds from each category, - Balance attribute  DONE
# as well computing category balances and 
# transferring balance amounts between categories” DONE
# Total balance of all catagories


import pdb

class Budget:

    objcollection = []

    def __init__(self):
        self.balance = 0
        self.objcollection.append(self)

    def deposit(self,amount):
        self.balance = self.balance + amount

    def withdrawing(self,amount):
        self.balance = self.balance - amount

    def balance(self):
        return self.balance

    def transferout(self,amount, catagory):
        self.withdrawing(amount)
        catagory.deposit(amount)



food = Budget()
clothes = Budget()
entertainment = Budget()
pets = Budget()

food.deposit(100)
clothes.deposit(500)
entertainment.deposit(20)
pets.deposit(2)

food.withdrawing(3.99)
clothes.withdrawing(250)
entertainment.withdrawing(20)


for i in [food, clothes, entertainment, pets]:
    print(i.balance)

pdb.set_trace()

food.transferout(20, clothes)



# food.deposit(20)
# clothes.withdraw(50)

# food.transfer()