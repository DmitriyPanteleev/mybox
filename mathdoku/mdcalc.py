#!/usr/bin/env python

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

def cleaning(sorted_result, ness_list, expt_list, demenition, intersection):
    # Intersection checking

    res_list = []

    for item in sorted_result:
        cstop = True
        csum = 0

        for i in expt_list:
            for j in item:
                if i == j :
                    cstop = False
        if ness_list != [] and cstop:
            for i in ness_list:
                if i in item:
                    cstop = True
                else:
                    cstop = False
                    break

        for i in range(1,demenition+1):
            ic = item.count(i)
            if ic > intersection:
                cstop = False
            if ic > 1 and ic <= intersection:
                csum += ic
        if csum > intersection:
            cstop = False

        if cstop:
            res_list.append(item)

    return res_list


if __name__ == '__main__':

    demenition = 7
    finalvol = 19
    quantity = 4
    operand = "+"
    intersection = 2
    expt_list = [2,1]
    ness_list = [5,3]
    
    sorted_result = mdcalc(demenition,finalvol,quantity,operand)

    real_result = cleaning(sorted_result,ness_list,expt_list,demenition,intersection)

    print(real_result)
