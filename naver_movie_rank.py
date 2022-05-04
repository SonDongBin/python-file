#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 네이버 영화 순위, 제목, 포인트 검색 출력
from urllib import request
from bs4 import BeautifulSoup


# In[2]:


url = 'https://movie.naver.com/movie/sdb/rank/rmovie.naver?sel=cur&date=20220503'

target = request.urlopen(url) # url open

soup = BeautifulSoup(target.read(), 'html.parser') # html 태그로 분리
soup


# In[4]:


movie_title = []
movie_rank = []

for line in soup.find_all('tr'):  # [<tr> ~ </tr>, ...]
    title = line.find('div', class_='tit5') # <div class='tit5'> </div>
    if title:
        movie_title.append(title.get_text().strip('\n'))
    point = line.find('td', class_='point')  # <td class='tit5'> </td>
    if point:
        movie_rank.append(point.get_text())
        
for i, (title, point) in enumerate(zip(movie_title, movie_rank)):
    print(i+1, ' : ',title, point)


# In[ ]:




