# while loop

# create a var to test
# test the var
# change the var in the loop

countvar1 = 6
while countvar1 > 0:
    print("===============")
    # print(countvar1)
    countvar1 = countvar1 - 1

print("====WELCOME====")

# # uses a list
# # takes items out of the list one at a time 
# # that you can use in the loop

for actionvar1 in (1,2,3,4,5,6):
    # print(actionvar1)
    print("===============")

# using range()

for i in range(16,5,-1):
    print(i)

# strings are iterable!

for loopvar1 in "thisisalotofletter":
    if loopvar1 in "aeiou":
        print(loopvar1 + " is a vowel")
    else:
        print(loopvar1 + " is a consonant")

# Break or Continue

for loopvar1 in "thisisalotofletter":
    if loopvar1 == "l":
        continue  # break
    print(loopvar1)
    
# loops and dicts


listvar3 = {"cow" : "moo", "sheep" : "baa"}

for i in listvar3.keys():
    print(listvar3[i])