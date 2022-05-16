from Student import Student
from Classroom import Classroom
from School import School

import os.path
from random import *
import random

import numpy as np

last_name = '김이박최정강조윤장임한신오서권황송안유홍' # 한국 성 순의 20
first_name = '가나다라마바사아자차카타파하'         # 이름조합

file = '/Users/j00n/Documents/GitHub/Academy-HW/Students.txt'

def Generator(num):         # 학생 정보 생성기
    if os.path.isfile(file) == True:
        return file
    else:
        f = open(file,'w')
        
        for i in range(num):
            ln = random.choice(last_name)
            mn = random.choice(first_name)
            fn = random.choice(first_name)
            name = ln+fn+mn
            age = randint(8,13)
            kor = randint(0,100)
            eng = randint(0,100)
            math = randint(0,100)
            f.write(name+",")
            f.write(str(age)+",")
            f.write(str(kor)+",")
            f.write(str(eng)+",")
            f.write(str(math)+"\n")
        f.close()
        return file

def make_student(file):             # 학생 Instanciate
    student_list = []
    with open(file,'r') as f:
        for line in f:
            S = "STUDENT"
            NO = 1
            (a,b,c,d,e) = line.split(",")
            student = Student(a,int(b),int(c),int(d),int(e))
            student_list.append(student)
    return student_list
                

# 입력한 숫자만큼 학생 생성
data = Generator(1000)

# 학생정보를 갖고 Instacne 화 한 후 Class 에 enroll

student_list = make_student(data)
Classroom1 = Classroom(student_list[:500])
Classroom2 = Classroom(student_list[500:])

Classroom = Classroom(student_list)

School = School(Classroom)
# 츨력
"""
print(Classroom,"\n")
print(Classroom.sort_by_kor(),"\n")
print(Classroom.sort_by_eng(),"\n")
print(Classroom.sort_by_math(),"\n")
"""


print("1반 국어평균 : {0}, 1반 영어평균 : {1}, 1반 수학평균 : {2}".format(Classroom1.kor_mean(), Classroom1.eng_mean(), Classroom1.math_mean()))
print("2반 국어평균 : {0}, 2반 영어평균 : {1}, 2반 수학평균 : {2}".format(Classroom2.kor_mean(), Classroom2.eng_mean(), Classroom2.math_mean()))
print("학교 국어평균 : {0}, 학교 영어평균 : {1}, 학교 수학평균 : {2}".format(School.kor_mean(), School.eng_mean(), School.math_mean()))