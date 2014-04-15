# Elementary Cellular Automation
# Brian Anders
# April 12, 2014

#!/usr/bin/python

circumference = 30
generations = 30
code = {}

def init():
    global circumference
    circumference = int(input('Circumference? '))
    global generations
    generations = int(input('Generations? '))
    
    for i in range(8):
        code["{0:b}".format(i)] = "0"
    rule(int(input("Which Rule? ")) % 255)
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
    

def main():
    file = open("ECA.html",'w')
    generation = init()
    file.write("<html><head><style>table{border-spacing:0;}td{width:10px;height:10px;background:whitesmoke;}td.black{background:black}</style></head><body><table>");
    
    for i in range(generations):
        file.write("<tr>" + generation.replace('0', '<td></td>').replace('1','<td class="black"></td>') + "</tr>")
        
        nextGeneration = ""
        
        for j in range(len(generation)):
            nextGeneration = nextGeneration + threeToOne(generation[(j-1) % len(generation)] + generation[j] + generation[(j+1) % len(generation)])
        
        generation = nextGeneration
    file.write("</table></body></html>")
    file.close()

        

main()
