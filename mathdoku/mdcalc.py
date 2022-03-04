#!/usr/bin/env python

demenition = 7
finalvol = 19
quantity = 4
operand = "+"
intersection = 2
expt_list = []

def generator (q=3,d=5):
    result =[]
    for j in range(q):
        result.append(d)

    for i in range(d**q):
        print(result)
        for j in range(q):
            result[j] -= 1
            if result[j] > 0:
                break
            result[j] = d

def operation (oper, args, rslt):
    if oper == "+":
            tres = 0
    if oper == "*":
            tres = 1
    
    for x in args:
        if oper == "+":
            tres += x
        if oper == "*":
            tres *= x
    
    if tres == rslt:
        return True
    else:
        return False

def mdcalc (d,f,q,op):
    result =[]
    gres = []
    for j in range(q):
        result.append(d)
    for i in range(d**q):
        if operation(op,result,f):
            tres = result.copy()
            tres.sort()
            gres.append(tres)
        for j in range(q):
            result[j] -= 1
            if result[j] > 0:
                break
            result[j] = d

    return [list(tupl) for tupl in {tuple(item) for item in gres }]

sorted_result = mdcalc(demenition,finalvol,quantity,operand)

# Intersection checking
for item in sorted_result:
    cstop = True
    csum = 0
    for i in range(1,demenition+1):
        ic = item.count(i)
        if ic > intersection:
            cstop = False
        if ic > 1 and ic <= intersection:
            csum += ic
    if csum > intersection:
        cstop = False
    for i in expt_list:
        for j in item:
            if i == j :
                cstop = False
    if cstop:
        print(item)

# print(sorted_result)
