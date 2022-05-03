#!/usr/bin/env python
# coding: utf-8

# In[ ]:


while True:
    input_data = input("계산식 입력 : (10 + 20 의 형식 ※q 입력시 종료) > ").split()
    if input_data[0] == 'q' :
        break
    if len(input_data) != 3:
        continue
    if not input_data[0].isnumeric() or not input_data[2].isnumeric():
        continue
        
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
print("Program end!!!")

