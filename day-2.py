#!/usr/bin/env python
# coding: utf-8

# In[5]:


# 키보드에서 문자를 입력받아 출력 하세요
input_str = input("문자 입력 > ")
print("입력받은 문자 : {}, 소문자로 변경 : {}, 대문자로 변경 : {}".     format(input_str, input_str.lower(), input_str.upper()))


# In[6]:


# 문자열의 함수 strip(), lstrip(), rstrip() -> 공백 제거
a_str = "   test 1234 abcd   "
print("strip : /{}/, rstrip : /{}/, lstrip : /{}/".     format(a_str.strip(), a_str.rstrip(), a_str.lstrip()))


# In[7]:


a_str.strip()[ : 4].isalnum()


# In[10]:


# find(문자), rfind(문자) -> 처음 나오는 문자의 인덱스 반환
print(a_str.find('te'))
a_str[ a_str.find('t') : a_str.rfind('t')+1 ]


# In[12]:


# 문자열과 in 연산자 : 문자 in 문자 -> 문자열에 문자가 존재하면 True
print('test' in a_str)
print('aa' in a_str)


# In[20]:


# split(구분자) -> 구분자를 기준으로 문자 나누기, 구분자가 없으면 공백
# list로 반환 [ , , ...]
a_str = "10 20 30 40 50"
print("/{}/, /{}/".format(a_str, a_str.split()))
b_str = "10,test,30,40,50,True"
b_str.split(',')


# In[22]:


'10' in b_str.split(',')


# In[26]:


print(b_str.split(',')[2:-1])
print(type(b_str.split(',')[2:-1]))
b_str.split(',')


# # 문자열 관련 함수 -> 문자열.함수명()
# # object명.함수명()
# # format(), upper(), lower()
# # find(), rfind() => 인덱스 반환
# # strip(), lstrip(), rstrip()
# # split(구분자) => list 반환
# # 값 in 배열, is00 -> Boolean 반환
# # 문자열[ start : end ] -> start포함, end는 미포함, -1 : 마지막 위치

# In[27]:


# Boolean -> ==, > , <, >=, <=, !=, and, or, not : True or False 반환
print(not 10 == 100)


# In[28]:


# if 표현식 : -> 표현식이 참이면 처리문장 실행
#    처리문장
#    ...
if 10==100:  # False -> if의 실행문 실행 안됨
    print('if 실행')
if True:
    print('True 실행')
    print('True 2행')
print('end')


# In[31]:


# 숫자를 키보드에서 입력받아 100보다 작으면 '100보다 작음'
# 100보다 크면 '100이상'으로 출력
# 1. 키보드에서 숫자 입력
input_num = input("숫자 입력 >")
# 2. 입력 받은 문자를 숫자로 형 변환
input_num = int(input_num)
# 3. 입력받은 숫자가 100보다 작은지 체크
if input_num < 100:
    print('\입력 받은 숫자는 {} : 100보다 작음'.format(input_num))
# 4. 입력받은 숫자가 100보다 크거나 같은지 체크
if input_num >= 100:
    print('입력된 숫자는 {} : 100이상 '.format(input_num))


# In[32]:


# 날짜/시간 관련된 기능을 가져옵니다
import datetime

# 현재 날짜/시간을 구합니다
now = datetime.datetime.now()

# 출력합니다
print("{}년 {}월 {}일 {}시 {}분 {}초".format(
    now.year,now.month,now.day,now.hour,now.minute,now.second))


# In[33]:


# 계절을 출력
if now.month >= 3 and now.month <= 5 :
    print("{}월은 봄입니다".format(now.month))
if 6<= now.month <=8:
    print("{}월은 여름입니다".format(now.month))
if 9<= now.month <=11:
    print("{}월은 가을입니다".format(now.month))
if now.month ==1 or now.month == 2 or now.month == 12:
    print("{}월은 겨울입니다".format(now.month))


# In[36]:


# 숫자를 입력받아 숫자가 짝수이면 '입력된 숫자 12는 짝수'
# 숫자를 입력받아 숫자가 홀수이면 '입력된 숫자 123은 홀수'
# 1. 숫자 입력 받음
input_number = input("정수 입력 > ")
# 2. 숫자가 짝수인지 확인 -> 2로 나눈 % 나머지값으로 확인 0이면 짝수
if int(input_number) % 2 == 0 :
    print("입력된 숫자 {} 는 짝수".format(input_number))
if int(input_number) % 2 != 0 :
    print("입력된 숫자 {} 는 홀수".format(input_number))
#      마지막 글자가 -> 0,2,4,6,8이면 짝수
if input_number[-1] == '0' or input_number[-1] =='2' or    input_number[-1] == '4' or input_number[-1] == '6' or    input_number[-1] == '8' :
        print("입력된 숫자 {} 는 짝수".format(input_number))
#      마지막 글자가 -> 1,3,5,7,9이면 홀수
if input_number[-1] == '1' or input_number[-1] =='3' or    input_number[-1] == '5' or input_number[-1] == '7' or    input_number[-1] == '9' :
        print("입력된 숫자 {} 는 홀수".format(input_number))
        
if input_number [-1] in "02468":
    print("입력된 숫자 {} 는 짝수".format(input_number))
if input_number [-1] in "13579":
    print("입력된 숫자 {} 는 홀수".format(input_number))


# In[37]:


if input_number [-1] in "02468":
    print("입력된 숫자 {} 는 짝수".format(input_number))
else:
    print("입력된 숫자 {} 는 홀수".format(input_number))


# In[38]:


if now.month >= 3 and now.month <= 5 :
    print("{}월은 봄입니다".format(now.month))
elif 6<= now.month <=8:
    print("{}월은 여름입니다".format(now.month))
elif 9<= now.month <=11:
    print("{}월은 가을입니다".format(now.month))
else:
    print("{}월은 겨울입니다".format(now.month))


# In[45]:


# 키보드에서 자료를 입력받아 숫자인지 확인후
input_data = input("자료를 입력 > ")
# 숫자이면 int형으로 변환한 후 3의 배수인지 확인
if not input_data.isalpha():
    if float(input_data) % 3 == 0:
        print("{}는 3의 배수임".format(input_data))
    else:
        print("{}는 3의 배수가 아님".format(input_data))
else:
# 문자이면 입력한 문자중에 't' 문자가 있는지 확인
    if 't' in input_data:
        print('t가 입력된 자료 : {}'.format(input_data))
    else:
        print('t가 없는 자료 : {}'.format(input_data))


# In[50]:


# 숫자 두개와 부호를 입력받아 계산하는 프로그램 작성
# 1. 처음 숫자 입력
# 2. 두번째 숫자 입력
# 3. 부호 입력 ( +, -, *, / 가 아니면 '부호에러' 출력)
# 4. 각 부호에 맞는 계산식과 결과 출력
num_1 = float(input("처음 숫자 입력 > "))
num_2 = float(input("두번째 숫자 입력 > "))
buho = input("부호 입력 (+,-,*,/) > ")
if buho in '+-*/':
    if buho == '+':
        result = num_1 + num_2
    elif buho == '-':
        result = num_1 - num_2
    elif buho == '*':
        result = num_1 * num_2
    else:
        result = num_1 / num_2
    print("{} {} {} = {}".format(num_1,buho,num_2,result))
else:
    print("부호 입력 오류")


# In[52]:


# list => [ 자료1, 자료2, ...] 자료들의 자료
a_list = [23,  'test', 'abcd', 45, True, False]
print(a_list)


# In[53]:


# test 문자열 추출
print(a_list[1])
print(a_list[2][0 : 2])  #ab
a_list[0] = 'list_a'
print(a_list)


# In[54]:


# list안에 list 내포
b_list = [[1,2,3], [4,5,6], [7,8,9]]
print(b_list)
print(b_list[1]) # [4,5,6]
print(b_list[2][0]) # 7


# In[61]:


# 10 + 20의 형식으로 입력을 받아 계산하는 프로그램 작성
input_data = input("계산식 입력 : (10 + 20 의 형식) > ").split()
print(input_data)

num_1 = int(input_data[0])
num_2 = int(input_data[-1])
buho = input_data[1]
if buho in '+-*/':
    if buho == '+':
        result = num_1 + num_2
    elif buho == '-':
        result = num_1 - num_2
    elif buho == '*':
        result = num_1 * num_2
    else:
        result = num_1 / num_2
    print("{} {} {} = {}".format(num_1,buho,num_2,result))
else:
    print("부호 입력 오류")


# In[73]:


# 처음 숫자에 'q'가 입력 되면 계산기 종료
while True:
    input_data = input("계산식 입력 : (10 + 20 의 형식 ※q 입력시 종료) > ").split()
    if input_data[0] == 'q' :
        break
    else:
        num_1 = int(input_data[0])
        num_2 = int(input_data[-1])
        buho = input_data[1]
        if buho in '+-*/':
            if buho == '+':
                result = num_1 + num_2
            elif buho == '-':
                result = num_1 - num_2
            elif buho == '*':
                result = num_1 * num_2
            else:
                result = num_1 / num_2
            print("{} {} {} = {}".format(num_1,buho,num_2,result))
        else:
            print("부호 입력 오류")
        


# In[87]:


# 구구단 출력
num_1 = 2 # 단
while num_1 < 10:
    num_2 = 1 # 1 ~ 9 까지 변하는 수
    while num_2 < 10:
        print("{} * {} = {}".format(num_1, num_2, num_1 * num_2), end='\t')
        num_2 += 1
    print()
    num_1 += 1


# In[88]:


# 두 수를 입력받아 두 수사이의 함을 구하세요
# 3 10 -> 3 +4 +5 + ... +10
while True:
    input_data = input('두 수 사이의 합을 구하세요 (10 20) > ').split()
    if input_data[0] == 'q' :
        break
    if len(input_data) !=2:
        print("두 수를 입력하세요")
        continue
    if input_data[0].isalpha() or input_data[1].isalpha():
        print("두 수를 입력하세요")
        continue
    num_1 = int(input_data[0])
    num_2 = int(input_data[1])
    if num_1 > num_2: # 큰값 작은값이 입력되면 값을 변경
        num_1,num_2 = num_2,num_1
    total = num_1
    ch_num = num_1
    while ch_num < num_2:
        ch_num += 1
        total += ch_num
    print("{}와 {}사이의 합은 {}".format(num_1, num_2, total))


# In[96]:


# list 선언, 함수, ...
# list에 요소 추가하기 : 리스트.append(값), 리스트.insert(위치, 값)
a_list = [1,2,3]
a_list.append(4) #[1,2,3,4]
print(a_list)

a_list.insert(1,'test')  #[1,'test',2,3,4]
print(a_list)

# a_list에 리스트 요소 추가
a_list.append([4,5,6]) # [1,'test',2,3,4,[4,5,6]]
print(a_list)

# extend(리스트) ->리스트의 각 요소가 리스트의 요소로 추가
a_list.extend([7,8,9]) #[1,'test',2,3,4,[4,5,6],7,8,9]
print(a_list)

# 리스트 + 리스트 -> 기존 리스트의 값에 변화 없음
print(a_list + [11,22,33])
print(a_list)


# In[97]:


# 리스트 요소 삭제 : del 리스트명[인덱스], 리스트명.pop(인덱스)]
# 리스트 값으로 삭제 : 리스트명.remove(값)
# 인덱스 1인 'test' 자료 삭제 : del 명령어 사용
del a_list[1]
print(a_list)


# In[98]:


# [4,5,6] 리스트 자료 삭제
a_list.pop(4) # 4 인덱스 자료 삭제
print(a_list)


# In[99]:


b_list = [1,2,3,4,5]
del b_list[1:3] # 2와 3삭제
print(b_list)


# In[100]:


b_list.remove(5)
print(b_list)


# In[101]:


# 리스트의 모든 요소 제거 : 리스트명.clear()
b_list.clear()
print(b_list)


# # list에 요소 추가하기 : 리스트.append(값), 리스트.insert(위치, 값)
# # 리스트에 리스트의 각 요소를 리스트의 요소로 추가 : 리스트.extend(리스트)
# # 리스트 요소 삭제 : del 리스트명[인덱스], 리스트명.pop(인덱스)]
# # 리스트 값으로 삭제 : 리스트명.remove(값)
# # 리스트의 모든 요소 제거 : 리스트명.clear()

# In[103]:


print(7 in a_list)  # 값 in 반복자료 -> True, False, not in
print(7 not in a_list)


# In[105]:


# for 반복자 in 반복 자료:
#     처리
for i in range(5):    #range(start (0부터 시작), end, step )
    print('출력', i)
print()
for i in range(1,5):
    print('출력', i)


# In[108]:


for i in a_list:
    print(i)
for char in 'hello world!!':
    print("-",char,end='')


# In[114]:


while True:
    input_data = input('두 수 사이의 합을 구하세요 (10 20) > ').split()
    if input_data[0] == 'q' :
        break
    if len(input_data) !=2:
        print("두 수를 입력하세요")
        continue
    if input_data[0].isalpha() or input_data[1].isalpha():
        print("두 수를 입력하세요")
        continue
    num_1 = int(input_data[0])
    num_2 = int(input_data[1])
    total = 0
    if num_1 < num_2: # 큰값 작은값이 입력되면 값을 변경
        for i in range(num_1, num_2+1):
            total += i
    else:
        for i in range(num_2,num_1+1):
            total += i
    print("{}와 {}사이의 합은 {}".format(num_1, num_2, total))


# In[115]:


# list의 요소 가져오기
a_list = [273,45,3,4,88]
for i in a_list:
    print(i, end='\t') # 273,45,3
print()

# range()함수와 인덱스를 이용하여 자료 가져오기
for i in range(len(a_list)):
    print(a_list[i], end='\t')
print()


# In[ ]:


# 숫자를 입력받아 리스트에 저장 : 'q'가 입력되면 종료
# 입력된 숫자의 총합고 총 곱을 출력
# 입력된 숫자의 갯수와 입력된 숫자의 평균을 출력 ( 평균은 소수점 미만 2자리로)


# In[136]:


while True:
    input_data = input('숫자를 입력하시오(q입력시 종료) > ').split()
    if input_data[0] == 'q' :
        break
    for i_data in input_data :
        if i_data.isalpha():
            print("숫자를 입력하세요")
            break

    t_list = []
    add_num = 0
    # 다 작업 못함
    # t_list.append(input_data[0: ])
    


# In[ ]:


a_list = []
print("처음", a_list)
a_list.append(1)
print("1을 추가함", a_list)
a_list.append(2)
print("2를 추가함", a_list)

