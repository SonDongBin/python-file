#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np

# arange() 함수를 이용하여 배열 생성
# ndim: 배열의 차수, shape: 3 * 5, dtype.name: 데이터 형식
# dtype.itemsize: 각 데이터의 저장 사이즈, size: 배열의 총 데이터 갯수
arr = np.arange(15)
print(arr, arr.ndim, arr.shape)
print(arr, arr.ndim) # arr.ndim 차원, array.shape 배열의 사이즈
arr2 = arr.reshape(3,5)  # 배열의 차수를 변경
print(arr2, arr2.ndim, arr2.shape)
print(arr.dtype.name, arr.dtype.itemsize, arr.size)


# In[5]:


a = np.arange(-5, 5, 0.5)
a.size
a.reshape(int(a.size/4), 4)


# In[7]:


b = np.array([1,2,3,4])
type(b)


# In[8]:


a_list = [[1,2,3],[4,5,6]]
print(a_list, type(a_list))


# In[9]:


a_arr = np.array(a_list)
print(a_arr, type(a_arr))


# In[10]:


# 1부터 100까지의 수를 리스트로 만든 후 5 * 4 * 5 의 배열로 변경
arr = np.array(list(range(1,101))).reshape(5,4,5)
arr.reshape(5*4*5)


# In[19]:


# 초기값을 부여하면서 배열 생성하기
# 초기값을 0으로
np.zeros(5)  # 1차원 배열 5인 -> 초기값이 0
np.zeros((2,3,5))  # 배열의 차원은 tuple로
np.zeros((5,2), dtype='i')  # 값을 정수형으로 사이즈는 32bit
np.zeros(5, dtype='U4')  # 값의 형식이 문자, NULL이 초기화 됨
np.zeros(5, dtype='i8')  # 64bit
np.zeros(5, dtype='f')  # float 32
np.ones(5, dtype='f')  # float 32, 1로 초기화
np.ones_like(np.zeros((5,2), dtype='i'), dtype='f')  # 기존 자료를 1로 초기화
np.empty((4,3))  # 빈 배열 생성 -> 값은 초기화 되어 있지 않음
# ones, zeros, empty, ones_like, zeros_like, empty_like


# In[21]:


x1 = np.array([1.0, 2.0, 3.0])   # (3,)
y1 = np.array([5.0, 10.0, 15.0])
x2 = np.array([[1.0, 2.0],[ 3.0, 4.0]])  # 2 * 1
y2 = np.array([[5.0,10.0],[15.0,20.0]]) 
z1 = np.array([-1.0, -2.0])
z2 = np.array([[5.0],[10.0],[15.0]])  # 3 * 1
print(x1.shape, z2.shape)


# In[23]:


print(x1 + y1)
print(x2 + y2)
print(x2 * y2)


# In[26]:


# 차수가 다른 배열 연산 : broadcast
print(x2 + z1)  # broadcast
print(x1 ** 2)
print(x1 >= 2)  # 조건 비교한 결과 False, True 반환


# In[28]:


print(x2.ndim, x2)
x2.flatten()  # (4, ) 1차원 배열로 바뀜


# In[35]:


# indexing, slicing, 반복처리
arr = np.arange(10) **2  # 0부터 9까지의 수를 제곱해서 배열로 생성
print(arr)
# 0, 1, 4, 9, ... => 4를 추출
print(arr[2])
# 3번째에서 6번째까지 자료 출력
print(arr[3:7])
# 0부터 2씩 증가시키면서 자료 출력
print(arr[0:-1:2])  
print(arr[ : : -1])  # 뒤에서 부터 추출

# for 문장을 사용하여 데이터 출력
for data in arr:
    print(data)


# In[45]:


# 1부터 20까지의 수를 1식 증가시키면서 배열 생성(5 * 4의 사이즈로)
arr = np.arange(1, 20+1, 1).reshape(5,4)
print(arr)  # 6[1,1]과 15[3,2]를 출력
print(arr[1,1], arr[3,2], arr[[1,3], [1,2]])  # array[행, 열]
print(arr[1:3, : ])  # 1행과 2행 모두 출력
print(arr[ : , -1])  # 마지막 열만 출력

arr[1, : ] = -arr[1, : ]
print(arr)
print(arr[ : :-1, : :-1])


# In[51]:


# np의 일밤함수 : np.array(), np.sin(a), cos, tanh, exp
np.sin(arr)
np.cos(arr)
np.tanh(arr)
np.exp(arr)

np.log(np.arange(0.01, 1, 0.05))  # np.log(arr)


# In[57]:


# maximun, minimum, sum, argmax
a1 = np.array([1,5,3])
a2 = np.array([3,4,5])
print(np.maximum(a1,a2))  # [3,5,5]
print(np.minimum(a1,a2))  # [1,4,3]
print(np.sum(a1))  # 9
print(np.argmax(a1))  # 큰 값이 위치한 위치 반환
print(np.argmin(a2))  # 작은 값이 위치한 위치 반환


# In[100]:


np.random.seed(0)

# random 함수
np.random.choice(100,5) # 0~100 사이 수 중에서 5개 선택
np.random.rand(2,3)  # 0에서 1 사이 수를 2 * 3으로 선택(총 6개의 수)
np.random.randn(2,3) # -무한대 에서 무한대 사이의 수를 정규분포 형태로 추출


# In[86]:


a = np.array([[0.1,0.8,0.2],[0.3,0.2,0.5],[0.9,0.5,0.3]])
np.argmax(a,axis=0)


# In[106]:


# 통계 함수 : count -> len(), 평균 mean(), 중간값 median(),
# 분산 var(), 표준편차 std(), 최대값 max(), 최소값 min(),
# 사분위수 percentile()
x = np.array([18,   5,  10,  23,  19,  -8,  10,   0,   0,   5,   2,  15,   8,
              2,   5,   4,  15,  -1,   4,  -7, -24,   7,   9,  -6,  23, -13])
print(len(x), np.mean(x))  # 개수, 평균
print(np.median(x), np.var(x), np.std(x), np.max(x))
print(np.min(x), np.percentile(x,25), np.percentile(x,75),
     np.percentile(x,100))


# In[171]:


# random coice 함수
np.random.choice(10,5, replace=False)


# In[173]:


# np.random.choice(5,10, p=[확률 배열]) -> np.arange(5)
# 0, 1, 2, 3, 4에 대해 선택 확률을 다르게 줌
np.random.choice(5,10, p=[ 0.1, 0, 0.3, 0.6, 0 ])
np.random.shuffle(x)


# In[174]:


x


# In[176]:


# np.random.randinit(low, high=None, size=None)
np.random.randint(10,size=10)
np.random.randint(10,30,size=10)
np.random.randint(10,30,size=(3,5))


# In[185]:


# 다음 행렬과 같은 배열이 있다.
# x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,
#               13, 14, 15, 16, 17, 18, 19, 20])

# 이 배열에서 3의 배수를 찾아라.
# 이 배열에서 4로 나누면 1이 남는 수를 찾아라.
# 이 배열에서 3으로 나누면 나누어지고 4로 나누면 1이 남는 수를 찾아라.
x = np.array(range(1,21))  # np.arange(1,21)

print(x[x % 3 == 0])
print(x[x % 4 == 1])

print(x[(x % 3 == 0) & (x % 4 == 1)])


# In[ ]:




