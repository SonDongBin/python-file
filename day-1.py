#!/usr/bin/env python
# coding: utf-8

# In[ ]:


print("test")


# In[ ]:


import keyword
print(keyword.kwlist)


# #PYTHON CODE
# -- PRINT 설명

# a = 10 + 20
# print(a)

# In[ ]:


print(10, 20, 'print test')
print(50)
print('a = ', a)
b = 20
b


# In[ ]:


# 하나만 출력합니다.
print("#하나만 출력합니다")
print("Hello Python Programing...!")
print()

#여러개를 출력합니다.
print(10, 20, 30, 40, 50)
print("안녕하세요", "저의", "이름은", "손동빈입니다!")
print()

#아무것도 입력하지 않으면 단순하게 줄바꿈합니다.
print("# 아무것도 출력하지 않습니다.")
print("--- 확인 전용선---")
print()
print()
print("--- 확인 전용선---")


# In[ ]:


# print() 함수 사용
print(type('test'), type(12), type(True), type(35.0), sep='\t')
print('test123','blank')
# "를 출력 \" escape 문자 사용
print("\"hello !!\\\"")

# \t, \n, \특수문자 (", ', \)


# In[ ]:


# \t 를 사용하여 자리수 맞춤으로 출력
print("이름\t나이\t지역")
print("윤인성\t25\t강서구")
print("윤아린\t24\t강서구")
print("구름\t3\t강서구")


# In[ ]:


print("""동해물과 백두산이 마르고 닳도록
하느님이 보우하사 우리나라 만세
무궁화 삼천리 화려강산 대한사람
대한으로 길이 보전하세\
""")


# In[ ]:


# 여러 라인의 문자열 => """ 문자열 """
# 문자열 연산 : + => 문자열 + 문자열
print("Good" + "afternoon !!" + " end!!")
# print("Good" + 1) # error


# In[ ]:


# 문자열 * 숫자 = 숫자만큼 문자열 반복
# 숫자 * 문자열
print('test ' * 3)
print(3 * 'test ')


# In[ ]:


# 0 인덱스
a_str = '안녕하세요'
print(a_str[0])
print(a_str[-1])
print(a_str[-2]) #세


# In[ ]:


# 범위의 자료를 검색 [ start : end ] : start는 포함, end는 포함하지 않음

print(a_str[0 : 2]) # 안녕만 출력

print(a_str[2 : ]) # 하부터 끝까지 출력

print(a_str[ : 3]) # 처음부터 하까지만 출력

print(a_str[ : -1]) # 마지막 글자만 제외하고 출력

print(a_str[ : ]) # 모든 문자 출력

print(a_str[-2])

# print(a_str[10]) index out of range


# In[ ]:


# 자료의 타임을 알려주는 함수 : type()
# 문자의열의 길이를 구하는 함수 : len()
print(len(a_str))
print(a_str[2 : len(a_str)-1]) # a_str[ 2: 5 - 1 ]
print(type(a_str))


# In[ ]:


# 숫자 연산자 : +, -, /, //, %, **
print(4 + 2, 4 - 2, 3 * 2, 3 / 2, 3 % 2, 3 **2)
a = 10; b = 3
print(a, "+", b, "=", a+b)
print(a, "//", b, "=", a//b)
print(a, "%", b, "=", a%b)


# In[ ]:


# 변수 선언과 참조
a = 10
b = 3
a + b


# In[ ]:


a += 3
a + b


# In[ ]:


a_str += '!'
print(a_str)


# In[ ]:


## 키보드에서 입력 받는 함수 input()
input_data = input('자료입력 > ') # 값
print(input_data, type(input_data))

# 데이터 타입을 변경 -> int(), float(), str()
print(float(input_data) + 100)
print(str(input_data) + '1') # str -> float -> str


# In[ ]:


# 키보드로 부터 두 수를 입력 받아 두 수의 합과, 곱의 결과를 구하세요
input_a = input("숫자 입력 ")
input_b = float(input("숫자입력 "))
print("input_a type : ", type(input_a), "\tinput_b type : ", type(input_b))
input_a = float(input_a)
print(input_a, "+", input_b , "=", input_a + input_b)
print(input_a, "*", input_b , "=", input_a * input_b)


# a = int(input('숫자'))
# b = int(input('숫자'))
# print(a+b)
# print(a*b)

# In[ ]:


# 문자열 관련 함수 : "{} {}".format(data1,data2)
print("{} {}".format('test', 123))
print("{} + {} = {}".format(input_a , input_b , input_a + input_b))
print("input_a type : {}\t input_b type : {}"     .format(type(input_a),type(input_b)))


# In[ ]:


# 정수
output_a = "{:d}".format(52)

# 특정 칸에 출력하기
output_b = "{:5d}".format(52)
output_c = "{:10d}".format(52)

#빈칸을 0으로 채우기
output_d = "{:05d}".format(52)
output_e = "{:05d}".format(-52)

print("# 기본")
print(output_a)
print("# 특정 칸에 출력하기")
print(output_b)
print(output_c)
print("# 빈칸은 0으로 채우기")
print(output_d)
print(output_e)


# In[ ]:


# 키보드에서 영문자 입력 -> input_str에 저장
input_str = input("영문자 입력 > ")
# 소문자로 출력  문자열.lower()
print("소문자 출력 : {}".format(input_str.lower()))
# 대문자로 출력  문자열.upper()
print("대문자 출력 : {}".format(input_str.upper()))

