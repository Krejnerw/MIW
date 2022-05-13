# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 11:33:32 2022

@author: weron
"""

l1 =[1,2,3,4]
l2 = [5,6,7,8]

l1.append(l2)
l1.extend(l2)
print(l1)

sl = {"a":1,"b":2,"d":11,"c":0}
print(sl)
print(sl["a"])
print(sl.keys())
print(sl.values())
print(sorted(sl))
print(sorted(sl.values()))
print(sorted(sl.keys()))
print(sorted(sl.items(),key=lambda x: x[1])) # sort by values
print(sorted(sl.items(),key=lambda x: x)) # sort by keys
print(sorted(sl.items(),key=lambda x: x[0])) # sort by keys
print(lambda x:sl[x])

print(bool()) #F
print(bool(" ")) #T
print(bool('')) #F
print(bool(0)) #F
print(bool(1)) #T
print(bool("0")) #T
print(bool("1")) #T
print(bool([])) #F
print(bool([","])) #T

for i in range(21):
    print(i)
   
def my_split(tekst, sep):
    slowo = ""
    slowa = []
    
    for i in ala:
        if i != sep:
            slowo += i
        else:
            slowa.append(slowo)
            slowo = ""
    slowa.append(slowo)
            
    print(slowa) 
    
ala = "kot ali ma 4 nogi ale ich nie lubi"
# my_split(ala, " ")

def check_pass(tekst):
    if len(tekst) != 10:
        return False
    haslowercase = False
    for i in tekst:
        if ord(i) >=65 and ord(i) <= 90:
            haslowercase = True
            break
        # check if i.islower()
        
    hasuppercase = False
    for i in tekst:
        if ord(i) >=97 or ord(i) <= 122:
            hasuppercase=True
            break
        # check if i.isupper()
            
    isspecialchar = False
    for i in tekst:
        if i == '!':
            isspecialchar = True
            break
        # check if "!" is in tekst
        
    if isspecialchar and hasuppercase and haslowercase:
        return True
    else:
        return False

haslo = "12bdbcoiwq"
haslo2 = "12bdbcoiwA"
haslo3 = "12bd!coiwA"

# print(check_pass(haslo))
# print(check_pass(haslo2))
# print(check_pass(haslo3))

l = [1,6,9,43,2,99]
for i in l:
    if i != 99:
        print(i)

print("print ind")    
ind = 0
while(True):
    if l[ind]==99:
        print(ind)
        break
    else:
        ind+=1

with open("plik.txt", "r", encoding="utf-8") as f:
    print(f.read())

with open("plik.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line, end="")
        
f = open("plik.txt", "r", encoding="utf-8")
print(f.readlines())

l = ["python", "java","c"]

with open("plik.txt", "a", encoding="utf-8") as f:
    f.write("\n")
    for i in l:
        f.write(i+"\n")

import sys

original_stdout = sys.stdout
with open('plik.txt', 'a') as f:
    sys.stdout = f # Change the standard output to the file we created.
    f.write("\n")
    for i in l:
        print(i)
    print('This message will be written to a file.')
    sys.stdout = original_stdout
    
    
    