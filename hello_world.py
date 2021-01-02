# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 19:42:33 2020

@author: sagni
"""


h=""
for Row in range(0,7):    
    for Col in range(0,7):     
        if (Col == 1 or Col == 5) or (Row == 3 and Col > 1 and Col < 6):  
            h=h+"*"    
        else:      
            h=h+" "    
    h=h+"\n"    
print(h)

e=""
for row in range(0,7):    
    for column in range(0,7):     
        if (column == 1 or ((row == 0 or row == 6) and (column > 1 and column < 6)) or (row == 3 and column > 1 and column < 5)):  
            e=e+"*"    
        else:      
            e=e+" "    
    e=e+"\n"    
print(e)

l=""    
for row in range(0,7):    
    for column in range(0,7):     
        if (column == 1 or (row == 6 and column != 0 and column < 6)):  
            l=l+"*"    
        else:      
            l=l+" "    
    l=l+"\n"    
print(l)
l=""    
for row in range(0,7):    
    for column in range(0,7):     
        if (column == 1 or (row == 6 and column != 0 and column < 6)):  
            l=l+"*"    
        else:      
            l=l+" "    
    l=l+"\n"    
print(l)

o="";    
for row in range(0,7):    
    for column in range(0,7):     
        if ((column == 1 or column == 5) and row != 0 and row != 6) or ((row == 0 or row == 6) and column > 1 and column < 5):  
            o=o+"*"    
        else:      
            o=o+" "    
    o=o+"\n"    
print(o);
print("\n \n \n")

w=""
for row in range(0,7):    
    for column in range(0,7):  
        if ((column == 1 or column == 5) and row < 6) or ((row == 5 or row == 4) and   column == 3) or (row == 6 and (column == 2 or column == 4)):
            w=w+"*";
        else:
            w=w+" "
    w=w+"\n"
print(w)

o="";    
for row in range(0,7):    
    for column in range(0,7):     
        if ((column == 1 or column == 5) and row != 0 and row != 6) or ((row == 0 or row == 6) and column > 1 and column < 5):  
            o=o+"*"    
        else:      
            o=o+" "    
    o=o+"\n"    
print(o);

r="";    
for row in range(0,7):    
    for column in range(0,7):     
        if (column == 1 or ((row == 0 or row == 3) and column > 1 and column < 5) or (column == 5 and row != 0 and row < 3) or (column == row - 1 and row > 2)):  
           r=r+"*"    
        else:      
            r=r+" "    
    r=r+"\n"    
print(r);

l=""    
for row in range(0,7):    
    for column in range(0,7):     
        if (column == 1 or (row == 6 and column != 0 and column < 6)):  
            l=l+"*"    
        else:      
            l=l+" "    
    l=l+"\n"    
print(l)

d="";    
for row in range(0,7):    
    for column in range(0,7):     
        if (column == 1 or ((row == 0 or row == 6) and (column > 1 and column < 5)) or (column == 5 and row != 0 and row != 6)):  
            d=d+"*"    
        else:      
            d=d+" "    
    d=d+"\n"    
print(d);
            
            
