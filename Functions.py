                                #####Functions#####

#pass variables as an arguments                            
def add(a,b):
    c=a+b
    return print(a," + ",b," = ",c)

add(1,2)

#Pass list as an argument
def addlist(n):
    a=0
    for i in n:
      a+=i
    return(a)
       
y=[10,20,30,50,60,80,90,100]

print(addlist(y))

def add(a,b): c=a+b return print(a," + ",b," = ",c)


#Arbitary arguments
def multiply(*z):
    x=1
    for i in z:
        x*=i
    return x

multiply(2,4,6,8,10)


#recurive functions
#factorial
def fact(n):
    if n == 1:
       return n
    elif n == 0:
        return 1
    elif n < 1:
       return ("Number should be greater than 1")
    else:
       return n*fact(n-1)

print(fact(int(0)))


#Map function

strings = ["map","reduce","filter"]

uppercase=list(map(str.upper,strings))

print(uppercase)


#Filter Function

numbers=range(1,100)

def multiples5(n):
    if n%5==0:
        return n

number_divisibleby5 = list(filter(multiples5, numbers))

print(number_divisibleby5)


#reduce function

from functools import reduce

numbers=range(1,10)
def add(a,b):
    return a+b

output= reduce(add,numbers)
print(output)

#with initial value
numbers=range(1,10)
def add(a,b):
    return a+b

output= reduce(add,numbers,100)
print(output)


#lambda function

#map with lambda
strings = ["map","reduce","filter"]
uppercase=list(map(lambda x: x.upper(),strings))
print(uppercase)

#filter with lambda
numbers=range(1,100)
number_divisibleby5 = list(filter(lambda n:n%5==0, numbers))
print(number_divisibleby5)

#reduce with lambda
numbers=range(1,10)
output= reduce(lambda a,b:a+b,numbers)
print(output)