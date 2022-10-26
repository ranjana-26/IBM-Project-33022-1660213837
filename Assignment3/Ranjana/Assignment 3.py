#ASSIGNMENT 3

#*** Power of number ***

from heapq import merge


print(7**4)

#*** Split the string ***

s = "Hi there sam!"
li = list(s.split(" "))
print(li)

#*** .format() method ***

text = "The diameter of {planet} is {diameter} kilometers."
print(text.format(planet = "Earth",diameter  = 12742))

#*** List index to print 'hello' ***

lst = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
print(lst[3][1][2][0])

#*** Dictionary grab the word "hello" ***

d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}
print(d['k1'][3]['tricky'][3]['target'][3])

#**** What is the main difference between a tuple and a list? ***

#Tuple is immutable
#Tuples operations are safe.
#Tuples consumes less memory.

#*** Create a function that grabs the email website domain from a string ***

def domainGet(email):
    print("Your domain is: " + email.split('@')[-1])

email = input("Please enter your email: >")
domainGet(email)

#*** The word 'dog' is contained ***

def findDog(st):
    if 'dog' in st.lower():
        print("True")
    else:
        print("False")

st = "Is there a dog here?"
findDog(st)

#*** Counts the number of times the word "dog" occurs ***

value = 'This dog runs faster than the other dog dude!'

def countdogs(value):
    count = 0
    for word in value.lower().split():
        if word == 'dog' or word == 'dogs':
            count = count + 1
            print(count)

countdogs(value)


#Problem

#*** Ticket ***

def caught_speeding(speed, is_birthday):
    if is_birthday:
        speeding = speed - 5
    else:
        speeding = speed
    
    if speeding > 80:
        return 'Big Ticket'
    elif speeding > 60:
        return 'Small Ticket'
    else:
        return 'No Ticket'

print(caught_speeding(65, True))
print(caught_speeding(75, False))
print(caught_speeding(86, False))

#*** Calculate total salary ***

lis = [20000, 35000, 26000, 78000, 56000, 34000]
sum = 0
for x in lis:
    sum += x

print(sum)

#*** Two dictionaries in Python ***

emp = {
    "Empid" : 1,
    "Empname": "Alex",
    "Basicpay" : 50000
}

dep = {
    "depname" : "IT",
    "depid" : "D41"
}
emp.update(dep)
print(emp)