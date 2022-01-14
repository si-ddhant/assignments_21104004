#Q1
#first we will take input by the user
a= float(input("enter first no."))
b= float(input("enter second no."))
c= float(input("enter third no."))

#program to find AVERAGE of the input no.s
avg = (a+b+c)/3
print(avg)

#Q2
#taking input of gross income and dependants from user
gInc = float(input("enter your gross income"))
dep = int(input("enter no. of dependants"))

rate= 0.2
std_ded= 10000 #standard deduction in dollars

taxable_income = gInc - std_ded - (dep*3000)

tax= taxable_income*rate
print("your tax is",tax)

#Q3
student = [21104004, "siddhant", 'M', "electrical engineering",9.5]
print(student)

#Q4
marks = [96,90,80,99,100]
marks.sort() #inbuilt function for sorting
print(marks)

#Q5a
colour = ["Red", "Green", "White","Black", "Pink", "Yellow"]

colour.pop(3)
print (colour)

#Q5b
colour = ["Red", "Green", "White", "Black", "Pink","Yellow"]

#replacing Black and Pink with Purple
colour[3:5] = ["Purple"]
print (colour)
