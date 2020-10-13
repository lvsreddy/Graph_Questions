# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 12:13:50 2020

@author: Sudharshan.Reddy
"""

#https://www.geeksforgeeks.org/stepping-numbers/


def steppingNumUtil(m, n, stepnum):
    
    #If Stepping Number is in the range [m,n] then print
    if stepnum <= n and stepnum >= m:
        print(stepnum, end = ' ')
   
    #If Stepping Number is 0 or greater than m, then return    
    if stepnum == 0 or stepnum > n:
        return;
        
        
    #Get the last digit of the currently visited Stepping Number   
    
    lastdigit = stepnum % 10
    
    #There can be 2 cases either digit to be appended is lastDigit + 1 or lastDigit - 1
    
    stepnum1 = stepnum*10 + lastdigit + 1
    stepnum2 = stepnum*10 + lastdigit - 1
    
    
    if lastdigit == 0:
        #If lastDigit is 0 then only possible digit after 0 can be 1 for a Stepping Number
        steppingNumUtil(m, n, stepnum1)
        
        
    elif lastdigit == 9:
        #If lastDigit is 9 then only possible digit after 9 can be 8 for a Stepping Number
        steppingNumUtil(m, n, stepnum2)
        
    else:
        steppingNumUtil(m, n, stepnum1)
        steppingNumUtil(m, n, stepnum2)


#Method displays all the stepping numbers in range [m, n]
def steppingNumbers(m,n):
    #For every single digit Number 'i' find all the Stepping Numbers starting with i 
    for i in range(10):
        steppingNumUtil(m,n,i)
        

m = 0
n = 21

steppingNumbers(m,n)

