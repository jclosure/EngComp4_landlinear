#!/usr/bin/env python
# coding: utf-8

# # My lesson 2

# In[8]:


import numpy
get_ipython().run_line_magic('matplotlib', 'notebook')
from matplotlib import pyplot
import sys
sys.path.append('../scripts/')

# Our helper with the functions
# plot_vector, plot_linear_transformation, plot_linear_transformations
# import plot_config
# plot_config.use_notebook = True
from plot_helper import *


# In[9]:


A = numpy.array([[1, 1], [-1, 1]])
print(A)


# In[4]:


plot_linear_transformation(A)


# In[15]:


i = numpy.array([1, 0])
j = numpy.array([0, 1])


# In[16]:


a = numpy.array([1, -1])
b = numpy.array([1, 1])


# In[17]:


vectors = [i, a] # where i landed
plot_vector(vectors)


# In[18]:


numpy.linalg.norm(i)


# In[19]:


numpy.linalg.norm(a)


# In[20]:


numpy.sqrt(2)


# In[21]:


plot_linear_transformation(A)


# In[22]:


A_inv = numpy.linalg.inv(A)


# In[23]:


plot_linear_transformation(A)
plot_linear_transformation(A_inv)


# In[24]:


plot_linear_transformations(A, A_inv)


# In[27]:


B = numpy.array([[1, 1], [0, -1]])
print(B)


# In[28]:


B_inv = numpy.linalg.inv(B)
print(B_inv)


# In[29]:


plot_linear_transformation(B)
plot_linear_transformation(B_inv)


# In[30]:


plot_linear_transformations(B, B_inv)


# In[32]:


C = numpy.array([[2, 1], [1, 2]])
print(C)
plot_linear_transformation(C)


# In[33]:


alpha = numpy.linspace(0, 2*numpy.pi, 41)


# In[34]:


vectors = list(zip(numpy.cos(alpha), numpy.sin(alpha)))


# In[35]:


plot_vector(vectors)


# In[36]:


vectors[0]


# In[38]:


C.dot(numpy.array(vectors[0]))


# In[41]:


newvectors = []
for i in range(len(vectors)):
    newvectors.append(C.dot(numpy.array(vectors[i])))


# In[42]:


plot_vector(newvectors)


# In[43]:


lengths = []
for i in range(len(newvectors)):
    lengths.append(numpy.linalg.norm(newvectors[i]))


# In[44]:


semi_major = max(lengths)
print(semi_major)


# In[45]:


semi_minor = min(lengths)
print(semi_minor)


# In[49]:


# semi major longest lies at 45 degrees which means that x and y equally contribute to it. therefore we can take the
# length of the semi_major (norm) and find it's components by dividing it by the squareroot of 2
s = semi_major/numpy.sqrt(2)


# In[50]:


u1 = numpy.array([s, s])
print(u1)


# In[51]:


C_inv = numpy.linalg.inv(C)
v1 = C_inv.dot(u1)


# In[52]:


plot_vector([u1, v1])


# The vector that landed on the semi-axis was only scaled by the effect of ${C}$.

# semi-minor

# In[54]:


u2 = numpy.array([semi_minor/numpy.sqrt(2), -semi_minor/numpy.sqrt(2)])
print(u2)


# In[75]:


v2 = C_inv.dot(u2)
print(v2)


# In[76]:


plot_vector([u2, v2])


# In[77]:


numpy.linalg.norm(u2)


# -----
# 
# ## System of equations

# In[78]:


A


# In[80]:


c = numpy.array([1, 5])
print(c)


# In[82]:


x = A_inv.dot(c) # is the vector that lands in c after the transformation
print(x)


# Row by row the system represents two lines:
# 
# $$ y = 1-x $$
# $$ y = 5+x $$

# In[88]:


xvalues = numpy.linspace(-4,2)
m1, b1, m2, b2 = -1, 1, 1, 5

pyplot.figure(figsize=(2,2))
pyplot.plot(xvalues, m1*xvalues+b1)
pyplot.plot(xvalues, m2*xvalues+b2)
pyplot.scatter(x[0], x[1])


# In[90]:


# numpy also has builtin support for solving for a transform A with the given vector C
x = numpy.linalg.solve(A, c)
print(x)


# In[91]:


# made from prev 2 vectors a and d, which are colinear
D = numpy.array([[-2, -1], [1, 0.5]])
print(D)


# In[92]:


plot_linear_transformation(D)


# In[93]:


# D doesn't have an inverse, it's a singular matrix that smashes the whole 2D space into a line. 
# It cannot be unpacked back into the entire 2D space


# In[ ]:


xvalues = numpy.linspace(y)

