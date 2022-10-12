# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 14:13:14 2021
Collatz Conjecture
@author: Christopher
"""
#In simple terms, the Collatz Conjecture states that if you take any positive integer and split it in half it is even, or triple it and add one if it is odd, and then iterate over that process, you will always end up at 1 and then an infinite loop of 4,2,1
#Calculates output values of the Collatz Conjecture when applied to any positive integer, but stops after reaching one rather than getting stuck in an infinite loop.
#This script calulaates the values between any positive integer input and 1.
#This script was made just for fun.

#Learn more about the conjecture here: https://www.quantamagazine.org/why-mathematicians-still-cant-solve-the-collatz-conjecture-20200922/


def collatz(num):
    if num % 2 == 0:
        num = num/2
    else:
        num = (3*num) + 1       
    return(num)


def calc(start):
    value = int(start)
    list=[value]
    while value > 1:
        value = int(collatz(value))
        list.append(value)
    return(list)


print(calc(int(input("Enter a starting value for the Collatz Conjecture."))))
