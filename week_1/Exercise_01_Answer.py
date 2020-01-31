#!/usr/bin/env python
# coding: utf-8

# 1. Create 5 list comprehensions to solve the following 5 problems:
#     1. Iterate a list of names to return a list of the names starting with H

# In[8]:


names = ["Hans", "Hugo", "Mikkel", "Benny", "Christian"]
hInNames = [name for name in names if "H" == name[0]]
hInNames


# B. In one line create a list of the numbers 1-100 to the power of 3

# In[10]:


powerList = [p**3 for p in range(1,101)]


# C. Iterate a list of names to create a list of tuples where the tuples first value is the length of the name and the second is the name

# In[8]:


names = ["Hans", "Hugo", "Mikkel", "Benny", "Christian"]
namesTuples = [(len(name), name) for name in names]
print(namesTuples)


# D. Iterate over each character in a string and get only those that are nummeric

# In[12]:


string = "sde84nfdn3f4ng"
numbers = [i for i in string if i.isdigit()]
print(numbers)


# E. Using only a list comprehension wrapped in set() get all possible combination from throwing 2 dice

# In[25]:


combi = set([(d1, d2) for d1 in range(1,7) for d2 in range(1,7)])
print(combi)


# 2. Create 2 dictionary comprehensions to solve the following:
#  1. Iterate a list of names and create a dictionary where key is the name and value is the length of the name

# In[26]:


names = ["Hans", "Hugo", "Mikkel", "Benny", "Christian"]
dict_variable = {name:len(name) for name in names}
print(dict_variable)


# B. Iterate a list of numbers and create a dictionary with (key, value) being (number, squareroot of number)

# In[36]:


import math
numbers = [1, 9, 81, 100, 256]
numbers_dict = {number:int(math.sqrt(number)) for number in numbers}
print(numbers_dict)


# 3. Progammatically using loops create a small program to produce a dictionary with all the 2 dice throw combinations as keys and their likelyhood in percent as values

# In[35]:


combi = set([(d1, d2) for d1 in range(1,7) for d2 in range(1,7)])
chances = {2:1,3:2,4:3,5:4,6:5,7:6,8:5,9:4,10:3,11:2,12:1}
like = {}
for x,y in combi:
    like[x,y] = (chances[x+y]/36)*100
print(like)

