#!/usr/bin/env python
# coding: utf-8

# In[4]:


# employee data with key as id of the employee and values as age of the employee
e ={101: 43, 102: 25, 103: 43, 104: 31, 105: 26, 106: 28, 107: 29,
    108: 43, 109: 25, 110: 22, 111: 22, 112: 25, 113: 30, 115: 45, 116: 23,
    117: 29, 118: 28, 119: 30, 120: 28, 121: 42, 122: 39, 123: 29, 124: 42,
    125: 43, 126: 42, 127: 40, 128: 27, 129: 23, 130: 30, 131: 37, 132: 20, 
    133: 36, 134: 27, 135: 27, 136: 22, 137: 28, 138: 23, 139: 45, 140: 39,
    141: 29, 142: 33, 143: 39, 145: 34, 146: 26, 147: 30, 148: 38, 149: 29,
    150: 24, 151: 28, 152: 34, 153: 42, 154: 29, 155: 23, 156: 31, 158: 25, 
    160: 45, 161: 42, 162: 27, 163: 24, 164: 20, 166: 24, 167: 28, 168: 20,
    169: 33, 170: 34, 171: 37, 172: 45, 173: 35, 174: 23, 175: 44, 176: 27,
    177: 30, 178: 26, 179: 27} 


# In[5]:


type(e)


# # Identify the senior most employees age
# 
# - 45
# - 44
# - 48
# - 42

# In[6]:


max(dict.values(e))


# # Identify the age of the employee with employee id 159 [ If the employee isn't present return NA]
# 
# - 25
# - 32
# - NA
# - 42

# In[7]:


e.get(159,"NA")


# # Count the total number of employee in the organization
# 
# - 79
# - 78
# - 60
# - 74

# In[8]:


len(dict(e))


# # Calculate the mean age of the employees
# 
# - 31.36
# - 36.48
# - 28.77
# - 32.47

# In[9]:


round(31.36)


# In[14]:


round(36.48)


# In[15]:


round(28.77)


# In[16]:


round(32.47)


# # Perform the following two tasks and then calculate the updated mean age of the employees
# Task1 Update the ages of employee id - 104,140, and 164 as 27 <br>
# Task2 Remove the employ with employee id - 143 <br>
# 
# - 30.71
# - 31.36
# - 30.13
# - 31.13
# 

# In[10]:


round(30.71)


# In[11]:


round(31.36)


# In[12]:


round(30.13)


# In[13]:


round(31.13)


# In[14]:


### Task 1


# In[33]:


e


# In[40]:


e.update{(104:27, 140:27, 163:27)}


# In[ ]:


dict.

