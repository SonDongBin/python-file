#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# 딕셔너리 다루기 선언은 {키:값, ...}, 접근은 dick[키]
dict_a = {
    'name' : '7D 건조 망고',
    'type' : '당절임',
    'ingredient' : ['망고','설탕','메타중아황산나트륨','치자황색소'],
    'origin' : '필리핀'
}


# In[ ]:


print(dict_a)
print(dict_a['name'])
print(dict_a['ingredient'])
print(dict_a['ingredient'][0])


# In[ ]:


print(dict_a.keys()) # 딕셔너리의 키(key) 만 출력
print(dict_a.values()) # 딕셔너리의 value 만 출력
# print(dict_a[1]) # 오류발생, 키로만 접근 가능
print(dict_a['name'],dict_a['type'])


# In[ ]:


# dictionary에 새로운 키와 값을 추가 : dict[새로운키] = 값
dict_a['price'] = 5000
dict_a


# In[ ]:


# dictonary의 키 값을 제거 : del dict[키]
del dict_a['price']
dict_a


# In[ ]:


# list 초기화 list_a = []
# dict 초기화 dict_a = {}
# in 연산자를 활용하여 키가 dict에 있는지 확인 가능
print('price' in dict_a) # False
print('name' in dict_a) # True


# In[ ]:


# get(키) -> 값을 돌려줌 : 함수를 활용하여 존재하는지 확인
print(dict_a.get('price')) # None
print(dict_a.get('name'))  # '7D 건조 망고'


# In[ ]:


# for문을 활용하여 값을 출력 : 딕셔너리의 키를 가져옴
for key in dict_a:
    print("dict_a['{}'] : {}".format(key, dict_a[key]))


# In[ ]:


# for문을 활용하여 값을 출력 : 딕셔너리의 키와 값을 가져옴
for key, value in dict_a.items():
    print("dict_a['{}'] : {}".format(key, value))


# In[6]:


# 이름과 정수를 입력 받아 이름을 키로 정수를 값으로 하는
# student 딕셔너리를 작성
# 이름에 'q'가 입력되면 입력 종료
# 입력된 자료 출력
# 입력한 학생의 인원수와 평균 출력
# 검색할 이름을 입력받아 자료에 있는지 확인 후 자료의 성적을 출력
student = {}
while True :
    # 이름과 정수 입력
    # 입력된 문자열을 이름과 점수로 분리 -> 리스트
    # 입력된 이름이 'q'이면 입력 종료
    # 아니면 점수를 int()로 변환 후 이름을 키로 점수를 값으로 저장
    input_data = input('이름 점수 입력 > ').split()
    if input_data[0] == 'q':
        break
    name = input_data[0]
    score = int(input_data[1])
    student[name] = score


# In[ ]:



# 반복문을 활용하여 입력된 자료를 이름과 성적으로 출력
# 학생의 인원수와 성적의 합을 구한 후 평균 구하기
# 검색할 이름 입력
# 검색하고자 하는 이름이 student에 있으면 성적 출력, 아니면 '자료없음' 출력
s_sum = 0
for key in student:
print("{} : {}".format(key, student[key]))
s_sum += student[key]
print("인원 : {} , 평균 : {}".format(len(key),s_sum/len(key)))

input_name = input('검색할 이름 입력 > ')
if input_name in student :
print ("{} : {}".format(input_name,student[input_name]))
else :
print("자료없음")


# In[7]:


for key in student:
    print("{} : {}".format(key, student[key]))
print("인원수 : {}, 합계 : {}, 평균 : {:3.2f}".format(len(student),
                                               sum(student.values()),
                                               sum(student.values())/len(student)))
s_name = input("검색할 이름 입력 : ")
s_score = student.get(s_name)
if s_score == None:
    print('자료없음')
else:
    print("{}의 점수는 {}".format(s_name, s_score))


# In[12]:


# 이름과 국어, 영어, 수학 점수를 입력받아 student에 저장
student = {}
while True :
    name = input('이름 입력 > ')
    if name == 'q':
        break
    while True:
        input_score = input("국어 영어 수학 점수 입력 >").split()
        if len(input_score) == 3:
            break
            
    score = []
    for value in input_score: # 3과목의 점수를 score 리스트에 푸가
        score.append(int(value))
    student[name] = score


# In[13]:


# 각 학생의 총점, 과목 점수, 평균을 출력
print("이름 : 국어\t영어\t수학\t총점\t평균")
for key in student:
    print(key, end=' : ')
    for score in student[key]:
        print(score,end='\t')
    print("{}\t {}".format(sum(student[key]), sum(student[key])/3))
# 검색할 이름을 입력받아 학생의 총점, 평균 출력
s_name = input("검색할 이름 : ")
s_score = student.get(s_name)
if s_score:
    print("{} : {}, {}".format(s_name,sum(s_score),sum(s_score)/len(s_score)))


# In[14]:


# 홍길동의 국어 점수를 80으로 수정
student['홍길동'][0] = 80


# In[16]:


# 연습문제 3, 172p
numbers = [1,2,6,8,4,3,2,1,9,5,4,9,7,2,1,3,5,4,8,9,7,2,3]
# 1을 키로 나온 갯수를 값으로, 2의 갯수
# {1:3, 2:,3: ...}
# nembers에서 값을 가져옴
# 값이 dict에 키로 존쟇면 키의 값에 1을 더함
# 값이 dict의 키에 없으면 키와 1을 추가
counter = {}
for number in numbers:
    if number in counter.keys():
        counter[number] += 1 #기존의 값에 1을 더해서 저장
    else:
        counter[number] = 1 #새로 생성
# 결과 출력
print(counter)


# In[18]:


# range(start, stop, step) : range(5) -> 0~4까지, range(1,5) -> 1에서 4까지
# range(0,5,2) -> 0에서 4까지 2씩 증가
list_a = [2,3,4,5,6,7]
for item in list_a:
    print(item)
print()
#range사용
for idx in range(len(list_a)):
    print(list_a[idx])
print()

for r_idx in reversed(range(len(list_a))):
    print(list_a[r_idx])
    
list_a.sort(reverse=True) # 자료를 정렬, 기존 자료 변경
print(list_a)
list_a.reverse()
list_a


# In[20]:


# while 시간을 기준으로 반복문 작성
import time
count = 0
target_time = time.time() + 3 #현재 시간 반환
while time.time() < target_time:
    count += 1
print("3초 동안 {}횟수 실행".format(count))


# In[24]:


# 두 수를 입력 받아 두 수 사이의 3의 배수의 합과 5의 배수의 합을 구하세요
# range() 함수를 사용하세요
# 두 수는 포함
num1, num2 = input("두 수 입력 :").split()
num1 = int(num1)
num2 = int(num2)
if num1 > num2:
    num1,num2 = num2,num1
total = 0
for num in range(num1,num2+1):
    if num % 3 == 0:
        total += num
print("{}부터 {}까지 3의 배수의 합은 {}".format(num1,num2, total))
print("{}부터 {}까지 3씩 증가하는 수의 합은 {}".format(num1,num2,
                                      sum(range(num1,num2+1,3))))
total = 0
for num in range(num1,num2+1):
    if num % 5 == 0:
        total += num
print("{}부터 {}까지 5의 배수의 합은 {}".format(num1,num2, total))
print("{}부터 {}까지 5씩 증가하는 수의 합은 {}".format(num1,num2,
                                      sum(range(num1,num2+1,5))))


# In[27]:


# 문자열, 리스트, 딕셔너리와 관련된 함수
# 리스트 : sum(list), min(list), max(list), reversed(list)
list_a = [1,2,3,4,5]
# list_reversed = reversed(list_a)
list_reversed = list(reversed(list_a)) # list_reversed[5,4,3,2,1]

print("list_a :", list_a)
print("list_reversed :", list_reversed)
# print("list_reversed :", list(list_reversed))

for i in list_reversed:
    print("111", i)
for i in list_reversed:
    print("222", i)


# In[29]:


list_a = [4,5,6,7,8,9]
for num in list_a:  #list의 값을 가져옴
    print(num)
for idx in range(len(list_a)):  #list의 index를 가져옴
    print(idx,list_a[idx])
# list의 인덱스와 값을 같이 가져옴 -> enumerate(리스트)
for idx, value in enumerate(list_a):  #딕셔너리는 딕셔너리.item() 키와 값
    print("{}번째 값 : {}".format(idx,value))


# # 리스트에 적용 가능한 함수 : max(리스트), min(리스트),
# #     sum(리스트), enumerate(리스트), reversed(리스트)
# #     list.sort(), list.reversed() -> 해당 오브젝트를 변경
# # 딕셔너리 오브젝트에 관련된 함수 : dict.key(), dict.values(), dict.items()
# # for key in dict : -> 딕셔너리의 키를 가져옴
# # 리스트는 인덱스로 데이터 접근 : 리스트[인덱스], 리스트[start : stop]
# # 딕셔너리는 키로 데이터 접근 : 딕셔너리[키]
# # len(), type(), range()

# In[31]:


# 리스트 내포 [ 처리문장  ]
# 0 부터 20까지 2씩 증가된 숫자의 제곱을 구해서 리스트에 저장
list_b = []
for num in range(2,20,2):
    list_b.append(num *num)
print(list_b)
                  
list_c = [num*num for num in range(0,20,2)]
print(list_c)


# In[36]:


# 1부터 100까지 3의 배수의 합을 구하세요
print(sum[i for i in range(1,100) if i % 3 == 0])
list_3 = []
for i in range(1,100):
    if i % 3 == 0:
        list_3.append(i)
sum(list_3)


# In[34]:


list_c = [str(num) for num in range(0,20,2)]
print(list_c)

# 리스트를 문자열러 join -> 문자열, join)문자열 리스트) -> 문자열
print('--'.join(['a','b','c']))

print('*'.join(list_c))
list_str = '--'.join(list_c)
print(list_str)
list_split = list_str.split('--')
list_split


# In[ ]:




