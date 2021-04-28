#!/bin/python3

import math
import os
import random
import re
import sys
import operator



if __name__ == '__main__':
    s = input()

    diction = {}
    
    mylist = list(s)
    dictlist = []
    
    #converting into dictionary
    
    for character in mylist:
        if character not in diction:
            diction[character] = 1
        else:
            diction[character] = diction[character] + 1
        
   #converting to list         
    
    for key, value in diction.items():
        temp = [key , value]
        dictlist.append(temp)
    
    
    records = dictlist
    
    #sort by occuerences and if occurences are same then sort by alphabet
    
    for i in range(len(records)):
        for j in range(i , len(records)):
           if(records[i][1] < records[j][1]):
                temp = records[i]
                records[i] = records[j]
                records[j] = temp
                
           if(records[i][1] == records[j][1]):
                if(records[i][0] > records[j][0]):
                    temp = records[i]
                    records[i] = records[j]
                    records[j] = temp   
    
    
    for i in range(3):
        print(records[i][0] , records[i][1])