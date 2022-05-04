#!/usr/bin/env python
# coding: utf-8

# In[2]:


# api를 활용한 자료 검색 -> 네이버의 파파고를 활용하여 번역 프로그램 작성
import requests


# In[3]:


text='''Yesterday
All my troubles seemed so far away
Now it looks as though they're here to stay
Oh, I believe in yesterday
Suddenly
I'm not half the man I used to be
There's a shadow hanging over me
Oh, yesterday came suddenly
Why she had to go, I don't know
She wouldn't say
I said something wrong
Now I long for yesterday
Yesterday
Love was such an easy game to play
Now I need a place to hide away
Oh, I believe in yesterday
Why she'''


# In[7]:


url = 'https://openapi.naver.com/v1/papago/n2mt'
headers = { 'X-Naver-Client-Id' : 'N2gZjiBaSy2jahJnKeYJ',
          'X-Naver-Client-Secret' : 'u47MGbwDLg'}
params = {"source" : 'en', 'target' : 'ko', 'text':text }


# In[12]:


response = requests.post(url, headers=headers, data=params)
print(type(response.text), response.text) # 문자열로 반환
# str을 json 형식으로 변경 -> 딕셔너리와 유사, 같은 방법으로 처리
result = response.json()
target = result['message']['result']['translatedText']
print(target)


# In[ ]:




