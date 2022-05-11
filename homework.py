#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# 1. 계산식('10 + 10'의 형식)을 입력받아 사칙연산을 수행 및 출력하는 
# 프로그램을 작성하시오.
# (조건 1) 특정 문자 입력시 종료가 가능하게 할 것. 예) q 입력시 프로그램 종료
# (조건 2) 가능한 모든 경우의 수에 대해 잘못 입력된 경우
#            다시 입력할 수 있게 하는 과정을 설계할 것. 
# 예) 잘못된 계산식 입력시 다시 입력하게
# (조건 3) 종료하기 전까지 새로운 계산식을 입력받아 반복 수행할 수 있는 
# 프로그램을 작성할 것.
# (조건 4) 한 셀 안에 완전한 프로그램을 작성하여 코드를 복사 및 붙여넣기했을 때 문제없이 돌아가게 할 것.
# (조건 5) 출력 결과에 계산식도 포함되도록 작성할 것.
# 실행 결과 예시)
# 10 * 20 = 200.0

def input_func():
    while True:
        input_data = input("계산식 입력 : 10 + 20의 형식 ").split()
        if input_data[0] == 'q':
            print("입력 종료")
            break
        if len(input_data) != 3:
            print("입력오류 재입력")
            continue
        num_list = [ int(num) for num in input_data if num.isdigit() ]
        if input_data[1] in '+-*/':
            return (num_list[0], input_data[1], num_list[1])
        else:
            print("부호 입력 오류")
def buho_func(num1, num2):
    if buho == '+':
        return num1 + num2
    elif buho == '-':
        return num1 - num2
    elif buho == '*':
        return num1 * num2
    else:
        return num1 / num2

while True:
    num1, buho, num2 = input_func()
    print('{} {} {} = {}'.format(num1,buho,num2,buho_func(num1,num2)))


# In[ ]:


# 2. 이름과 국어, 영어, 수학 점수를 입력 받아 
# 총점과 평균을 출력하는 프로그램을작성하시오.
# (조건 1) 텍스트 파일을 만들어 프로그램이 실행될 때마다
# 작성 및 수정이 가능하게 할 것.
# (조건 2) 특정 문자 입력시 종료가 가능하게 할 것. 예) q 입력시 프로그램 종료
# (조건 3) 가능한 모든 경우의 수에 대해 잘못 입력된 경우
#            다시 입력할 수 있게 하는 과정을 설계할 것. 
# 예) 점수가 2과목만 입력시 다시 입력하게
# (조건 4) 한 사람이 아닌 여러 사람의 이름과 점수를 
# 반복적으로 입력받아서 누적 출력할 수 있게 할 것.
# (조건 5) 한 셀 안에 완전한 프로그램을 작성하여 
# 코드를 복사 및 붙여넣기했을 때 문제없이 돌아가게 할 것.
# (조건 6) 코드에 오류가 생겼을 경우를 대비하여 
# 정상 작동 및 오류 발생시 특정 문구가 출력될 수 있도록 작성할 것.
# 실행 결과 예시)
# 파일 실행 중...
# 이름    국어    영어    수학    총점    평균
# 양창은    90    80    85    255.0    85.00
# 양현모    95    75    70    240.0    80.00
student = {}
fp = open("student.txt","a+")
while True :
    name = input('이름 입력 > ')
    if name == 'q':
        break
    while True:
        input_score = input("국어 영어 수학 점수 입력 >").split()
        if len(input_score) == 3:
            break
    output = name + ',' + ','.join(input_score) + '\n'
    fp.write(output)

    fp.seek(0)
    print("이름 : [국어 영어 수학] 합계 평균")
    for line in fp.readlines(): 
        line_list = line.strip('\n').split(',')
        student[line_list[0]] = [ int(line_list[i]) for i in range(1,4)]
    for key, score in student.items():
        print("{} : {} {}  {:3.2f} ".format(key, score, sum(score),sum(score)/3))
fp.close


# In[ ]:


# GG
# 어느 고등학교에서 실시한 1000명의 수학 성적을 토대로 통계 자료를 만들려고 한다.
# 이때, 이 학교에서는 최빈수를 이용하여 학생들의 평균 수준을 짐작하는데, 
# 여기서 최빈수는 특정 자료에서 가장 여러 번 나타나는 값을 의미한다.
# 다음과 같은 수 분포가 있으면,
# 10, 8, 7, 2, 2, 4, 8, 8, 8, 9, 5, 5, 3
# 최빈수는 8이 된다.
# 최빈수를 출력하는 프로그램을 작성하여라 
# (단, 최빈수가 여러 개 일 때에는 가장 큰 점수를 출력하라).
# [제약 사항]
# 학생의 수는 1000명이며, 각 학생의 점수는 0점 이상 100점 이하의 값이다.
# [입력]
# 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
# 각 테스트 케이스의 첫 줄에는 테스트 케이스의 번호가 주어지고 
# 그 다음 줄부터는 점수가 주어진다.
# [출력]
# 부호와 함께 테스트 케이스의 번호를 출력하고, 
# 공백 문자 후 테스트 케이스에 대한 답을 출력한다.
def put_counter(arr):
    cb_count = 0
    cb = 0
    for i in range(100,-1,-1):
        count = arr.count(i)
        if cb_count < count:
            cb_count = count
            cb = i
    return cb

if __name__ == "__main__":
    t = int(input("테스트 케이스의 수 : "))
    for i in range(t):
        t_data = int(input("테스트 케이스 번호 : "))
        arr = list(map(int,input("자료입력 : ").strip().split()))
        print("#{} {}".format(t_data,put_counter(arr)))


# In[ ]:




