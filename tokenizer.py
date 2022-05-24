import re

def checkidentifier(str):
    if str[0].isdigit():
        return False
    # pattern = re.compile("[A-Za-z0-9]+")
    if re.match("^[A-Za-z0-9_]+$", str) and str[0] != "^[0-9]":
        return True
    else:
        return False
    
def checkequalsign(str):
    if str == '=':
        return True
    else:
        return False
    
def checknumber(str):
    numstr = str[:-1]
    semicolon = str[-1:]
    # if more than 1 digit of number and if the first digit is 0
    if len(numstr) > 1 :
        if numstr[0] == "0":
            return False 
    if re.match("^[0-9]+$", numstr) and semicolon == ";":
        return True
    else:
        return False
    
def checkexpression(str, dict):
    numstr = str[:-1]
    semicolon = str[-1:]
    if len(numstr) > 1 :
        if numstr[0] == "0":
            return False 
    if semicolon == ";":
        for i in numstr:
            if checkstatus(i,dict) == False:
                return False
        return True
                    

def checkstatus(i,dict):
    for key in dict:
        if i == "^[0-9]" or i == key or i == "+" or i == "-" or i == "/" or i == "*" or i == "(" or i == ")":
           return True
    return False
    
def checkeachline(str,dict):
    parts = []
    parts = str.split(' ')
    if checkidentifier(parts[0]) and checkequalsign(parts[1]) and checknumber(parts[2]):
        return True
    elif checkidentifier(parts[0]) and checkequalsign(parts[1]) and checkexpression(parts[2],dict):
        return True
    else: 
        return False
    
def tokenize(str):
    lines = []
    lines = str.split('\n')
    dict = {}
    parts = []
    status = True
    for line in lines:
        parts = line.split(' ')
        if checkeachline(line,dict):
            dict[parts[0]] = parts[2][:-1]
        else:
            print("error")
            status = False
            break
            
    if status == True:
        for key in dict:
            for key2 in dict:
                if dict[key2] == key:
                    dict[key2] = dict[key]
        for key in dict:
            print(key+" = "+dict[key])
    
    
    
    
    
# infile = open()
# infile.read()

# must separated by \n
tokenize("x = 0;\ny = x;\nz = x+y;")