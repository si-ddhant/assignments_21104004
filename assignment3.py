#QUESTION 1

#function to count word
def word_count(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts

#function to count characters
def letter_count(str):

    all_freq = {}
  
    for i in str:
        if i in all_freq:
            all_freq[i] += 1
        else:
            all_freq[i] = 1
    return all_freq
  
str1 =input("enter a word or sentence ")

#condition for string to be a word
if (" " not in str1):
    print(letter_count(str1))
    
else:   
    print(word_count(str1))



#QUESTION 2
#input current date
Day = int(input("enter day "))
Month = int(input("enter month "))
Year = int(input("enter year "))

#condition given in question
if (1<= Month<= 12) and 1<= Day<= 31 and 1800<= Year<= 2025:
    condn = True
else:
    condn = False

    
if condn == True:

    if 1<=Day<30 and Month != 2:
        date = Day +1
        print("Next Date is:",date,"/",Month,"/",Year)
    elif Day == 31 and Month == 12:
        date = 1
        mon = 1
        yr = Year +1
        print("Next Date is:",date,"/",mon,"/",yr)
    elif Day == 30 and Month == 4 or 6 or 9 or 11:
        date = 1
        mon = Month +1
        print("Next Date is:",date,"/",mon,"/",Year)
    elif Day == 28 and Month == 2:
        if Year%4 == 0:
            
            date = 29
            print("Next Date is:",date,"/",Month,"/",Year)
        elif Year%4 != 0:
            date = 1
            mon = Month + 1
            print("Next Date is:",date,"/",mon,"/",Year)
    elif Day == 29 and Month ==2:
        if Year%4 == 0:
            date = 1
            mon = Month + 1
            print("Next Date is:",date,"/",mon,"/",Year)  
        elif Year%4 != 0:
            print ("error")    
    else:
        date = 1
        mon = Month + 1
        print("Next Date is:",date,"/",mon,"/",Year)

else:
    print("error, write correct date")


#QUESTION 3
lst = [] #empty list
n = int(input("enter no. of elements"))

#inputing elements in the list
for i in range(n):
    n = int(input("element"))
    lst.append((n,n*n))
print (lst)

#QUESTION 4
grade = int(input("enter grade point "))

if grade == 10:
    letter_grade = "'A+'"
    performance = "Outstanding"
    
elif grade == 9:
    letter_grade = "'A'"
    performance = "Excellent"
    
elif grade == 8:
    letter_grade = "'B+'"
    performance = "Very Good"
   
elif grade == 7:
    letter_grade = "'B'"
    performance = "Good"
    
elif grade == 6:
    letter_grade = "'C+'"
    performance = "Average"
    
elif grade == 5:
    letter_grade = "'C'"
    performance = "Below Average"
   
elif grade == 4:
    letter_grade = "'D'"
    performance = "Poor"
if 4<=grade<=10:
    print ("Your Grade is", letter_grade, "and",performance,"performance")
else:
    print ("error, enter valid grade point")
    

#QUESTION 5
for i in range (1,7):
    for k in range(0,i-1):
        print("  ", end="")
    for j in range (0,13-(2*i)):
        ch1 = chr(65+j)
        print(ch1, end=" ")
    print("\n",end= "")


#QUESTION 6
student = {} #empty dictionary

#option a
while True:
    p = int(input("enter sid"))
    student[p]= input("enter name")
    n = input("Y or N ")
    if n == 'Y':
        continue
    elif n == 'N':
        break
print(student)

#option b
a = sorted(student.items(), key=lambda x: x[1])   
print(a)

#option c
for i in sorted (student):
    print((i,student[i]), end = " ")
print("\n")
 
#option d
srch = int(input("enter sid "))
print(student[srch])


#QUESTION 7
n = int(input("enter no. of terms"))
n1,n2 = 0,1
sum = 0
print("Fibonacci sequence:")
count = 0
while count < n:
    print(n1, end="",)
    nth = n1 + n2
    sum = sum + n1
    # update values
    n1 = n2
    n2 = nth
    count += 1
print ("\n")
print (sum/n)


#QUESTION 8
set1 = {1,2,3,4,5}
set2 = {2,4,6,8}
set3 = {1,5,9,13,17}

#option a
set4 = set1.union(set2) - set1.intersection(set2)
print (set4)

#option b
set5 = set1.union(set2.union(set3))- set1.intersection(set2)- set2.intersection(set3)- set3.intersection(set1)
print (set5)

#option c
set6 = set1.intersection(set2).union(set2.intersection(set3)).union(set3.intersection(set1))- set1.intersection(set2.intersection(set3))
print (set6)

#option d
set7 = set()

for i in range (1,11):
    if i in set1 :
        continue
    else:
        set7.add(i)
print (set7)   

#option e
set8 = set()
for i in range (1,11):
    if i in set1:
        continue
    elif i in set2:
        continue
    elif i in set3:
        continue
    else:
        set8.add(i)
print (set8)
