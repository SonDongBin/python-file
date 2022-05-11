#!/usr/bin/env python
# coding: utf-8

# In[2]:


# 남북한발전전력량.xlsx 파일을 가져와서 그래프로 표현
import pandas as pd

df = pd.read_excel('./dataset/남북한발전전력량.xlsx')

df  # 남한과 북한의 합계와 년도별 자료만 추출
df_ns = df.iloc[[0,5], 3:]
df_ns


# In[3]:


# 인덱스명을 변경
df_ns.index = ['South','North']
df_ns


# In[6]:


# df_ns.info()  # 년도가 칼럼명 -> object 를 int 형으로 변경
df_ns.columns = df_ns.columns.map(int)
df_ns.columns


# In[8]:


# 그래프 그리기
df_ns.plot()

# 인덱스와 칼럼을 전치 변환
df_nst = df_ns.T
df_nst.plot()


# In[11]:


df_nst.plot(kind='bar')  # 막대그래프
df_nst.plot(kind='hist')  # 히스토그램


# In[12]:


# scatter , boxplot 그리기
df = pd.read_csv('./dataset/auto-mpg.csv')
df.columns = ['mpg','cylinders','displacement','horsepower','weight',
              'acceleration','model year','origin','name']
df.head()


# In[13]:


# 'mpg', 'weight'의 scatter 그리기
df.plot(x='mpg', y='weight', kind='scatter')


# In[15]:


df[['mpg','cylinders']].plot( kind='box')  # 이상점 발견하고자 할 경우


# In[16]:


df[['mpg','cylinders']]


# In[ ]:




