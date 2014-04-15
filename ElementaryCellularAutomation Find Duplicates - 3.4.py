# Elementary Cellular Automation
# Brian Anders
# April 12, 2014

## This program takes all rule in Elementary Cellular Automation and
## finds the rules that generate duplicate output. Then it prints the
## arrays of duplicate rules.

#!/usr/bin/python

circumference = 100
generations = 200
code = {}
codesToTry = [30, 54, 60, 62, 90, 94, 102, 110, 122, 126, 150, 158, 182, 188, 190, 220, 222, 250]
codeObject = {}
duplicates = {}

def init(c):
    for i in range(8):
        code["{0:b}".format(i)] = "0"
    rule(c)
    string = ""
    for i in range(circumference):
        if(i == circumference//2):
            string = string + "1"
        else:
            string = string + "0"
    return string

def threeToOne(three):
    return code[str(int(three))]

def rule(rule):
    rule = "{0:b}".format(rule)
    while len(rule) < 8:
        rule = "0" + rule
    for i in range(7,-1,-1):
        code["{0:b}".format(i)] = rule[7-i]
    

def main(r):
    generation = init(r)
    theCode = ""
    
    for i in range(generations):
        theCode = theCode + generation
        
        nextGeneration = ""
        
        for j in range(len(generation)):
            nextGeneration = nextGeneration + threeToOne(generation[(j-1) % len(generation)] + generation[j] + generation[(j+1) % len(generation)])
        
        generation = nextGeneration
    theCode = theCode + generation

    global codeObject
    try:
      codeObject[theCode]
    except KeyError:
      codeObject[theCode] = [r]
    else:
      codeObject[theCode].append(r)
    



        
for r in range(256):
    main(r)


print("these are the sets of duplicate rules")
for c in codeObject:
    if(len(codeObject[c]) > 1):
        print(codeObject[c])

