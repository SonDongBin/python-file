#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

# ./dataset/auto-mpg.csv 파일을 읽어와서 데이터프레임 생성
df = pd.read_csv('./dataset/auto-mpg.csv', header=None)
df.head()


# In[2]:


# 칼럼 이름 변경
df.columns = ['mpg','cylinders','displacement','horsepower','weight',
              'acceleration','model year','origin','name']
df


# In[3]:


# 데이터프레임의 기본 정보 : df.info()
df.info()


# In[4]:


print(df.dtypes) # 각 칼럼의 데이터 타입 출력
#print(df.mpg.dtype)
# 기술 통계정보 확인 df.describe()
df.describe(include='all')


# In[5]:


# 데이터프레임의 정보
# 각 열의 데이터 갯수 확인 : 객체.count()
df.count()  # Nan 자료를 제외한 실제 값이 존재하는 자료의 갯수
# df.mpg.count()


# In[12]:


# 각 열의 고유의 갯수 : unique(), df['열명'].value_counts()
print(df['origin'].value_counts())
print(df.origin.dtype)
type(df['origin'].value_counts())


# In[8]:


# 통계함수 : 평균값 -> df 평균, 각 열의 평균
# df.mean(), df['열명'].mean()
# medium(), max(), min()
print(df.mean(numeric_only=True))
print(df['mpg'].mean())


# In[9]:


df.corr()  # df[['mpg', 'weight']].corr()


# In[10]:


df[['mpg', 'weight']].corr()


# In[15]:


import seaborn as sns

titanic = sns.load_dataset('titanic')
titanic.info()
titanic[['survived','age','deck']].count()


# In[ ]:


# titanic 자료를 가져와서 처음 10개의 자료를 검색
# 칼럼명 출력
# 20번째에서 30번째까지의 자료중 survived, age, fare, class 칼럼의 정보만 출력
# age 칼럼의 갯수 출력
# age를 한번씩만 출력


# In[22]:


titanic = sns.load_dataset('titanic')

print(titanic.head(10))

print(titanic.columns)

print(titanic.loc[20:30,['survived', 'age', 'fare', 'class']])

print(titanic['age'].count())
print(titanic['age'].unique())


# In[ ]:




