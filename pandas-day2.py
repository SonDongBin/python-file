#!/usr/bin/env python
# coding: utf-8

# In[2]:


# 시리즈 연산 : 시리즈 연산식 숫자 -> 시리즈의 각 원소에 숫자 연산
import pandas as pd

sr = {'국어':100, '영어':90, '수학':80}
sr = pd.Series(sr)


# In[3]:


print("before {} : after {}".format(sr, sr + 10))
print("before {} : after {}".format(sr, sr - 10))
print("before {} : after {}".format(sr, sr * 10))
print("before {} : after {}".format(sr, sr / 10))


# In[5]:


# 시리즈 사칙연산(+, -, *, /) 시리즈
sr1 = pd.Series({'국어':100, '영어':90, '수학':80})
sr2 = pd.Series({'국어':80, '영어':70, '수학':90})

sr = sr1 + sr2
sr


# In[6]:


# 시리즈 연산시 인덱스가 없거나 Nan값이 연산에 사용되면 결과는 Nan
import numpy as np
sr1 = pd.Series({'국어':np.nan, '영어':90, '수학':80})
sr2 = pd.Series({'국어':80, '영어':70, '수학':90, '과학':100})
sr1 + sr2


# In[8]:


# 연산 메소드 : 시리즈.add(시리즈1), sub(), mul(), div()
sr_add = sr1.add(sr2, fill_value=0)  # Nan 데이터를 0으로 대치
sr_sub = sr1.sub(sr2, fill_value=0)
sr_mul = sr1.mul(sr2, fill_value=0)
sr_div = sr1.div(sr2, fill_value=0)
print("{}, {}, {}, {}".format(sr_add,sr_sub,sr_mul,sr_div))


# In[13]:


import seaborn as sns

titanic = sns.load_dataset('titanic')
titanic.head()
df = titanic.loc[ :, ['age', 'fare']]
print(df.head())  # 처음부터 5개만 보여줌, tail() 뒤에서 5개만 보여줌
df.tail()
print(sns.get_dataset_names())


# In[15]:


titanic.info()


# In[17]:


df + 10


# In[18]:


# 외부 파일을 읽어서 데이터프레임 생성
# pd.read_csv(파일명) -> ',' 또는 구분자로 분리된 자료를 읽어옴
file_path = './dataset/read_csv_sample.csv'
df = pd.read_csv(file_path, header=None) # header 지정하지 않음
# df = pd.read_csv("./dataset/read_csv_sample.csv")
df


# In[19]:


df = pd.read_csv(file_path) # 0 자리의 자료를 칼럼으로 인식
df


# In[20]:


df = pd.read_csv(file_path, index_col='c0')  # index 칼럼 지정
df


# In[27]:


# excel 파일 read : read_excel(파일명, 옵션)
file_path = './dataset/남북한발전전력량.xlsx'
df = pd.read_excel(file_path) #, header=None)  df.to_excel(파일명)
df.head()
df.to_excel("sample.xlsx",index=False)


# In[28]:


# json 파일 : pd.read_json
file_path = './dataset/read_json_sample.json'
df = pd.read_json(file_path)
df


# In[31]:


# html file read : pd.read_html
file_path = './dataset/sample.html'
tables = pd.read_html(file_path)
tables


# In[36]:


df = tables[1]
df.reset_index(inplace=True)   # name을 인덱스로 설정
df.set_index('name', inplace=True)
df


# In[37]:


# 여러개의 데이터프레임을 하나의 excel 파일로 저장하기
data1 = {'name':['Jerry', 'Riah', 'Paul'],
        'algol':['A','A+','B'],
        'basic':['A+','F','B'],
        'c++':['B','c+','A']}
data2 = {'c0': [1,2,3],
        'c1': [4,5,6],
        'c2': [7,8,9],
        'c3': [10,11,12]}
df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)


# In[38]:


df1.set_index('name', inplace=True)
df2.set_index('c0', inplace=True)


# In[42]:


df1
df2
# ./dataset/df_excel.xlsx 로 저장
wp = pd.ExcelWriter('./dataset/df_excel.xlsx')  # fp = open(파일명,모드)
df1.to_excel(wp, sheet_name='sheet1')
df2.to_excel(wp, sheet_name='sheet2')
df.to_excel(wp, sheet_name='sheet3')
wp.save()   # fp.close() 비슷


# In[ ]:




