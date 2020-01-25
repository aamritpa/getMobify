#!/usr/bin/env python
# coding: utf-8

# In[14]:


import re
import pandas as pd
from subprocess import Popen, PIPE
import sys
import numpy as np


# In[2]:


print('Enter a Value\n')
entered=input()


# In[3]:


#Camel Case detection
def is_camel_case(s):
    if s[0]==s[0].upper():
        return False
    return s != s.lower() and s != s.upper() and "_" not in s

test1= is_camel_case(entered)
if (test1==True):
    print('Camel Case Detected') 


# In[6]:


#Pascal case detection
def is_pascal_case(s):
    if s[0]==s[0].upper():
        for i in range(1,len(s)):
            if s[i]==s[i].upper():
                print('Pascal Case Detected')
                return True
    return False
test2= is_pascal_case(entered)


# In[7]:


#Snake case detection
def is_snake_case(s):
    for i in range(len(s)):
        if (s[i]=='_'):
            return True
    return False

test3= is_snake_case(entered)
if (test3==True):
    print('Snake Case Detected')


# In[ ]:





# In[8]:


if (test3==True):
    #Snake case to Camel Case
    getvalue= input('For Camel 1, For Pascal 2')
    
    if int(getvalue)==1:
    
        REG = r"(.*?)_([a-zA-Z])"
        def camel(match):
            return match.group(1) + match.group(2).upper()

        def camel_upper(match):
            return match.group(1)[0].upper() + match.group(1)[1:] + match.group(2).upper()

        words = entered.splitlines()

        results = [re.sub(REG, camel, w, 0) for w in words]
        print( results)
    # Snake to Pascal
    if int(getvalue)==2:
        REG = r"(.*?)_([a-zA-Z])"
        def camel(match):
            return match.group(1) + match.group(2).upper()

        def camel_upper(match):
            return match.group(1)[0].upper() + match.group(1)[1:] + match.group(2).upper()

        words = entered.splitlines()

        results = [re.sub(REG, camel, w, 0) for w in words]
        good= pd.Series(1,dtype=np.str)
        good[0]=''
        for i in range(len(results)):
            if i==0:
                good[0]=good[0]+results[i].upper()
            else:
                good[0]= good[0]+results[i]
        print(good[0])


# In[15]:


if test2==True:
    # Pascal to Camel 
    getvalue= input('For Camel 1, For Snake 2')
    if int(getvalue)==1:
        good= pd.Series(1,dtype=np.str)
        good[0]=''
        for i in range(len(entered)):
            if i==0:
                good[0]=good[0]+entered[i].lower()
            else:
                good[0]= good[0]+entered[i]
        print( good[0])
    if int(getvalue)==2:
        # Pascal to Snake
        good= pd.Series(1,dtype=np.str)
        good[0]=''
        for i in range(len(entered)):
            if i==0:
                good[0]=good[0]+entered[i].lower()
            else:
                good[0]= good[0]+entered[i]
        print(''.join(['_'+i.lower() if i.isupper() else i for i in good[0]]).lstrip('_')) 


# In[ ]:


if test1==True:
    getvalue= input('For Snake 1, For Pascal 2')
    #Camel Case to Snake Case.
    if int(getvalue)==1:
        print(''.join(['_'+i.lower() if i.isupper() else i for i in entered]).lstrip('_')) 
    #Camel to Pascal
    if int(getvalue)==2:
        good= pd.Series(1,dtype=np.str)
        good[0]=''
        for i in range(len(entered)):
            if i==0:
                good[0]=good[0]+entered[i].upper()
            else:
                good[0]= good[0]+entered[i]
        print( good[0])


# In[ ]:





# In[85]:





# In[78]:





# In[ ]:





# In[ ]:




