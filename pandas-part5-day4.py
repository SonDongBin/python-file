#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Nan을 처리하는 함수 -> dropna(), fillna()
# Nan이 아닌 값을 제거하거나 대치하고자 할때
# 제거하고자 하는 값을 Nan으로 대체후 dropna(), fillna() 처리
import pandas as pd

df= pd.read_excel('./dataset/남북한발전전력량.xlsx')
df.head()


# In[2]:


# '-'를 Nan으로 변경 후 처리
import numpy as np
df.replace('-',np.nan, inplace=True)
df


# In[6]:


# 중복 데이터를 갖는 데이터프레임 만들기
df = pd.DataFrame({'c1':['a', 'a', 'b', 'a', 'b'],
                  'c2':[1, 1, 1, 2, 2],
                  'c3':[1, 1, 2, 2, 2]})
df


# In[9]:


print(df.duplicated())  # duplicated() 중복 여부 반환 : True, False
print(df['c1'].duplicated())
print(df[['c2','c3']].duplicated())


# In[10]:


# 중복 데이터인 경우 삭제 : drop_duplicates()
print(df.drop_duplicates())  # 행의 모든 값이 중복인 경우 삭제
df.drop_duplicates(subset=['c2','c3'])


# In[ ]:


# Nan 데이터 처리 : dropna(), fillna()
# 중복 데이터 처리 : duplicated(), drop_duplicates()


# In[11]:


# auto-mpg.csv 파일을 가져옴
df = pd.read_csv('./dataset/auto-mpg.csv', header=None)

# column 명 지정
df.columns = ['mpg','cylinders','displacement','horsepower','weight',
              'acceleration','model year','origin','name']
df.head()


# In[12]:


# 단위 표준화 : mpg(mile per gallon) -> kpl(kilometer per liter)
# 1 mpg = 0.425km/l
df['kpl'] = (df['mpg'] * 0.425).round(2)
df.head()


# In[16]:


print(df['horsepower'].head())
# df['horsepower'].astype('float')
df['horsepower'].unique()  # '?' 검색됨

# '?' -> Nan을 변경
df['horsepower'].replace('?',np.nan, inplace=True)


# In[17]:


print(df['horsepower'].unique())
df['horsepower'] = df['horsepower'].astype('float')


# In[19]:


# df['horsepower'].dropna(inplace=True)
df.dropna(subset=['horsepower'], axis=0, inplace=True)


# In[20]:


df.horsepower.unique()


# In[25]:


# origin 칼럼의 데이터 타입과 값, unique()
df.origin.unique()  # 1:USA, 2: EU, 3:JPN

df.origin.replace({1:'USA', 2:'EU', 3:'JPN'}, inplace=True)
print(df.origin.unique(), df.origin.dtype)
# data type은 object -> category 타입으로 변경
df.origin = df.origin.astype('category')
print(df.origin.unique(), df.origin.dtype)

# data type은 category -> object 타입으로 변경
df.origin = df.origin.astype('object')
print(df.origin.unique(), df.origin.dtype)


# In[26]:


# "model year" -> 정수형의 category로 변경
df['model year'].unique()
df['model year'] = df['model year'].astype('category')
df['model year'].sample(10)


# In[ ]:


# auto-mpg.csv 파일을 읽어와서 df을 생성
# 칼럼명 부여
# horsepower 칼럼을 float 형으로 형 변환
# horsepower 에 이상한 값이 있으면 제거
df = pd.read_csv('dataset/auto-mpg.csv',header=None)
df.columns = ['mpg','cylinders','displacement','horsepower','weight',
              'acceleration','model year','origin','name']


# In[35]:


df['horsepower'].unique()
df['horsepower'].replace('?',np.nan,inplace=True)
df.dropna(subset=['horsepower'], axis=0, inplace=True)


# In[37]:


df.horsepower = df.horsepower.astype('float')
df.horsepower


# In[42]:


# horsepower 칼럼의 값을 구간으로 나누어 봅니다
# bins 나누고자 하는 구간의 개수
count, bin_label = np.histogram(df.horsepower, bins=3)
# [경계값, .. , ]

bin_names = ['저출력', '보통출력', '고출력']
df['hp_bin'] = pd.cut(x = df['horsepower'],
                     bins = bin_label,
                     labels = bin_names,
                     include_lowest = True)


# In[45]:


df.sample(5)


# In[50]:


# sklearn 의 preprocessing 를 활용한 one_hot_encoding
from sklearn import preprocessing as pre

# 전처리를 위한 encoder 생성
label_encoder = pre.LabelEncoder()  # label_encoder 생성
onehot_encoder = pre.OneHotEncoder()  # one hot encoder 생성

# label_encoder 로 문자형 범주를 숫자형 범주로 변경
onehot_label = label_encoder.fit_transform(df['hp_bin'])
print(onehot_label)

# 2차원으로 변경 -> ( 열이 1개인 2차원으로 변경, 행렬로 변경)
onehot_reshape = onehot_label.reshape(len(onehot_label), 1)
onehot_reshape[:10, :]


# In[51]:


# 희소 행렬로 변경
onehot_fitted = onehot_encoder.fit_transform(onehot_reshape)
print(onehot_fitted)


# In[52]:


# 정규화 -> 값의 범위가 0~1, 또는 -1~1 사이의 값으로 변경
df.horsepower.head()
df_1 = df.copy()


# In[53]:


df_1.horsepower = df_1.horsepower / abs(df_1.horsepower.max())  # 정규화 1
df_1.horsepower.head()


# In[54]:


# 정규화 방법 2 : (최대값 - 최소값)으로 나누어 만드는 방법
df.horsepower = (df.horsepower - df.horsepower.min()) /     (df.horsepower.max() - df.horsepower.min())


# In[55]:


df.horsepower.head(10)


# In[59]:


# 시계열 데이터
df = pd.read_csv('./dataset/stock-data.csv')
df.head()
df.info()
df.describe()


# In[61]:


# Date 칼럼의 값을 object에서 datetime 형식으로 변경
df['New_Date'] = pd.to_datetime(df['Date'])
df.info()


# In[62]:


# df.drop(columns=['New Date'], inplace=True)


# In[63]:


df.info()


# In[64]:


# New_Date 를 인덱스로, Date 칼럼을 삭제
df.set_index('New_Date', inplace=True)
df.head()


# In[65]:


df.drop(columns=['Date'], inplace=True)
df.head()


# In[67]:


# 칼럼명을 New_Date -> Date로 변경
# index reset, 칼럼명 변경
# index set
df.reset_index(inplace=True)
df.rename(columns={'New_Date':'Date'}, inplace=True)
df.set_index('Date', inplace=True)
df.head()


# In[69]:


# stock-data.csv 파일을 읽어서 df 로 변환
# date -> New_date (datetime 으로 변경)
df = pd.read_csv('dataset/stock-data.csv')
df['New_Date'] = pd.to_datetime(df['Date'])
df.head()


# In[70]:


# New_Date -> datetime : dt.year, dt.month, dt.day
df['Year'] = df['New_Date'].dt.year
df['Month'] = df['New_Date'].dt.month
df['Day'] = df['New_Date'].dt.day
df.head()


# In[71]:


df['New_Date'].dt.to_period(freq='M')


# In[ ]:




