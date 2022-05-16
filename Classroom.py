# from Student import Student
import numpy as np
from Student import Student
from random import *
import random

class Classroom:
    def __init__(self,Student):
        self.classroom = []
        self.enroll(Student)
    
    def __repr__(self):
        return self.classroom
    
    def __str__(self):
        return '\n'.join(str(student) for student in self.classroom)

    def enroll(self,Student):
        if type(Student) == list:
            for student in Student:
                self.classroom.append(student)
        else:
            self.classroom.append(Student)
            
    def sort_by_kor(self):
        return '\n# 국어 성적순 #\n\n'+'\n'.join(str(student) for student in sorted(self.classroom, key=lambda x: x.get_score('kor'), reverse=True))
    
    def sort_by_eng(self):
        return '\n# 영어 성적순 #\n\n'+'\n'.join(str(student) for student in sorted(self.classroom, key=lambda x: x.get_score('eng'), reverse=True))
    
    def sort_by_math(self):
        return '\n# 수학 성적순 #\n\n'+'\n'.join(str(student) for student in sorted(self.classroom, key=lambda x: x.get_score('math'), reverse=True))
    
    def kor_mean(self):
        score = []
        for student in self.classroom:
            score.append(student.get_score('kor'))
        return np.mean(score)
    
    def eng_mean(self):
        score = []
        for student in self.classroom:
            score.append(student.get_score('eng'))
        return np.mean(score)
    
    def math_mean(self):
        score = []
        for student in self.classroom:
            score.append(student.get_score('math'))
        return np.mean(score)
    
    def exam(self,subject):
        if subject in self.subject():
            return str("해당 과목은 이미 존재합니다.")
        else: 
            for student in self.classroom:
                student.set_score(subject, random.randint(0,100))
            return '\n'.join(str(student) for student in self.classroom)
        
    def exam_change(self,subject,name,score):
        if subject in self.subject():
            for student in self.classroom:
                if student.name == name:
                    student.set_score(subject, score)
                    return ("점수가 변경되었습니다. ", student.get_score(subject))
        else:
            return str('해당 과목이 존재하지 않습니다.')
    
    def subject(self):
        return list(self.classroom[0].get_score_list().keys())


'''
A = Student('황준하',25, 90, 10, 0)
B = Student('황준하',25, 80, 20, 1)
C = Student('황준하',25, 70, 30, 2)
D = Student('황준하',25, 60, 40, 3)

student = [A,B,C,D]

C = Classroom(student)
print(C.exam('kor'))
print(C.subject())
print(C.exam_change('중국어','황준하',30))

print(C)

print(C.sort_by_kor())
print(C.sort_by_eng())
print(C.sort_by_math())

print(C.kor_mean())
'''