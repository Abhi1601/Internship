#!/usr/bin/env python
# coding: utf-8

# Programming Question
# 

#  1. Write a python program to find a factorial of a number

# Answer below

# In[1]:


def fact(n) :
    if(n==0) :
        return 1
    else :
        return n*fact (n-1)


# In[2]:


x=int(input ("Enter x :"))
y=fact(x)
print("{}! {}".format(x,y))


# 2. write a python program weather a number is prime or composite

# In[7]:


n=input('Enter the number: ')
try:
    n=int(n)
except:
    print('Wrong input.')
    quit()
if n==1 or n==0:
    print('this is either prime or composite')
else:
    c=0

   


# In[8]:


for i in range(2,n):
       if n%i==0:
           c=c+1
       if c==0:
           print("this is prime number")
       else:
           print("this is composite number.")


# 3. Write a python program to check whether a given string is palindrome or not.

# In[10]:


String = input(" Oranges ")
str1=""


# In[12]:


for i in String:
    str1 = i + str1
print("String in reverse Order : ",str1)

if(String == str1):
    print("This is a Palindrome String")
else:
    print("This is Not a Palindrome String")


# 4. Write a Python program to get the third side of right-angled triangle from two given sides.

# In[20]:


def pythagoras(opposite_side,adjacent_side,hypotenuse):
    if opposite_side == str("x"):
        return ("opposite = " + str(((hypotenuse**2) - (adjacent_side**2))**0.5))
    elif adjacent_side == str("x"):
        return("Adjacent = " + str(((hypotenuse**2) - (opposite_side**2))**0.5))
    elif hypotenuse == str("x"):
        return ("hypotenuse = " + str(((opposite_side**2) + (adjacent_side**2))**0.5))
    else:
        return "the answer is!"
    
    


# In[22]:


print(pythagoras(6,7,'x'))
print(pythagoras(6,'x',8))
print(pythagoras('x',7,8))
print(pythagoras(6,7,8))


# 5. Write a python program to print the frequency of each of the characters present in a given string.

# In[29]:


#Answer
strQ = "AbhishekNipane"
print ("Given String: ",strQ)
res = {}
 
res={n: strQ.count(n) for n in set(strQ)}

print("Frequency of each character :\n ",res)

