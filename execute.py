import random
from multiprocessing import Process, Queue
from Student import Student
from Classroom import Classroom
from School import School
from event import Event

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
            attendance = 1
            in_school = 1
            kor = randint(0,100)
            eng = randint(0,100)
            math = randint(0,100)
            f.write(name+",")
            f.write(str(age)+",")
            f.write(str(attendance)+",")
            f.write(str(in_school)+",")
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
            (a,b,c,d,e,f,g) = line.split(",")
            student = Student(a,int(b),int(c),int(d),int(e),int(f),int(g))
            student_list.append(student)
    return student_list

def execute(id, start, end, result, Event):

    day = 0
    for i in range(start, end):
        day += 1
        print("DAY {0}\n".format(day))
        Event.event_occur() # 이벤트 발생
        
        # 출석체크
        to = 0
        at = 0
        
        for classroom in Event.school:
            for student in classroom.classroom:
                if student.in_school == 1:
                    to += 1
                    if student.attendence == 1:
                        at +=1
        

        print("\n총원 : {0}명, 출석 수 : {1}명\n".format(to, at))
        print("-------------")
        
        for classroom in Event.school:
            for student in classroom.classroom:
                if student.in_school == 1:
                    student.attendence = 1
        
        

    
if __name__ == "__main__":
    
    last_name = '김이박최정강조윤장임한신오서권황송안유홍' # 한국 성 순의 20
    first_name = '가나다라마바사아자차카타파하'         # 이름조합
    file = '/Users/j00n/Documents/GitHub/Academy-HW/Students.txt'
    data = Generator(1000)
    student_list = make_student(data)
    Classroom1 = Classroom(student_list[:500])
    Classroom2 = Classroom(student_list[500:])
    Classroom = [Classroom1, Classroom2]
    School = School(Classroom)
    Event = Event(School.school)
    
    START, END = 0, 15
    result = Queue()
    th = Process(target=execute, args=(1, START, END, result, Event))
    
    th.start()
    th.join()
    