#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# datetime : 날짜, 시간 관련 모듈
import datetime as dt

print("현재시간 출력", dt.datetime.now())


# In[ ]:


import datetime as dt

print("현재 시간 출력하기")
now = dt.datetime.now()
print(now.year, "년")
print(now.month, "월")
print(now.day, "일")
print(now.hour, "시")
print(now.minute, "분")
print(now.second, "초")
print()

print("시간을 포멧에 맞춰 출력하기")
output_a = now.strftime("%Y.%m.%d %H:%M:%S")
output_b = "{}년 {}월 {}일 {}시 {}분 {}초".format(now.year,                                           now.month,                                           now.day,                                           now.hour,                                           now.minute,                                           now.second)
output_c = now.strftime("%Y{} %m{} %d{} %H{} %M{} %S{}").format(*"년월일시분초")
print(output_a)
print(output_b)
print(output_c)


# In[ ]:


import time

target = time.time() + 1
while time.time() < target:
    print("대기상태",time.time())
    


# In[ ]:


# urllib 모듈 : 웹의 데이터 연결
from urllib import request

target = request.urlopen("https://google.com")
print(target.read()) # <html> tag 형식으로 변경


# In[3]:


get_ipython().system('pip install beautifulsoup4')


# In[11]:


# url 데이터 다루기 위해 bs4의 BeautifulSoup 을 import
from bs4 import BeautifulSoup


# In[12]:


html_doc = """<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""


# In[13]:


html_doc


# In[14]:


soup = BeautifulSoup(html_doc, 'html.parser')
soup


# In[18]:


# 각 tag 의 데이터 검색
print(soup.title)
print(soup.title.name)  # tag의 이름
print(soup.title.parent) # 부모의 tag
print(soup.title.string) # title의 데이터


# In[22]:


print(soup.p)
print(soup.p['class']) # 하나만 검색
print()
# 모든 p 태그 검색
print(soup.find_all('p')) # 'p' 태그 검색 후 리스트로 반환
print()
print(soup.find('a')) # 처음 나오는 a 태그 하나만 검색
print()
# id = 'link2' 를 검색
print(soup.find(id='link2'))


# In[23]:


for link in soup.find_all('a'):
    print(link.get('href'))


# In[24]:


soup.get_text()


# In[29]:


tag = BeautifulSoup('<b id="boldest">bold</b>', 'html.parser').b
print(tag['id'])
print(tag.text)


# In[26]:


tag.attrs


# In[28]:


tag['another-attribute'] = 1
tag.attrs


# In[ ]:


# 설치가 안된 경우 실행
# !pip install flask


# In[30]:


# 웹 프레임워크 : flask
from flask import Flask


# In[31]:


# 함수 데코레이터
# @ 로 시작하면 데코레이터
def test(function):
    def wrapper():
        print("wrapper 시작")
        function()
        print("wrapper end")
    return wrapper
# 데코레이터 함수 생성
@test
def hello():
    print("hello")
    
hello() # 함수 호출


# In[32]:


hello()


# In[ ]:




