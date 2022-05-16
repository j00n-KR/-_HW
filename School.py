# from Student import Student
# from Classroom import Classroom
import numpy as np

class School:
    def __init__(self, classroom):
        self.school = []
        self.enroll(classroom)
    
    def __repr__(self):
        return self.school
    
    def __str__(self):
        return '\n'.join(str(classroom) for classroom in self.school)

    def enroll(self,Classroom):
        for classroom in Classroom.classroom:
            self.school.append(classroom)
            
    def kor_mean(self):
        score = []
        for classroom in self.school:
            score.append(classroom.get_score('kor'))
        return np.mean(score)
    
    def eng_mean(self):
        score = []
        for classroom in self.school:
            score.append(classroom.get_score('eng'))
        return np.mean(score)
    
    def math_mean(self):
        score = []
        for classroom in self.school:
            score.append(classroom.get_score('math'))
        return np.mean(score)

"""
A = Student('황준하',25, 90, 10, 0)
B = Student('황준하',25, 80, 20, 1)
C = Student('황준하',25, 70, 30, 2)
D = Student('황준하',25, 60, 40, 3)

student = [A,B,C,D]

C1 = Classroom(student)
C2 = Classroom(student)
C3 = Classroom(student)

classroom = [C1, C2, C3]

S = School(classroom)

print(S)

print("국어 평균 : ",S.kor_mean())
print("영어 평균 : ",S.eng_mean())
print("수학 평균 : ",S.math_mean())
"""