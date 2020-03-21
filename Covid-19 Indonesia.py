#!/usr/bin/env python
# coding: utf-8

# In[1]:


from numpy import *


# In[2]:


x = array((1,2,6,8,9,10,11,13,14,15,16,17,18,19))
y = array((0,2,4,6,19,27,34,69,96,117,134,172,227,309))


# In[3]:


from scipy.interpolate import *


# In[4]:


from matplotlib.pyplot import *


# In[26]:


p3 = polyfit(x,y,5)


# In[27]:


print("Polynomial regression y = {:.4f} + {:.4f}x + {:.4f}x^2 + {:.4f}x^3 + {:.4f}x^4 + {:.4f}x^5".format(p3[0],p3[1],p3[2],p3[3],p3[4],p3[5]))


# In[28]:


ax = plot(x,y,'ro')
plot(x,polyval(p3,x),'b')
title('Polynomial Regression Covid-19')
grid()
xlabel('x')
ylabel('y')


# In[31]:


z = array((1,2,6,8,9,10,11,13,14,15,16,17,18,19,20,21,22,23))


# In[32]:


ax = plot(x,y,'ro')
plot(z,polyval(p3,z),'b')
title('Polynomial Regression Covid-19')
grid()
xlabel('tanggal')
ylabel('positif covid')


# In[ ]:




