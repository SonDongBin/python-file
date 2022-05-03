#!/usr/bin/env python
# coding: utf-8

# In[2]:


# 모듈 import 모듈명, from 패키지 또는 모듈명 import 모듈명 또는 함수명, 변수
# import 모듈 as 사용하고자 하는 식별자 (별명)
import math as mt

print(mt.sin(1))
print(mt.floor(4.5))
print(mt.ceil(4.5))


# In[3]:


from math import sin, cos, floor

sin(10)


# In[10]:


# random 모듈 사용해 보기
import random

print("random() : ",random.random())
print("uniform() : ",random.uniform(1,10))
print("range() : ",random.randrange(10))
list_a = [1,2,3,6,23]
print("choice() : ",random.choice(list_a))
print("shuffle() : ",random.shuffle(list_a))
print("shuffle() : after ",list_a)
print("sample() : ",random.sample(list_a,k=2))


# In[13]:


import os

print(os.name, os.getcwd())
print(os.listdir())
print(os.mkdir('test_dir'))


# In[15]:


print(os.listdir())
os.rmdir('test_dir')
print(os.listdir())


# In[16]:


import random
lotto_number_list = []
num = random.randrange(1, 46)
for i in range(7) :
    while num in lotto_number_list :
        num = random.randrange(1, 46)
    lotto_number_list.append(num)
print('Lotto number : {}, {}, {}, {}, {}, {}\nBonus number : {}'.      format(lotto_number_list[0], lotto_number_list[1], lotto_number_list[2],             lotto_number_list[3], lotto_number_list[4], lotto_number_list[5], lotto_number_list[6]))


# In[ ]:




