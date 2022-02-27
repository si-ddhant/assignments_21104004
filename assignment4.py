#QUESTION1
def hanoi(n,A,C,B):
    if n == 0:
        return
    hanoi(n-1,A,B,C)
    print ("move",n,"from", A, "to",C)
    hanoi(n-1,B,C,A)
hanoi(3,'a','b','c') #a,b,c are tower names


#QUESTION2
#recursive method
def pascal(row, column):
    if column == 0:
        return 1
    elif row == 0:
        return 0
    else:
        return pascal(row-1, column) + pascal(row-1, column-1)

n = int(input("enter no. of rows "))
for i in range(n):
    for j in range((n-i+1)):
        print(' ',end ="")
    for j in range (n):
        if j>i:
            continue
        print(pascal(i,j), end =" ")
    
    print("")


#iteratative method
for line in range(1, n + 1):

    print('  ' * (n - line), end='')

    x = 1
    for i in range(1, line + 1):
        print(x, end='   ')

        x = x * (line - i) // i
    print()


#QUESTION3
def fun(a,b):
    divmod(a,b)
    return divmod(a,b)
num1 = int(input("enter first no. "))
num2 = int(input("enter second no. "))
a = fun(num1,num2)

#inbuilt function to find if the function is callable
#a
print("print true if the function is callable: ",callable(fun(num1,num2)))

#b
print("print true if all values are non zero : ",bool(0 not in a))

#c
b = a + (4,5,6)
print("unfiltered : ",b)

#inbuilt function to filter 
c = filter(lambda x: x<=4, b)
print("filtered tuple: ",tuple(c))

d = filter(lambda x: x<=4, b)

#d
e = set(d)
print("converted into set data type : ",e)

#e
f = frozenset(e) #makes set immutable
print("immutable set",f)

#f
print("maximum value in the set : ",max(f))
print("Hash value of the max value : ",hash(max(f)))


#QUESTION4
class Student:
    def __init__(self, student, sid):
        self.name = student
        self.sid = sid

    def __del__(self):
        print("Object deleted")
    def details(self):
        print(self.name , self.sid)


# creating object
student1 = Student("siddhant", 21104004)
print("Object created")

# printing the assigned values
print("NAME     ROLL_NUMBER")
student1.details()


# deleting object
del student1
print("")


#QUESTION5
class Employee():
    def __init__(self, name , salary):
        self.name = name
        self.salary = salary
    def details(self):
        print(self.name ,  self.salary)
   
        
employee1 = Employee("Mehak" , 40000)
employee2 = Employee("Ashok" , 50000)
employee3 = Employee("Viren" , 60000)

print("NAME  SALARY")
employee1.details()
employee2.details()
employee3.details()

print("\nupdating details of mehak... ")

print("updated details of mehak :")
print("NAME  SALARY")
employee1.salary = 70000
employee1.details()

del employee3


#QUESTION6
import enchant
d = enchant.Dict("en_US")

# inputting a word from the first friend
word = input("Enter the first word: ")

# inputting a meaningful word with the exact same letters
testword = input("\nEnter a new meaningful word to test your friendship: ")


# defining dictionary from last assignment
def count_in_dict(word):
    count = {}
    list1 = list(word)

    n = len(list1)
    for i in range(n):
        if list1[i] in count:
            count[list1[i]] += 1
        else:
            count[list1[i]] = 1
    return count


# test to verify the letters of the new word
if count_in_dict(word) != count_in_dict(testword):
    print("The letters aren't exact, friendship is fake!!")

if d.check(testword):
    print ("real")
else:
    print("fake")