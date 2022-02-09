def gradeing(inputvar):
    if var1 > 85:
        return "A"
    elif var1 > 65:
        return "B"
    else:
        return "F"



var1 = 2
gradevar = gradeing(var1)

# print a certificate

print("================")
print("  You got an:   ")
print("       "+ gradevar + "   "  )
print("================")