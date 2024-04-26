#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np 
arr1=np.array([6,7,8,9,10]) 
arr2=np.array([1,2,3,4,5]) 
print("array1:",arr1) 
print("array2:",arr2) 
print("addition : ", np.add(arr1,arr2)) 
print("subtraction : ", np.subtract(arr1,arr2)) 
print("multiplication : ", np.multiply(arr1,arr2)) 
print("division : ", np.divide(arr1,arr2)) 
print("modulo division : ", np.mod(arr1,arr2)) 
print("power : ", np.power(arr1,arr2)) 
print("quiotent modulus : ", np.divmod(arr1,arr2)) 


# In[4]:


import numpy as np 
a=np.array([[1,2,3],[4,5,6],[7,8,9]]) 
print(a[1:3]) 
print(a[0:]) 
print(a[2:3]) 
print(a[1,2:]) 
print(a[2]) 


# In[7]:


import numpy as np 
pi=np.pi 
arr1=np.array([1,2,3,4]) 
arr2=np.array([1,pi/6,pi/4,2])

b=np.cos(arr2) 
c=np.tan(arr2) 
d=np.average(arr1) 
e=np.sqrt(arr1) 
f=np.log(arr2) 
g=np.exp(arr2) 
print("array1:",arr1) 
print("array2:",arr2) 
print("sin(arr2) :",np.sin(arr2)) 
print("cos(arr2) :",b) 
print("tan(arr2) :",c) 
print("average(arr1) :",d) 
print("sqrt(arr1) :",e) 
print("log(arr2) :",f) 
print("sqrt(arr2) :",g) 


# In[8]:


import numpy as np 
arr=np.array([1,2,3,4,5]) 
a=np.mean(arr) 
b=np.std(arr) 
c=np.var(arr) 
d=np.percentile(arr,100) 
e=np.cumsum(arr) 
f=np.cumprod(arr) 
g=np.amax(arr) 
h=np.amin(arr) 
print("array:",arr) 
print("mean:",a) 
print("standard deviation:",b) 
print("variance:",c) 
print("percentile:",d) 
print("cummulative sum:",e) 
print("cummulative product:",f) 
print("maximum value:",g) 
print("minimum value:",h) 


# In[11]:


import numpy as np 
arr1=np.array([1,2,3,4]) 
arr2=np.array([3,4,6,7]) 
print("array1:",arr1) 
print("array2:",arr2) 
a=np.union1d(arr1,arr2) 
b=np.intersect1d(arr1,arr2) 
c=np.setdiff1d(arr1,arr2) 
d=np.unique(arr1) 
print("union1d:",a) 
print("intersection1d:",b) 
print("setdifference1d:",c) 
print("unique:",d) 


# In[12]:


import numpy as np 
arr1=np.array([1,2,3]) 
arr2=np.array([5,6,7]) 
print("product:", np.dot(arr1,arr2)) 
print("inner product :", np.inner(arr1,arr2)) 
print("outer product :", np.outer(arr1,arr2)) 
print("vector product:", np.cross(arr1,arr2)) 


# In[14]:


import numpy as np 
arr=np.array([[1,2,9],[4,5,6],[7,8,9]]) 
arr1=([[1,2],[3,4]]) 
arr2=([[3,4],[5,6]]) 
print("matrix is:",arr) 
a=np.linalg.det(arr) 
b=np.linalg.inv(arr) 
c=np.trace(arr) 
d=np.matmul(arr1,arr2) 
print("determinant :",a) 
print("inverse :",b) 
print("trace :",c) 
print("matrix multiplication :",d) 


# In[16]:


import numpy as np 
arr=np.array([[1,2],[3,4]]) 
print("matrix is:",arr) 
b,c=np.linalg.eig(arr) 
d,e,f=np.linalg.svd(arr) 
print("eigen values:",b) 
print("eigen vectors:",c) 
print("singular value decomposition:",d) 
print(e) 
print(f) 


# In[17]:


import numpy as np 
import random 
a=np.random.uniform(low=0.0,high=1.0,size=5) 
b=np.random.normal(loc=0.0,scale=1.0,size=5) 
c=np.random.binomial(n=10,p=0.5,size=3) 
d=np.random.chisquare(df=2,size=4) 
print("uniform :",a) 
print("normal :",b) 
print("binomial :",c) 
print("chisquare :",d)


# In[23]:


import random
import numpy as np
import matplotlib.pyplot as plt

# Function to perform a random walk
def random_walk(steps):
    position = 0
    trajectory = [position]
    for _ in range(steps):
        step = 1 if random.randint(0, 1) else -1
        position += step
        trajectory.append(position)
    return trajectory

# Perform random walk with 1000 steps
steps = 1000
trajectory = random_walk(steps)

# Extract statistics using numpy
min_value = np.min(trajectory)
max_value = np.max(trajectory)

# Plot the random walk trajectory
plt.plot(trajectory)
plt.title("Random Walk with 1000 Steps")
plt.xlabel("Step")
plt.ylabel("Position")
plt.grid(True)
plt.show()


# In[ ]:




