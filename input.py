import os.path
from random import *
import random

class Student:
    def __init__(self, name, age, kor, eng, math):
        self.name = name
        self.age = age
        self.kor = kor
        self.eng = eng
        self.math = math
        
    def __str__(self):              # 출력 형태
        return f'이름 : {self.name}, 나이 : {self.age}, 국어 : {self.kor}, 영어 : {self.eng}, 수학 : {self.math}'
    
    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age
    
    def get_kor(self):
        return self.kor
    
    def get_eng(self):
        return self.eng
    
    def get_math(self):
        return self.math
    
    def set_name(self, value):
        self.name = value
        
    def set_age(self, value):
        self.age = value
        
    def set_kor(self, value):
        self.kor = value
        
    def set_eng(self, value):
        self.eng = value
        
    def set_math(self, value):
        self.math = value


class Class:
    def __init__(self):
        self.class_member = []
    
    def __str__(self):              # 학생 명단
        list = []
        for i in self.class_member:
            list.append(i.get_name())
        return str(list)

        
    def enroll(self, student):      # 신규 학생 등록
        self.class_member.append(student)
    
    def info(self):                 # 등록 학생 정보 열람
        for i in self.class_member:
            print("[{0}]".format(i))
    
    def get_student_name(self, student):
        return student.get_name()
            
    def count(self):                # 학생 수
        return len(self.class_member)
    
    def age_mean(self):             # 나이 평균
        total = 0
        count = self.count()
        for i in self.class_member:
            total += i.get_age()
        return total/count
            
    def kor_mean(self):             # 국어 평균
        total = 0
        count = self.count()
        for i in self.class_member:
            total += i.get_kor()
        return total/count
    
    def eng_mean(self):             # 영어 평균
        total = 0
        count = self.count()
        for i in self.class_member:
            total += i.get_eng()
        return total/count
    
    def math_mean(self):            # 수학 평균
        total = 0
        count = self.count()
        for i in self.class_member:
            total += i.get_math()
        return total/count
    
    def sort_by_age(self):         # 나이에 따라 정렬
        sorted_student = sorted(self.class_member, key=lambda x: x.get_age())
        sorted_by_age = []
        no = 1
        for i in sorted_student:
            sorted_by_age.append({"순위":no,i.get_name():i.get_age()})
            no += 1
        return sorted_by_age
    
    def sort_by_kor(self):         # 국어 성적에 따라 정렬
        sorted_student = sorted(self.class_member, key=lambda x: x.get_kor(), reverse=True)
        sorted_by_kor = []
        no = 1
        for i in sorted_student:
            sorted_by_kor.append({"순위":no,i.get_name():i.get_kor()})
            no += 1
        return sorted_by_kor
    
    def sort_by_eng(self):         # 영어 성적에 따라 정렬
        sorted_student = sorted(self.class_member, key=lambda x: x.get_eng(), reverse=True)
        sorted_by_eng = []
        no = 1
        for i in sorted_student:
            sorted_by_eng.append({"순위":no,i.get_name():i.get_eng()})
            no += 1
        return sorted_by_eng
    
    def sort_by_math(self):         # 수학 성적에 따라 정렬
        sorted_student = sorted(self.class_member, key=lambda x: x.get_math(), reverse=True)
        sorted_by_math = []
        no = 1
        for i in sorted_student:
            sorted_by_math.append({"순위":no,i.get_name():i.get_math()})
            no += 1
        return sorted_by_math

# random

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
    with open(file,'r') as f:
        for line in f:
            S = "STUDENT"
            NO = 1
            (a,b,c,d,e) = line.split(",")
            student = Student(a,int(b),int(c),int(d),int(e))
            Class.enroll(student)
                


# Class Instance 화
Class = Class()

# 입력한 숫자만큼 학생 생성
data = Generator(1000)

# 학생정보를 갖고 Instacne 화 한 후 Class 에 enroll
make_student(data)

# 츨력
print("* 학생명단 *\n",Class,"\n")
print("* 나이 순 *\n",Class.sort_by_age(),"\n")
print("* 국어성적 순 *\n",Class.sort_by_kor(),"\n")
print("* 영어성적 순 *\n",Class.sort_by_eng(),"\n")
print("* 수학성적 순 *\n",Class.sort_by_math(),"\n")

print("국어평균 : {0}, 영어평균 : {1}, 수학평균 : {2}".format(Class.kor_mean(), Class.eng_mean(), Class.math_mean()))