#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import test_package.module_a as a
import test_package.module_b as b


# In[ ]:


print(a.variable_a, b.variable_b)


# In[ ]:


from test_package import module_a, module_b


# In[ ]:


module_a.variable_a


# In[1]:


from test_package import *  # __init__.py -> __all__ = [모든 모듈명]


# In[2]:


module_a.variable_a


# In[ ]:




