#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[3]:


# 시리즈 개별 원소에 함수를 매핑 : 시리즈 객체.apply(함수)
def add_10(n):
    return n + 10
def add_two_obj(a, b):
    return a + b

print(add_10(30))
print(add_two_obj(20,40))


# In[4]:


import seaborn as sns

titanic = sns.load_dataset('titanic')
titanic.head()  # 'age'와 'fare' 칼럼의 정보만 추출하여 df 생성
df = titanic.loc[ : , ['age','fare']]
df.head()


# In[9]:


# age 칼럼의 모든 값에 add_10을 적용
# 시리즈 개별 원소에 함수를 매핑 : 시리즈객체.apply(함수)
df['age'].apply(add_10).head()

# age 칼럼의 모든 값에 20을 더한 값을 출력
df['age'].apply(add_two_obj, b=20)

# add_10을 lambda 로 변경
# df['age'].apply(lambda x: add_10(x))
df['age'].apply(lambda x: x + 10).head(3)


# In[11]:


# 데이터프래임의 각 원소에 함수 매핑 : 데이터프레임객체.applymap(함수)
df.applymap(add_10).head()


# In[12]:


# 데이터프레임의 각 원소에 함수 매핑 : 데이터프레임객체.apply(함수, axis=0)
df.apply(add_10, axis=0)  # add_10(a) a<- df의 각 칼럼이 


# In[16]:


df.apply(lambda x: x + 10, axis=0)


# In[17]:


df.apply(lambda x: x.max() - x.min(),axis=1)


# In[ ]:


#### titanic 에서 'age'와 'fare'칼럼의 정보만 추출
# age가 20이상 70 미만인 자료만 검색
# m_age 칼럼 추가 : age의 max에 자신의 age를 뺀 값
# m_fare : fare + age 값을 넣으세요
df= titanic.loc[(titanic.age >= 20) & (titanic.age < 70), ['age','fare']]
max_age = df.age.max()
df['m_age'] = df.apply(lambda x: max_age - x.age, axis=1)
df['m_fare'] = df.apply(lambda x: x.fare + x.age, axis=1)
df.head()
# df = titanic.loc[ : , ['age','fare']]
# df['age'].apply(lambda x: 20 <= x < 70)
# df


# In[26]:


df = titanic.loc[ : , ['age', 'fare']]

def missing_value(x):
    return x.isnull()

def missing_count(x):
    return missing_value(x).sum()

def total_number_missing(x):
    return missing_count(x).sum()


# In[27]:


df.pipe(missing_value)  # dataframe
df.pipe(missing_count)  # series
df.pipe(total_number_missing)  # 값


# In[32]:


# 열 재구성 : 데이터프레임의 열 순서를 변경
df = titanic.loc[0:4, 'survived':'age']
print(df)

# 열의 순서를 변경 : 칼럼명을 sort해서 기존의 df에 적용
df_sort = df[sorted(df.columns.values)]
df_sort


# In[40]:


df_sort = df[list(reversed(df.columns.values))]
df_sort


# In[33]:


df[['age','pclass','sex','survived']]


# In[41]:


# 주가데이터 읽어옴
df = pd.read_excel('dataset/주가데이터.xlsx')
df.info()


# In[43]:


df.head()


# In[46]:


# df['연월일'].astype('str').str.split('-').get(0)
# 연월일 칼럼을 문자로 변경, split()을 이용하여 년 월 일로 분리
df['연월일'] = df['연월일'].astype('str')
df.info()
dates = df['연월일'].str.split('-')
dates.head()


# In[50]:


## 시리즈객체의 문자열 리스트 인덱싱 : 시리즈.str.get(인덱스)
dates.str.get(2)
df['연'] = dates.str.get(0)
df['월'] = dates.str.get(1)
df['일'] = dates.str.get(2)
df.head()


# In[51]:


# 나이가 10세 미만이고 여성인 승객의 자료를 추출
# age, class, fare, sex 칼럼만 추출
df = titanic.loc[(titanic.age <10) & (titanic.sex == 'female'),
                 ['age','class','fare','sex']]
df.head()


# In[53]:


# 나이가 10세 미만이거나 60세 이상인 승객의 age, pclass, fare 칼럼 추출
# sibsp -> 동승한 형제 또는 배우자의 수 3 또는 4 또는 5인 승객의 모든 자료 추출
df = titanic.loc[(titanic.age < 10) | (titanic.age >= 60),
                ['age','pclass','fare']]
df.head()

df_sib = titanic.loc[(titanic.sibsp==3)|(titanic.sibsp==4)|(titanic.sibsp==5),:]
df_sib.head()


# In[54]:


# df.isin([])  # list중에 해당하는 값이 존재하면 True
df_sib = titanic.loc[titanic['sibsp'].isin([3,4,5]),:]
df_sib.head()


# In[55]:


# 남북한발전전력량을 읽어서 Nan을 처리 : 2010년 ~ 2016년까지의 자료만
# '-'도 처리
# 년도를 인덱스로 변환
# 남한과 북한의 합계 데이터만 추출
# 년도별 남한과 북한의 발전량을 그래프로 그려보세요
df = pd.read_excel('dataset/남북한발전전력량.xlsx')
df.d


# In[ ]:




