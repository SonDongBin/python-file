#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# %load include.py
#!/usr/bin/env python

# In[ ]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams['font.family'] ='Malgun Gothic'
matplotlib.rcParams['axes.unicode_minus'] =False


# In[13]:


import seaborn as sns


# In[14]:


df = sns.load_dataset('titanic')
df.info()

# deck 칼럼의 값의 갯수 확인 : value_counts()
print(df['deck'].value_counts(dropna=False).sum())
print(df['deck'].value_counts().sum())
# isnull() -> Null 이면 True 아니면 False
# notnull() -> Null 이면 False 아니면 True
print(df.head().isnull.sum(axis=0))
print(df.head().notnull.sum(axis=1))


# In[15]:


# 검색된 누락 데이터 제거
nan_df = df.isnull()
nan_df.columns


# In[16]:


for col in nan_df.columns:
    nan_cnt = nan_df[col].value_count()
    
    try:
        print(col, ' : ', nan_cnt[True])
    except:
        print(col, ' : ', 0)


# In[17]:


df.info()


# In[18]:


# deck 칼럼의 null 개수 많음 -> 삭제 , dropna(thresh=500)
df_1 = df.dropna(axis=1, thresh=500)
df_1.columns


# In[19]:


df_1 = df.dropna(subset=['age','deck'], how='any', axis=0)
df_1.info()


# In[20]:


# 누락데이터 치환
print(df['age'].head(10))

# 'age' 칼럼의 값을 평균값으로 대체 변경
df_copy = df.copy()


# In[21]:


df_copy['age'].fillna(df_copy['age'].mean(), inplace=True)
df_copy['age'].head(10)


# In[22]:


df_copy['age'].value_counts(dropna=True).idxmax()


# In[23]:


df_2 = df.copy()
df_2['age'].head(7)
df_2['age'].fillna(df['age'].value_counts(dropna=True).idmax(), inplace=True)
df_2['age'].head(10)


# In[24]:


df_3 = df.copy()
df_3['age'].fillna(method='ffill',inplace=True)
df_3['age'].head(10)


# In[ ]:


# titanic 자료를 로드해서 df에 저장한후
# 1. deck 칼럼을 삭제하고
# 2. age 의 Nan에 age의 가장 작은 값을 대체
# 3. embark_town의 820에서 835번째 자료를 검색
# 4. embark_town 칼럼의 Nan은 이전 값으로 대체
# 5. embark_town의 820에서 835번째 자료를 검색(수정된 자료를 확인)


# In[ ]:


# 남북한발전전력량을 읽어와서
# 모든 자료가 Nan인 행을 삭제
# 누락데이터에 이전자료를 대체
# 남한의 자료만 추출 후 칼럼의 값이 같은 칼럼을 삭제
# 처음 나오는 칼럼을 인덱스로 설정
# 년도를 int로 변경
# 년도를 인덱스로 변경

