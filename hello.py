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




#7. String manipulation
"""
string1 = input("Enter the word")
i=0
for char in string1:
    print(string1[i])
    i+=1

"""
