#!/usr/bin/env python
# coding: utf-8

# # my lession 1 on Linear Algebra
# 
# https://github.com/engineersCode/EngComp4_landlinear

# In[23]:


import numpy
get_ipython().run_line_magic('matplotlib', 'inline')
from matplotlib import pyplot


# In[24]:


import sys
sys.path.append('../scripts/')

# Our helper with the functions
# plot_vector, plot_linear_transformation, plot_linear_transformations
from plot_helper import *


# In[25]:


vectors = [(2,2)]
tails = [(-3, -2), (-3, 1), (0, 0), (1, -3)]


# In[26]:


plot_vector(vectors, tails)


# In[27]:


vectors = [(2, 4)]
tails = [(0,0), (-1, 1)]
plot_vector(vectors, tails)


# Vector addition

# In[34]:


a = numpy.array((-2, 1))
b = numpy.array((1, -3))
origin = numpy.array((0, 0))
vectors = [a, b, a+b]
tails = [origin, a, origin]
plot_vector(vectors, tails)


# Vector scaling

# In[29]:


c = numpy.array((2, 1))
vectors = [c, 2*c]
plot_vector(vectors)


# In[30]:


c = numpy.array((2, 1))
vectors = [c, -2*c]
plot_vector(vectors)


# In[31]:


i = numpy.array((1, 0))
j = numpy.array((0, 1))

vec = 3*1 + 2*j

vectors = [i, j, 3*i, 2*j, vec]
plot_vector(vectors)


# **Linear combinations** -- adding together two vectors that were each scaled
# 
# **Span** -- set of all possible linear combinations

# In[32]:


from numpy.random import randint

vectors = []
for _ in range(40):
    m = randint(-10, 10)
    n = randint(-10, 10)
    vectors.append(m*i + n*j)
    
plot_vector(vectors)


# In[36]:


from numpy.random import randint

vectors = []
for _ in range(40):
    m = randint(-10, 10)
    n = randint(-10, 10)
    vectors.append(m*a + n*b)
    
plot_vector(vectors)


# In[37]:


d = numpy.array((-1, 0.5))


# In[38]:


vectors = []
for _ in range(40):
    m = randint(-10, 10)
    n = randint(-10, 10)
    vectors.append(m*a + n*d)
    
plot_vector(vectors)


# In[39]:


a


# In[40]:


d


# a and d share the same span because they describe the same line.  d is a multiple of a. therefore, they are linearly dependent.

# In[43]:


a


# In[41]:


b


# In[42]:


c


# We have vectors $\mathbf{a}$, and $\mathbf{b}$
# 
# $\mathbf{c}= 2*\mathbf{i} + 1*\mathbf{j}$
# 
# Use the components of $\mathbf{c}$ to make a linear combination of $\mathbf{a}$ and $\mathbf{b}$

# In[47]:


c_prime = 2*a + 1*b
c_prime


# In[48]:


# c_prime has the coordinates (2,1), i.e. c, in the a,b system of coordinates, wherein a,b are the basis vectors
# c_prime has the coordinate (-3,-1), in the i,j system of coordinates


# In[50]:


2*a


# In[51]:


1*b


# In[53]:


A = [[-2,1], [1,-3]]
A = numpy.array(A)
print(A)


# In[54]:


print(c)


# In[55]:


A.dot(c)


# In[56]:


A.dot(i) #=> a


# In[58]:


A.dot(j) #=> b


# In[59]:


plot_linear_transformation(A)


# In[60]:


M = [[1,2], [2,1]]
M = numpy.array(M)
print(M)


# In[61]:


M.dot(i)


# In[62]:


M.dot(j)


# In[63]:


plot_linear_transformation(M)


# In[65]:


x = numpy.array((0.5, 1))
vectors = [x, M.dot(x)]
plot_vector(vectors)


# In[67]:


N = numpy.array([[1,2], [-1,2]])
print(N)


# In[68]:


plot_linear_transformation(N)


# In[69]:


X = numpy.array([[2,3], [1,3]])
print(X)


# In[70]:


plot_linear_transformation(X)


# In[71]:


X = numpy.array([[-1,2], [2,-1]])
print(X)


# In[72]:


plot_linear_transformation(X)


# In[74]:


rotation = numpy.array([[0, -1], [1, 0]])
print(rotation)


# In[75]:


plot_linear_transformation(rotation)


# In[77]:


shear = numpy.array([[1,1], [0, 1]])
print(shear)


# In[78]:


plot_linear_transformation(shear)


# In[79]:


scaling = numpy.array([[2, 0], [0, 0.5]])
print(scaling)


# In[80]:


plot_linear_transformation(scaling)


# Special scaling matric that leaves the unit vectors the same length:
# **identity** matrix

# In[81]:


rotation_90_clockwise = numpy.array([[0, 1], [-1, 0]])
print(rotation_90_clockwise)


# In[82]:


plot_linear_transformation(rotation_90_clockwise)


# In[83]:


print(shear@rotation)


# In[84]:


plot_linear_transformation(shear@rotation)


# In[85]:


plot_linear_transformation(rotation@shear)


# **Inverse of a matrix** undoes the effect of the linear transformation

# In[88]:


from numpy.linalg import inv


# In[89]:


M


# In[93]:


M_inv = inv(M)


# In[91]:


plot_linear_transformations(M, M_inv)


# In[ ]:




