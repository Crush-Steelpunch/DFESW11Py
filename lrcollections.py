# listvar1 =  ["meat", "vegetables", "cake", "beer for the weekend",4,5.5,6,True]
# #               0          1          2                3          4 5   6  7

# listvar1.append("painkillers")
# print(listvar1.count("cake"))
# print(len(listvar1))
# listvar1.insert(0, "caviar")
# print(listvar1)

# cool_cows = ["Winnie the Moo", "Moolan", "Milkshake", "Mooana"]
# cool_sheep = ["Baaaart", "Baaaarnaby"]
# cool_pigs = ["Chris P. Bacon", "Hamlet", "Hogwarts"]

# cool_animals = [cool_cows, cool_sheep, cool_pigs]
# print(cool_animals[2][0])

listvar2 =  ("meat", "vegetables", "cake", "beer for the weekend",4, 5.5,6,6,True)
#               0          1          2                3          4  5   6  7
#              -8         -7         -6               -5         -4 -3  -2 -1
print(type(listvar2))
print(listvar2[-3])


listvar3 = {"cow" : "moo", "sheep" : "baa"}
listvar3["cat"] = "meow"

print(listvar3)
print(listvar3.keys())
print(listvar3.values())