# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 13:01:00 2022

@author: weron
"""

from math import ceil, floor
from random import uniform


def foo(x):
    return x

# pierwiastek z podanej liczby
def root_round_4(number):
    """root of a number based on 2 with the rounding to 4 numbers"""
    a=1
    b=number
    isStabilesed = False
    while not isStabilesed:
        mean = round((a+b)/2,4)
        if mean == a:
            return a
        else:
            a = mean
            b = round(number/a,4)

def root(number):
    """root of a number based on 2 without the rounding"""
    try:
        a=1
        b=number
        while True:
            mean = (a+b)/2
            if mean == a:
                return a
            else:
                a = mean
                b = number/a
    except ZeroDivisionError:
        print("Can not divide by 0")
        return -1

# print(root(5))

# pd -calkowanie metoda montekarlo dla funkcji dowolnej
def funcIn(x, y,function):
    if y > 0 and y <= function(x):
        return 1
    elif y < 0 and y >= function(x):
        return -1
    return 0

def randomPoint(a,b):
    return uniform(a, b)

def monteCarloForIntegralFunction(xp, xk, func, numberOfPoints=100):
    integral:float 
    n:int
    pointsIn = 0
    
    numberOfPoints *=100
    yp = floor(min(func(xp),func(xk)))
    yk = ceil(max(func(xp),func(xk)))
    
    for i in range(numberOfPoints):
        pointsIn += funcIn(randomPoint(xp, xk),randomPoint(yp, yk),func)
        
    integral = pointsIn/numberOfPoints*(xk-xp)*(yk-yp)
    return integral

def monteCarloForIntegralFunction2(xp, xk, func):
    frequency=100
    pointsIn = 0

    yp = 0
    yk = ceil(max(func(xp),func(xk)))
    rectangleArea = (xk-xp)*(yk-yp)
    
    for i in range(frequency):
        pointsIn += funcIn(randomPoint(xp, xk),randomPoint(yp, yk),func)
        
    integral = round(pointsIn/frequency*rectangleArea,6)
    while True:
        for i in range(frequency,frequency+10):
            pointsIn += funcIn(randomPoint(xp, xk),randomPoint(yp, yk),func)
        if round(pointsIn/frequency*rectangleArea,6) == integral:
            return integral, frequency
        else:
            integral = round(pointsIn/frequency*rectangleArea,6)
            frequency+=10
            
            
print(monteCarloForIntegralFunction(0, 1, foo, 10000))
print(monteCarloForIntegralFunction2(0, 1, foo))

# dla funkcji 2 podajemy epsilon jako punkt ktory ma osiagnac zeby program sie skonczyl
# zabrac od kogos polecenei do calkowani
# potem jakies porownywanie dla np 30 podzialow i 40 jak dosc mala roznica 
# program stop jak nie to dalej dla 40 i 50 podzialow np
 
def epsilonForIntegralFunction(epsilon, a, b, func):
    frequency = 10
    tmp = 0
    
    while True:
        dx  = (b-a)/frequency
        integral = 0
        for i in range(frequency):
            heightA = a + dx * i
            heightB = a + dx * (i + 1)

            integral += (func(heightA) + func(heightB)) / 2 * dx
        if abs(integral-tmp) <= epsilon:
            return integral
        else:
            tmp = integral
            frequency+=1
        
 
integral = epsilonForIntegralFunction(0.00000000001, 0, 1, foo)
print(integral)
