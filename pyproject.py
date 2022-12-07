'''enter a positive integer range [A, B] and system will find out the status (Prime or composite) of each number available
in the given range. At the end print the count also.'''

lower_value=int(input("Enter the lowest range  value: "))
upper_value=int(input("Enter the upper range value: "))
a=lower_value
b=upper_value
primeCount=0
compositeCount=0

print("Prime numbers from {} to {} are:- ".format(a,b))

for n in range(a,b+1):
    if n>1:
        for i in range(2,n+1):
            if n%i==0:
                break#(1,2,2,3)
        if i==n:
            print(n)
            primeCount=primeCount+1
            
print("Composite numbers from {} to {} are :- ".format(a,b))
for n in range(a,b+1):
    if n>1:
        for i in range(2,n+1):
            if n%i==0:
                break
        if i!=n:
            print(n)
            compositeCount=compositeCount+1

print("Total Prime numbers are :- {}".format(primeCount))
print("Total composite numbers are :- {}".format(compositeCount))