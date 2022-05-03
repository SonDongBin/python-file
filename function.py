#!/usr/bin/env python
# coding: utf-8

# In[17]:


# 함수 : 코드의 집합
# 선언(정의)
# def 함수명(매개변수, ...):  일반, 가변, 키워드
#     들여쓰기
#     return 값

def print_3_times():
    print("hello!!")
    print("hello!!")
    print("hello!!")
    
def print_n_times(value, n):   # 기본 형
    for i in range(n):
        print(value)
        
def print_val_times(n, *values):  # 가변 매개변수, 하나만 사용
    for i in range(n):
        for value in values:
            print(value, end='\t')
        print()
        
def compute_func(num1,num2=100):
    return num1 + num2
# 매개변수 나열 순서 -> 기본, 가변, 키워드


# In[18]:


print_3_times()   # 함수 호출
print()
print_n_times('test',2)
print()
print_val_times(2,'test','data','세번째 데이터')
print(compute_func(10,30))
print(compute_func(20)) # num2 에 100이 입력됨


# In[57]:


# 계산기 프로그램 작성
# 입력은 10 + 20 의 형식으로
# 입력된 문자열을 분리해서 리스트로 변형한 후 숫자이면 int로 형 변환
# 각 부호별로 함수정의
def input_func():
    while True:
        input_data = input("계산식 입력 : 10 + 20의 형식 ").split()
        num_list = [ int(num) for num in input_data if num.isdigit() ]
        if input_data[1] in '+-*/':
            return (num_list[0], input_data[1], num_list[1])
def buho_func(num1, num2):
    if buho == '+':
        return num1 + num2
    elif buho == '-':
        return num1 - num2
    elif buho == '*':
        return num1 * num2
    else:
        return num1 / num2   


# In[62]:


num1, buho, num2 = input_func()
buho_func(num1,num2)


# In[ ]:




