def gradeing(inputvar):
    if var1 > 85:
        return ["A","Distinction"]
    elif var1 > 65:
        return ["B", "Pass"]
    else:
        return ["F","What a thicko"]



var1 = 2
gradevar = gradeing(var1)

# print a certificate

print("================")
print("  You got an:   ")
print("       "+ gradevar[0] + "   "  )
print("       "+ gradevar[1] + "   "  )
print("================")