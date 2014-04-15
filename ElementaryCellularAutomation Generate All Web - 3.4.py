# Elementary Cellular Automation
# Brian Anders
# April 12, 2014

## This program takes all 256 rules in Elementary Cellular Automation and
## creates an html file with a table showing the generations created by
## each rule.

# try these rules: 30, 54, 60, 62, 90, 94, 102, 110, 122, 126, 150, 158, 182, 188, 190, 220, 222, 250 

#!/usr/bin/python

circumference = 100
generations = 200
code = {}

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
    

def main(c):
    file = open(str(c) + ".html" ,'w')
    generation = init(c)
    file.write("<html><head><style>table{border-spacing:0;}td{width:10px;height:10px;background:whitesmoke;}td.black{background:black}</style></head><body><table>");
    
    for i in range(generations):
        file.write("<tr>" + generation.replace('0', '<td></td>').replace('1','<td class="black"></td>') + "</tr>")
        
        nextGeneration = ""
        
        for j in range(len(generation)):
            nextGeneration = nextGeneration + threeToOne(generation[(j-1) % len(generation)] + generation[j] + generation[(j+1) % len(generation)])
        
        generation = nextGeneration
    file.write("</table></body></html>")
    file.close()

        
for c in range(256):
    main(c)
