#!/usr/bin/env python
# coding: utf-8

# In[10]:


# 재귀함수
# 반복문으로 팩토리얼 수 구하기
def fact(n):
    global counter
    output = 1
    for i in range(1,n+1):
        output *= i
        counter += 1
    return output
# 재귀함수로 팩토리얼 구하기
def fact_rec(n):  # n*fact_rec(n-1)
    # n이 0이면 1을 return
    global counter
    counter += 1
    if n == 0:
        return 1
    else:
        return n * fact_rec(n-1)


# In[5]:


counter = 0
print(fact(6), counter) # n! 구함


# In[11]:


counter = 0
print(fact_rec(10), counter)


# In[25]:


# 피보나치 수열 : 1=1, 2=1, f(n) = f(n-1) + f(n-2)
def fibo(n):  # 실행 속도가 느림 -> 함수 호출 횟수가 중복해서 호출
    # print("fibonacci({}) 를 구함".format(n))
    global counter
    counter += 1
    if n == 1:
        return 1
    if n == 2:
        return 1
    return fibo(n-1) + fibo(n-2)

def fibo_memo(n):
    global counter
    counter += 1
    if n in dictionary:
        return dictionary[n]
    
    output = fibo_memo(n-1) + fibo_memo(n-2)
    dictionary[n] = output
    return output


# In[26]:


counter = 0
fibo(35)
print("실행횟수 : {}".format(counter))

dictionary = {1:1, 2:1}
counter = 0
fibo_memo(35)
print("fibo_memo() 실행횟수 : {}".format(counter))
print(dictionary)


# In[27]:


# 고급 함수 : lambda
# 함수를 매개변수로 전달하는 대표적인 표준함수
# map(함수, 리스트) : 리스트의 각 요소에 함수를 적용
# filter(함수, 리스트) : 리스트의 각 요소중 조건에 맞는 요소만 함수를 적용
def power(item):
    return item * item
def under_3(item):
    return item < 3

power_1 = lambda x: x*x
under_3_1 = lambda x: x<3


# In[ ]:


list_a = [1,2,3,4,5]
# map() 함수를 사용
output_a = map(power, list_a)
print(list(output_a))

# filter() 함수를 사용
output_b = filter(under_3, list_a)
print(list(output_b))


# In[28]:


list_a = [1,2,3,4,5]
# map() 함수를 사용, inline labda
output_a = map(lambda x: x*x, list_a)
print(list(output_a))

# filter() 함수를 사용
output_b = filter(lambda x: x<3, list_a)
print(list(output_b))


# In[33]:


# 파일 처리 : fp = open("파일명", 모드) ~ fp.close()
fp = open("./basic1.txt","w")
fp.write("file write test!!!")
#fp.close()


# In[34]:


fp.close()


# In[32]:


# with 키워드를 사용해서 file open, with 구문 종료시 file 자동 close
with open("basic.txt","a") as fp:
    fp.write("with write test\n")


# In[37]:


# file read
with open("basic.txt","r") as fp:
    content = fp.read()   # file의 전체 데이터 읽음
    fp.seek(0)   # file의 처음으로 이동
    print("111",fp.readlines())
    fp.seek(0)
    for line in fp.readlines():   # \n을 기준으로 데이터를 읽음
        print("222",line)
    


# In[58]:


# 이름 국어 영어 수학 점수를 입력받아 파일에 저장 한 후
# 파일의 내용을 가져와서 이름을 키로 성적을 데이터로 딕셔너리에 저장 후
# 학생 이름 국어 영어 수학 총점 평균을 출력하는 프로그램 작성
# 파일명은 student.txt, 딕셔너리는 student로 하세요
# 입력은 이름에 'q'가 입력되면 종료
# 홍길동,90,80,70 이 형식으로 파일에 저장

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


# In[61]:


student = {}
fp.seek(0)
for line in fp.readlines():  # 라인 단위로 데이터 읽어옴
    line_list = line.strip('\n').split(',') # 마지막 '\n' 제거후 ','로 분리
#    student[line_list[0]] = list(map(lambda x:int(x),
#    [line_list[i] for i in range(1,4)]))
    student[line_list[0]] = [ int(line_list[i]) for i in range(1,4)]
#fp.close
print(student)


# In[62]:


for key, score in student.items():
    print("{}: {} {} {:3.2f} ".format(key, score, sum(score),sum(score)/3))


# In[63]:


# 제너레이터 함수 : yield 가 존재하면 함수를 호출해도 실행되지 않음
# next() 함수를 사용하여 실행
def test():
    print("test finc")
    yield "test"
    
# 함수 호출
print("first")
test()

print("second")
next(test())

print(test())


# In[68]:


# 제너레이터 함수는 next(제너레이터 함수명)으로 실행, yield을 만나면 멈춤
def test():
    print("A 지점 통과")
    yield 1
    print("B 지점 통과")
    yield 2
    print("C 지점 통과")
    yield
# 함수 호출
func = test()
print("D 지점 통과") # 1
print(next(func))    # A 지점 통과, 1
print("E 지점 통과") # E 지점 통과
print(next(func)    # B 지점 통과, 2
next(func)


# In[69]:


(lambda x,y: x + y)(1,3)


# In[70]:


# try ~ except : 프로그램 실행시 예외 발생시 처리하는 구문
# try:
# 예외 발생 가능성 있는 코드
# except:
# 예외 발생시 실행하는 코드
# else:
# 정상 작동시 실행하는 코드
# finally:
# 무조건 실행하는 코드
try:
    input_num = int(input("정수 입력 "))
    print(input_num * 2)
except:
    print("정수를 입력하세요")
#    pass


# In[78]:


try:
    fp = open("info.txt","r")
    fp.write("try test file \n")
except Exception as e:
    print("run time error")
    print(e)
else:
    print("file read")
    try:
        fp.read()
    except:
        print("file read error")
finally:
    print("The end")
    fp.close()
    
print("file closed : ", fp.closed)


# In[79]:


# try _ except ~ else ~ finally ~ : finally는 어느 경우에도 실행함
def test():
    print("func start")
    try:
        print("try 구문 실행")
        return
    except:
        print("except 구문 실행")
    finally:
        print("finally 실행")
    print("test end")
    
test()


# In[83]:


def input_data():
    global fp
    while True:
        try:
            i_data = input("이름 성적 입력 ").split()
            if i_data[0] == 'q':
                read_file()
                return
            fp.write(','.join(i_data+'\n')
        except Exception as e:
            print("입력 오류 -> 다시 입력 하세요 :",e)
        finally:
            print("입력 종료")
def read_file():
    global fp
    fp.seek(0,0)
    for line in fp:
        line_list = line.split(',')
        print("{} : {}".format(line_list[0],line_list[1]))


# In[ ]:


# 이름과 성적을 입력 받아 파일에 저장하는 프로그램 작성
# try ~ except ~ finally 를 사용하여 입력 자료 검증
# 이름은 isalpha, 점수는 isdigit인지 확인
# 이름에 'q'가 입력 되면 종료


# In[ ]:


숫자(int, float), 문자(str), boolean(True,False)
데이터를 여러개 모은것 : list[], dictionary{키:값, ...}, tuple()
if ~ else
if ~ elif ~ else
while ~ break continue
for 변수 in 반복자

def 함수(매개변수, ...) -> yield -> 호출 next()
호출
함수(값, ...)

try: ~ except ~ else ~ finally
file = open(파일명,모드)
with open(파일명, 모드) as file:
    
문자열 관련 함수 => 문자열.upper(), lower, is00(), split(), strip()
문자열[start : stop ] start 포함 stop 포함 안함
리스트 관련함수 -> 데이터 추가 .append(), insert(), extend()
                  제거 리스트.pop(), 리스트.remove()
                  수정 리스트[인덱스] = 값
                  리스트.reversed()
                  리스트.sort()
sum(리스트) , max(리스트) , min(리스트)
딕셔너리 -> dict.kyes(), value(), items()
        수정 dict[키] = 값
        추가 dict[추가 키] = 값
자료삭제 : del 리스트[], del dict[키]
    
특별한 함수 (lambda x,y: return 값)(x,y)
type(변수)
len(변수)
range(start, stop, step)


# In[84]:


list_a = [1,2,3]
# list_b = list_a.copy # 데이터 복사
list_b = list_a
list_b[1] = 10 # list_a가 수정 됨
print(list_a)
print(list_b)


# In[ ]:




