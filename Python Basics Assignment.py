#!/usr/bin/env python
# coding: utf-8

# In[10]:


#1.Explain the key features of Python that make it a popular choice for programming?
#Ans: Python is a programming language.It is widely used in the data industry.
#         Features of Python:
#         1.It has lot of libraries(around 137000).
#         2.It has huge active community.
#         3.It is versatile as it can be used in web development,machine learning etc.
#         4.It is easy to learn.
#Python is popular because of its simplicity and it is easy to learn.And it is widely used in the field of data science 
#and data analytics
    
    
 


# In[12]:


#2.Describe the role of predefined keywords in Python and provide examples of how they are used in a
#program

#Ans: Python Keywords are some predefined and reserved words in Python that have special meanings.
#Keywords are used to define the syntax of the coding.

#for example print is a keyword in python which is used to print the content or output on the console screen

print("This is a sample")


#if keyword is used to test the condition:

a=4 
if(a):
    print("Inside the if condition")

#and is a logical operator which returns true if both the operands are true else returns false.
 
c=5
if((c==5) and (a==4)):
    print("OK")
#some of the keywords of python are:
#or is  a logical operator which returns true if anyone operand is true else returns false.
#not is  a logical operator it returns True if the operand is false else returns false.
#elif is a condition statement used with an if statement. The elif statement is executed if the previous conditions were not true.
#else is used with if and elif conditional statements. The else block is executed if the given condition is not true.
#for is used to create a loop.
#while is used to create a while loop.
#break is used to terminate the loop.
#as is used to create an alternative.
#def is used to define functions.
#True



# In[15]:


#3 Compare and contrast mutable and immutable objects in Python with examples

#Ans: Mutable Objects:A mutable object is an entity whose value can be altered after its creation.Exmaples are
#Lists
#Dictionaries
#Sets

#example of list:
my_list = [1, 2, 3]
my_list[0] = 'a'
print(my_list)

#Immutable Objects:A immutable object is an entity whose value cannot be altered after its creation.Exmaples are
#Numbers
#Strings
#Tuples

#example of the tuple:
my_tuple=(1,2,3)
#my_tuple[0]=1 this will result in error
print(my_tuple)




# In[16]:


#4. Discuss the different types of operators in Python and provide examples of how they are used?

#Ans Python language supports various types of operators, which are:
#Arithmetic Operators(+,-,*,/,%,**,//).
a=2
b=3
c=a+b
print(c)

#Comparison Operators(==,!=,>,<,>=,<=).
d=7
e=8
if(e>d):
    print("yes")


#Assignment Operators(=,+=,-=,/=,%=).
a+=5
print(a)

#Logical Operators(and,or,not).
if(e==8)and(d==7):
    print("yes")

#Bitwise Operators(&,|,~,^,<<,>>).
f=a&b
print(f)

#Membership Operators(in,not in).
l=[1,2,3]
a=1
if(a in l):
    print("yes a is in l")

#Identity Operators(is,is not).It returns boolean value
b=a
print(b is a)



# In[17]:


#5.Explain the concept of type casting in Python with examples

# Ans Python program to demonstrate 
# implicit type Casting 
 
# Python automatically converts 
# a to int 
a = 7
print(type(a)) 
 
# Python automatically converts 
# b to float 
b = 3.0
print(type(b)) 
 
#Explicit Type Conversion in Python
#In this method, Python needs user involvement to convert the variable data type into the required data type.

#Mainly type casting can be done with these data type functions:

#Int(): Python Int() function take float or string as an argument and returns int type object.
#float(): Python float() function take int or string as an argument and return float type object.
#str(): Python str() function takes float or int as an argument and returns string type object.

# Python program to demonstrate 
# explicit type Casting 
 
# int variable
a = 5
 
# typecast to float
n = float(a)
 
print(n)
print(type(n))
 
    
    


# In[18]:


#6. How do conditional statements work in Python? Illustrate with examples?

#ans Conditional statements in python are used to test the condition ther are as follows:
#if
a=10
if(a>8):
    print("yes")

#if-else
if(a<8):
    print("ok")
else:
    print("yes")
    

#if-elif-else
if(a>11):
    print("ok")
elif(a>8):
    print("yes")
else:
    print("ok")

    
    
#nested if else
if(a):
    if(a>4):
        print("yes")
    else:
        print("no")
else:
    print("a is equal to 0")


# In[19]:


#7 Describe the different types of loops in Python and their use cases with examples.

#ans While Loop in Python
#In Python, a while loop is used to execute a block of statements repeatedly until a given condition is satisfied. When the condition becomes false, the line immediately after the loop in the program is executed.

#Python While Loop Syntax:
#while expression:
#    statement(s)

count = 0
while (count < 3):
    count = count + 1
    print("Hello")

#For Loop in Python
#For loops are used for sequential traversal. For example: traversing a list or string or array etc. 


#For Loop Syntax:

#for iterator_var in sequence:
 #   statements(s)

n = 4
for i in range(0, n):
    print(i)


# In[ ]:




