#1. Table of number n
"""
n = int(input("Enter the number "))  
for i in range(1,11):  
    c = n*i  
    print n,"*",i,"=",c

"""



#2. Print Even number btween 2 and n
"""
n = int(input("Enter the number "))  
for i in range(2,n,2):  
    print(i)  

"""




#3. Find greatest number from user input
"""
list = []
n = int(input("Enter the number of elements in the list:"))

for i in range(0,n):
    ele = int(input())
    list.append(ele)

print (list)

list.sort();
print ("Sorted list is :",list)
print ("largest element is: ",list[-1])
print ("largest number is: ",max(list))

"""



#4. Addition of the element of the list
"""
list = [];
n = int(input("Enter the number of elements in the list: "))

for i in range(0,n):
    ele = int(input())
    list.append(ele)
print (list)

sum =0
for i in list:
    sum = sum+i
print ("The sum is:",sum)

"""




#5. Number Pyramid // Nested for loop
"""
n = int(input("Enter the number of rows: "));

for i in range(0,n+1):
    for j in range(i):
        print(i,end="")
    
    print()

"""

#6. Cuberoot through bisection algorithm/aproaximation
"""
n = float(input("Enter number to find cuberoot of: "))
epsilon = 0.001
counter = 0
low = 0
high = n 
guess = (high+low)/2.0


if abs(n) >1:
    while abs(abs(guess)**3 - abs(n)) >= epsilon:
        if abs(guess)**3 < n:
            low = guess
        else:
            high = guess
        
        guess = (high+low)/2.0

        counter += 1

    print("number of iteration:",counter)
    print("Cuberoot of ",n,"is",guess)

if abs(n)<1:
    low = n
    high = 1
    guess = (high+low)/2.0

    while abs (abs(guess)**3 - abs(n)) >= epsilon:
        if n > 0:
            if guess**3 < n:
                low = guess
            else:
                high = guess

            guess = (high+low)/2.0
            counter += 1
        else:
            low = -1
            high = n
            if guess ** 3 > n:
                high = guess
            else:
                low = guess
            guess = (low + high) / 2.0
            counter+= 1
    print(counter)
    print("The cube root of",n,"is closest to:",guess)
"""


#7. String manipulation
"""
string1 = input("Enter the word")
i=0
for char in string1:
    print(string1[i])
    i+=1

"""

#8. lambda function
"""
lst = (10,22,37,41,100,123,29)  
oddlist = tuple(filter(lambda x:(x%2 != 0),lst)) # the tuple contains all the items of the tuple for which the lambda function evaluates to true    
print(oddlist)  

"""



#9 file handling
"""
from os import write
import os

fileObject = open("hello.txt","w")
fileObject.write("This message is appended from terminal.")
fileObject.close()


print("Changing file again")

change2 = open("hello.txt","a")
change2.write(" This is second update in file and it should be appended in last of the files, not ovewrite")
change2.close()

file = open("hello.txt","r")
content = file.read(2000)

print(type(content))
#print(content)

for i in file:
    print(i)


file.close()

os.getcwd()

"""





#10. Modules

import testModule

