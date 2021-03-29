#!/usr/bin/env python
# coding: utf-8

# In[ ]:



thislist = []
x = range(2000,3201,1)
for n in x:
 if not(n % 7) and n % 5:
  thislist.append(n)


# In[ ]:


#question2

def factorielle(n):
    if n == 0:
        return 1
    else:
        return n * factorielle(n-1)
n = input('your number ? ')
n=int(n)
print(factorielle(n))


# In[ ]:


#question3



n = input('your number ? ')
n=int(n)
thisdict =	{}
i = 1
while i < n:
 thisdict[i] = i * i
 i += 1
 
print(thisdict)


# In[ ]:


#question4

ch=input('your word ? ')
i=input('number? ')
i=int(i)
i= i - 1
while int(i)>int(len(ch)):
 i=input('positive number lower than '+str(len(ch))+' ? ')
l = list(ch)
l[int(i)-1] = "" 
ch=("".join(l))
print(ch)


# In[ ]:


#question5


import numpy as np
a= np.array([[0 , 1], [2 , 3], [4 , 5]])
print(a)
print(a.tolist())


# In[ ]:


#question7

values = input("Input some comma seprated numbers : ")
list = values.split(",")
newlist = []
for i in list:
    a=([(2 * 50 * int(i))/30])
    a=round(a[0])
    print(a)

