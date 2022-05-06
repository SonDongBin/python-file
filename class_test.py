#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Student:
#    def __init__(self, 추가적인 매개변수)
    def __init__(self,name,kor,math):
        self.name = name
        self.kor = kor
        self.math = math
        
    def get_sum(self):
        return self.kor + self.math
        
student_1 = Student('홍길동', 90, 80) # 클래스명() -> 생성자,하나의 instance 생성
print("{} : {}, {}, 총점 : {}".format(student_1.name,student_1.kor,
                                   student_1.math, student_1.get_sum()))


# In[ ]:


# 이름, 국어, 영어, 수학 점수를 입력 받아
# 클래스의 리스트로 저장
# 각 학생의 이름, 성적, 총합, 평균
# 전체 학생의 과목별 총점과 평균을 구하세요
class Student:
    def __init__(self,name,kor,eng,math):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math
        
    def get_sum(self):
        return self.kor + self.eng + self.math
    
    
    def __str__(self):   # 함수 호출시 일반 함수처럼 호출 가능
        return "{}\t{}\t{}".format(self.name,
                                  self.get_sum(),
                                  self.(get_sum()/3))
students = [] 
while True:
    name = input("이름을 입력 : ")
    if name == 'q':
        print("종료합니다")
        break
    
    while True:
        input_score = input("성적을 입력 : ").split()
        if len(input_score) == 3 :
            break
        else :
            print("입력오류")
            continue
    
    students.append(Student(name,int(input_score[0]),
                        int(input_score[1]),int(input_score[2])))


# In[ ]:


for student in students:
    print("{} : {}, {}, {}, 총점 : {} , 평균 : {:3.2f}".         format(student.name, student.kor, student.eng,
               student.math, student.get_sum(), (student.get_sum())/3))


# In[ ]:





# In[ ]:


# isinstance(instance, class) 함수 : instance가 클래스 소속에 대해 True, False
class Student:
#    def __init__(self):
#        self.a = 'test'   # 메모리에 값을 할당할수 없음, error
#        self.score
    def study(self):
        print("공부를 합니다")

class Teacher:
    def teach(self):
        print("학생을 가르칩니다")
        
classroom = [Student(), Student(), Teacher(), Student(), Teacher()]

# 각 인스턴스가 Student 이면 학생의 print 아니면 teacher의 print()
for person in classroom:
    if isinstance(person, Student):
        person.study()   # 학생 클래스의 print()
    else:
        person.teach()   # 선생님 클래스의 print()


# In[ ]:


# 클래스를 선언합니다.
class Student:
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science

    def get_sum(self):
        return self.korean + self.math +            self.english + self.science

    def get_average(self):
        return self.get_sum() / 4

    def __str__(self):
        return "{}\t{}\t{}".format(
            self.name,
            self.get_sum(),
            self.get_average()) 
    def __eq__(self,value):  # a == b
        return self.get_sum() == value.get_sum()
    def __ne__(self,value):  # a != b
        return self.get_sum() != value.get_sum()


# In[ ]:


student_a = Student("윤인성", 87, 98, 88, 95)
student_b = Student("연하진", 92, 98, 96, 98)
print("student_a == student_b : ", student_a == student_b)
print("student_a != student_b : ", student_a != student_b)


# In[ ]:


# 학생 리스트를 선언합니다.
students = [
    Student("윤인성", 87, 98, 88, 95),
    Student("연하진", 92, 98, 96, 98),
    Student("구지연", 76, 96, 94, 90),
    Student("나선주", 98, 92, 96, 92),
    Student("윤아린", 95, 98, 98, 98),
    Student("윤명월", 64, 88, 92, 92)
]

# 출력합니다.
print("이름", "총점", "평균", sep="\t")
for student in students:
    print(str(student))


# In[ ]:


# 클래스 변수 : 클래스명.변수명, 클래스 함수 : @classmethod def 함수명() :
class Student:
    # 클래스 변수
    count = 0
    students = []
    
    # 클래스 함수
    @classmethod
    def print(cls):
        print("-----------학생목록----------")
        print("이름\t총점\t평균")
        for student in Student.students:
            print(str(student))
        print("-----------------------------")
        
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science
        Student.count += 1  # 학생수 증가시킴
        Student.students.append(self)  # 학생 리스트에 데이터 추가
        
    def get_sum(self):
        return self.korean + self.math +            self.english + self.science

    def get_average(self):
        return self.get_sum() / 4

    def __str__(self):
        return "{}\t{}\t{}".format(
            self.name,
            self.get_sum(),
            self.get_average()) 


# In[ ]:


Student("윤인성", 87, 98, 88, 95)
Student("연하진", 92, 98, 96, 98)
Student("구지연", 76, 96, 94, 90)
Student("나선주", 98, 92, 96, 92)
Student("윤아린", 95, 98, 98, 98)
Student("윤명월", 64, 88, 92, 92)
Student("김미화", 82, 86, 98, 88)
Student("김연화", 88, 74, 78, 92)
Student("박아현", 97, 92, 88, 95)
Student("서준서", 45, 52, 72, 78)
print(Student.count)
Student.print()


# In[ ]:


class Test:
    def __init__(self, name):
        self.name = name
        print("{} - 생성되었습니다".format(self.name))
    def __del__(self):
        print("{} - 파괴되었습니다".format(self.name))

a = Test("A")
b = Test("B")
c = Test("C")


# In[ ]:


import math


# In[ ]:


class Circle:
    def __init__(self,radius):
        self.__radius = radius  # private 변수 : 외부에서 접근 불가
        
    def get_circle_area(self):
        return self.__radius * 2 * math.pi

#    def get_radius(self):    # getter
#        return self.__radius
    
    @property
    def radius(self):    # getter
        return self.__radius
    
#    def set_radius(self, value):    # setter
#        self.__radius = value
        
    @radius.setter
    def radius(self, value):    # setter
        self.__radius = value


# In[ ]:


circle = Circle(10)
circle.get_circle_area()
print("befor :",circle.radius)
circle.radius = 20
circle.get_circle_area()
print("after :",circle.radius)


# In[ ]:


# 이름과 정수를 입력받아 저장 : Stu -> class를 생성
# 이름에 'q' 가 입력되면 입력 종료
# 학생의 이름을 private 변수로 지정
# 학생의 이름과 성적을 출력
# 수정하고자 하는 이름을 입력 받아 검색해서 이름과 성적을 출력
# 검색된 자료가 존재하면 수정하고자 하는 이름을 입력받아 기존의 이름 수정
# 수정된 최종 전체 학생 결과 출력


# In[3]:


class Stu:
    def __init__(self,name,score):
        self.__name = name
        self.score = score
        
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,value):
        self.__name = value


# In[ ]:


# students = []
while True:
    input_data = input("이름 성적 입력 : ").split()
    if input_data[0] == 'q':
        break
    students.append(Stu(input_data[0],input_data[1]))
    
for student in students:
    print(student.name,' : ', student.score)
print()

search_name = input("수정하고자 하는 이름 입력 : ")
for student in students:
    if student.name == search_name:
        change_name = input("바꿀 이름 입력 : ")
        student.name = change_name
else:
    print("수정하고자 하는 이름 없음")
print()

for student in students:
    print(student.name, ' : ', student.score)
print()


# In[11]:


# 클래스 상속
# 부모 클래스 선언
class Parent:
    def __init__(self):
        self.value = '테스트'
        print("Parent 클래스의 __init__ 메소드 호출")
    def test(self):
        print("Parent 클래스 호출")

# 자식 클래스 생성        
class Child(Parent):   # 클래스명(부모 클래스명)
    def __init__(self):
        Parent.__init__(self)
        print("Child 클래스의 __init__ 메서드 호출")
    def test(self):   # 부모와 같은 이름의 함수 재정의 : 오버라이드
        print("Child 클래스 호출")
    def child_func(self):
        print("child Nes function 호출")


# In[13]:


child = Child()
child.test()
print(child.value)
child.child_func()


# In[15]:


print(type([1,2,3]))


# In[ ]:


def 함수명():

class 클래스명:
    클래스 변수
    @clssmethod
    def 함수명() -> 클래스 함수
    def __init__(self, ...):
        self.__변수명 -> private 변수
    @property
    def 변수명(self):
        return self.__변수명
    @변수명.setter
    def 변수명(self, 값):
        self.__변수명 = 값
    def get_func(self, )
    
함수명(값, ...)
클래스명(값, ...) -> 생성자, __init__함수를 실행
클래스명.변수 -> 클래스 변수
클래스명.함수명 -> 클래스 함수
오브젝트명.변수명 -> private getter
오브젝트명.변수명 = 값 -> private setter

