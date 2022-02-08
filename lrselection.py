# Operators and Boolean Logic

var1 = 5
var2 = int(input("NUMIN: "))
var3 = [1,2,3,4,5,6]


if 10%var2 != 0 or (var2 >= 5 and var2 in var3):
    print("This is the True Code Path")
else:
    print("This is the False Code Path")

print("This line isn't indented and will always run")

# If and Elif

var1 = 5
var2 = int(input("NUMIN: "))
var3 = [1,2,3,4,5,6]

if var2 > var1:
    print(var2, "is bigger than 5")
elif var2 > 0:
    print(var2, "is a positive number")
elif var2 < 0:
    print(var2, "is a negative number")
else:
    print(var2, "is 0" )


# string method tests

var2 = input("TYPE!: ")

if var2.isalnum():
    print("is a letter or a number")
else:
    print("is a symbol")


# Nested if

var2 = input("type")

if var2.isnumeric():
    if float(var2) > 0:
        print(var2 + " is a positive number")
    else:
        print(var2 + " is a negative number")
else:
    print(var2 + " is not a number")
