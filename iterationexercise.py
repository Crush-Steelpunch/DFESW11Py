# Write a while loop                       DONE
# which asks for the names of 5 people,
# and for each person prints their name 
# followed by the text "is awesome!"

# A) take a name, print "name is awesome" then loop
# B) take 5 names in a loop, then print all the "name is awesome"

# Answer for A

countvar = 5
while countvar > 0:
    namevar = input("TYPE NAME: ")
    print(f"{namevar} is awesome!")
    countvar = countvar - 1

# Answer for B

countvar = 5
namelist = []
while countvar > 0:
    namelist.append(input("Please add a name: "))
    countvar = countvar - 1

countvar = 0
while countvar < 5:
    print(namelist[countvar], "is awesome!")
    countvar = countvar + 1

