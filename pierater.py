import pdb
from lrfunctions import gradeing
from lrfunctions import maxthreenumbers
from lrfunctions import len as hilen

pdb.set_trace()

# import filename
var1 = int(input("Rate the pie out of 100: "))
returnval = gradeing(var1)
print(returnval)

for i in range(4):
    print(i)

print(len("aeiou"))

print(hilen())


# filename.function(_)