#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 데이터프레임 합치기 : pd.concat(데이터프레임 리스트)
import pandas as pd

df1 = pd.DataFrame({'a': ['a0', 'a1', 'a2', 'a3'],
                    'b': ['b0', 'b1', 'b2', 'b3'],
                    'c': ['c0', 'c1', 'c2', 'c3']},
                    index=[0, 1, 2, 3])
 
df2 = pd.DataFrame({'a': ['a2', 'a3', 'a4', 'a5'],
                    'b': ['b2', 'b3', 'b4', 'b5'],
                    'c': ['c2', 'c3', 'c4', 'c5'],
                    'd': ['d2', 'd3', 'd4', 'd5']},
                    index=[2, 3, 4, 5])


# In[3]:


print(df1)
print(df2)


# In[5]:


print(pd.concat([df1,df2]))  # 행으로 데이터 프레임 연결하기
print(pd.concat([df1,df2], ignore_index=True))  # 기존의 인덱스 무시


# In[6]:


pd.concat([df1,df2], axis=1)  # 칼럼으로 연결하기


# In[7]:


pd.concat([df1,df2],axis=1, join='inner') # 인덱스가 같은 행만 조인


# In[8]:


pd.concat([df1,df2], join='inner')  # 칼럼명 같은 경우만 조인


# In[9]:


# 데이터프레임과 시리즈 연결
sr1 = pd.Series(['e0', 'e1', 'e2', 'e3'], name='e')
sr2 = pd.Series(['f0', 'f1', 'f2'], name='f', index=[3, 4, 5])
sr3 = pd.Series(['g0', 'g1', 'g2', 'g3'], name='g')


# In[13]:


sr3


# In[16]:


print(pd.concat([df1,sr1], axis=1))  # df1과 시리즈 sr1을 칼럼으로 연결
print()
print(pd.concat([df2,sr2], axis=0, sort=True))
print(pd.concat([df2,sr2], axis=1, sort=True))


# In[18]:


# sr, df, join ='outer' -> 'inner', axis=0 (아래로 연결), axis=1 (옆으로 연결)
# pd.concat([])
pd.concat([sr1,sr2,sr3], axis=1)


# In[37]:


# pd.merge( left, right, how=, on=)
df1 = pd.read_excel('dataset/stock_price.xlsx')
df2 = pd.read_excel('dataset/stock_valuation.xlsx')
df1.head()  # df -> stock_name -> value -> price
df2.head()  # df -> name -> eps-bps-per-pdr


# In[23]:


# how='inner' 두 개의 데이터프레임에 칼럼명이 같은 칼럼명은
# 두 프레임의 id 의 값이 같은 자료만 추출
merge_inner = pd.merge(df1,df2)
merge_inner


# In[24]:


merge_inner = pd.merge(df1,df2, how='left')  # df1의 내용은 모두 출력
merge_inner


# In[25]:


pd.merge(df1,df2, how='outer')  # how='right' : df2는 모두 추출


# In[26]:


pd.merge(df1,df2, how='inner', on='id')  # on='칼럼명', 특정 칼럼의 값을 기준


# In[27]:


# 칼럼명을 다르게 merge
pd.merge(df1,df2,how='left', left_on='stock_name', right_on='name')


# In[40]:


# price가 50000미만인 자료의 id,name,vlaue,price,eps,bps,per를 추출
# 1, df1에서 price가 50000미만인 자료의 id,vlaue,price만 추출
# 2, df1과 df2 (name,eps,bps,per만 가져와서) merge
price = df1.loc[df1['price']<50000,['id','value','price']]
print(price)
df_2 = df2.loc[:,['id','name','eps','bps','per']]
df_2

pd.merge(price, df_2, how='left')


# In[ ]:


# df1.join(df2, how=, key)


# In[41]:


import seaborn as sns
titanic = sns.load_dataset('titanic')
df = titanic


# In[ ]:


# 그룹연산 실행 순서
# 데이터를 특정 조건으로 분할
# 분할된 데이터를 집계, 변환, 필터링
# 2단계에서 실행된 결과를 결합


# In[42]:


print(df['class'].unique())
# df.groupby(칼럼명)
grouped = df.groupby('class')


# In[43]:


for key, group in grouped:
    print("key : ", key)
    print(group.head())


# In[44]:


grouped.mean()  # 그룹별 각 칼럼의 평균


# In[45]:


# First 클래스의 승객만 추출
grouped.get_group('First')


# In[46]:


# 'class'로 그룹을 지은 뒤 각 클래스별 가장 많은 나이를 추출
class_group = df.groupby('class')
class_group['age'].max()


# In[47]:


# class, sex를 기준으로 그룹을 짓고 각 그룹의 자료를 출력
# 멀티인덱스 ( , )
class_sex = df.groupby(['class','sex'])
for key, group in class_sex:
    print("key : ", key)
    print(" number : ", len(group))
    print(group.head())


# In[48]:


# 각 클래스별 성별, 나이, 요금, 생존율의 평균
class_sex[['age', 'fare', 'survived']].mean()


# In[50]:


# 3등석의 male의 자료만 추출
class_sex.get_group(('Third', 'male'))['age']


# In[71]:


# auto-mpg.csv 파일을 origin을 1: USA, 2: EU, 3: JPN
# 제조 국가 별로 mpg의 평균
# USA의 weight이 가장 적은 값을 추출
df = pd.read_csv('dataset/auto-mpg.csv',header=None)
df.columns =  ['mpg','cylinders','displacement','horsepower','weight',
              'acceleration','model year','origin','name']
df.origin.replace({1:'USA', 2:'EU', 3:'JPN'}, inplace=True)
df.origin.unique()
grouped = df.groupby('origin')
print(grouped['mpg'].mean())
grouped.get_group('USA')['weight'].min()


# In[73]:


# 그룹 메서드 -> grouped.칼럼.그룹함수()
titanic = sns.load_dataset('titanic')
df = titanic.loc[ :, ['age','sex','class','fare','survived']]


# In[74]:


grouped = df.groupby('class')
grouped.fare.std()


# In[75]:


# 매핑함수를 여러개
def min_max(x):
    return x.max() - x.min()

grouped.agg([min_max])


# In[79]:


grouped[['age','fare']].agg(['min','max','std'])
# 모든 칼럼에 min, max 함수를 적용하여 값을 구함


# In[80]:


grouped.agg({'age':[min,max], 'fare':['mean']})  # 칼럼별로 함수 적용


# In[82]:


df.groupby('sex').agg(['min','max','sum','count'])


# In[94]:


df = titanic.loc[ :, ['age']]
# grouped = df.groupby('class')
df.age.fillna(0,inplace=True)


# In[95]:


df.age.unique()


# In[ ]:





# In[98]:


# 그룹 연산 데이터 변환 : (값 - 편균(키))/표준편차(키)
age_mean = grouped.age.mean()
print(age_mean)

age_std = grouped.age.std()
print(age_std)

for key, group in grouped:
    group_score = (group['age'] - age_mean.loc[key]) / age_std.loc[key]
    print('key : ', key)
    print(group_score.head(3))


# In[102]:


# transform() : 그룹의 각 원소에 그룹함수를 적용
def group_score(x):
    return (x - x.mean())/x.std()

age_score = grouped.age.transform(group_score)
print(age_score.loc[[1,9,0]])


# In[101]:


age_score = grouped.age.transform(lambda x : (x - x.mean())/x.std())
print(age_score.loc[[1,9,0]])


# In[103]:


# class, age, fare 칼럼을 가지고 와서 class로 그룹을 나누고
# 그룹별로 자신의 fare에 자기가 속한 그룹의 fare의 평균값을 뺀 값을 구하세요
# 1,9,0 인덱스를 가져와서 출력
df1 = titanic.loc[:, ['class','age','fare']]
df1_fare = df1.groupby('class').fare.transform(lambda x: x-x.mean())
df1_fare[[1,9,0]]


# In[105]:


# 그룹 객체 필터링 filter 함수 : 그룹객체.filter(조건식 함수)
df1_grouped = df1.groupby('class')
df1_result = df1_grouped.filter(lambda x: len(x) >= 200)
df1_result['class'].unique()


# In[106]:


# 평균 나이가 30보다 작은 그룹의 데이터만 출력
print(df1_grouped.filter(lambda x: x.age.mean() < 30))
df1_grouped.filter(lambda x: x.age.mean() < 30)['class'].unique()


# In[108]:


# 그룹 객체에 함수 매핑 : 그룹객체.apply(매핑함수)
df1_grouped.apply(lambda x: x.describe())


# In[109]:


df1_grouped.age.apply(lambda x: (x - x.mean())/x.std())


# In[110]:


age_filter = df1_grouped.apply(lambda x: x.age.mean()<30 )
for key in age_filter.index:
    if age_filter[key] == True:
        age_filter_df = df1_grouped.get_group(key)
        print(age_filter_df.head())


# In[115]:


# titanic 에서 'sex','age','class','fare','survived' 칼럼을 가져옴
df2 = titanic.loc[:,['sex','age','class','fare','survived']]
df2.head()
# 그룹을 멀티로 class, sex
df2_grouped = df2.groupby(['class','sex'])
gdf = df2_grouped.mean()
gdf


# In[116]:


gdf.loc[('First','female')]  # 처음 인덱스를 기준으로 추출(인덱스1, 인덱스2)


# In[117]:


# 두번째 인덱스를 기준으로 데이터를 검색 :
# 그룹객체.xs(그룹의 값, level=그룹명)
# sex == 'male'인 자료만 검색
gdf.xs('male', level='sex')


# In[120]:


# 피벗 : pivot_table()
df2

pd.pivot_table(df2,
              index = 'class',
              columns = 'sex',
               values = 'age',
              aggfunc = 'mean')


# In[122]:


pd.pivot_table(df2,
              index = 'class',
              columns = 'sex',
               values = ['age','fare'],
              aggfunc = ['mean', 'sum'])


# In[135]:


pdf = pd.pivot_table(df2,
              index = ['class','sex'],
              columns = ['survived'],
               values = ['age','fare'],
              aggfunc = ['mean', 'sum'])


# In[136]:


pdf.columns


# In[137]:


pdf


# In[131]:


# 'Firsr','female'의 정보 가져오기
pdf.xs(('First','female'))


# In[132]:


pdf.xs('male',level='sex')


# In[133]:


# 'First','male'의 정보만 추출 : pdf.xs(('First','male'),level=[0, 'sex'])
pdf.xs(('First','male'),level=[0, 'sex'])


# In[134]:


# mean 정보만
pdf.xs('mean', axis=1)


# In[138]:


pdf.xs(0,level='survived',axis=1)


# In[ ]:


# 데이터 전처리
# horsepower 숫자로 변경
# '?' -> Nan 으로 대체
df['horsepower'].replace('?',np.nan, inplace=True)
df.dropna(subset=['horsepower'], axis=0, inplace=True)
# Nan데이터 삭제
df['horsepower'] = df['horsepower']

