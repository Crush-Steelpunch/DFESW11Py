import random

def gradeing(inputvar):
    if inputvar > 85:
        return ["A","Distinction"]
    elif inputvar > 65:
        return ["B", "Pass"]
    else:
        return ["F","What a thicko"]


def maxthreenumbers(in1,in2,in3):
    if in1 > in2:
        if in1 > in3:
            return in1
        else:
            return in3
    else:
        if in2 > in3:
            return in2
        else:
            return in3

def reverseastring(in1):
    lenin = len(in1)-1
    outvar = ''
    while lenin > -1:
        outvar = outvar + in1[lenin]
        lenin = lenin - 1
    return outvar

def testisprime(in1):
    counter = 2
    moduloresult = 1
    while moduloresult != 0:
        counter += 1
        moduloresult = in1%counter
    if counter == in1:
        return True
    else:
        return False

def testispalindrome(in1):
    revword = reverseastring(in1)
    if revword == in1:
        return True
    else:
        return False

def pascalstriangle(in1):
    rowa = [1]
    rowb = [1,1]
    stagelist = []
    returnstr = str(rowa) + "\n"
    returnstr = returnstr + str(rowb) + "\n"
    for i in range(in1):
        rowlen = len(rowb)-1
        rowa = [1]
        for i in range(rowlen):
            tmpa = rowb[i]
            if i + 1 > rowlen:
                break
            tmpb = rowb[i+1]
            tmpc = tmpa + tmpb
            rowa.append(tmpc)
        rowa.append(1)
        returnstr = returnstr + str(rowa) + "\n"
        rowb = rowa
    return returnstr

def isperfectnum(in1):
    divisorlist = []
    testsum = 0
    for i in range(1,in1):
        moduloresult = 1
        testdivisor = in1%i
        if testdivisor == 0:
            divisorlist.append(i)
    for i in divisorlist:
        testsum = testsum + i
    if testsum == in1:
        testother = testsum + in1
        if testother / 2 == in1:
            return True
        else:
            return False
    else:
        return False


def len():
    return "Hi, I am Len!"

def guessnum():
    guessvar = random.randint(1, 9)
    return guessvar
