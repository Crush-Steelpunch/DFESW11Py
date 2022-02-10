import pdb

# pdb.set_trace()

class Category:

    # we need a balance attribute
    def __init__(self,balance=0):
        self.balance = balance
    

    # we need a deposit function
    def deposit(self, amount):
        self.balance = self.balance + amount

    # we need a withdrawl function
    def withdrawl(self, amount):
        self.balance = self.balance - amount

    # we need a transfer function
    # where from <- the balance of the other catagory object
    # where to <- The object that this method is called from
    # Amount
    def transfer(self,amount,fromcatagory):
        self.deposit(amount)
        fromcatagory.withdrawl(amount)
        

food = Category(0)
clothes = Category(15)
entertainment = Category(12)
pdb.set_trace()
print('#Food Account')
print(food.balance)
food.deposit(15)
print(food.balance)

food.transfer(15, clothes)

print(food.balance)


#food.transfer()
print(clothes.balance)
clothes.deposit(60)
print(clothes.balance)
clothes.withdrawl(12)
print(clothes.balance)
