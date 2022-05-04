class Student:
    def __init__(self, name, age, kor, eng, math):
        self.name = name
        self.age = age
        self.kor = kor
        self.eng = eng
        self.math = math
        
    def __str__(self):
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
    
    def return_kor(self):
        return 'kor'
    


class Class:
    def __init__(self):
        self.class_member = []
    
    def __str__(self):
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
            
    def count(self):
        return len(self.class_member)
    
    def age_mean(self):
        total = 0
        count = self.count()
        for i in self.class_member:
            total += i.get_age()
        return total/count
            
    def kor_mean(self):
        total = 0
        count = self.count()
        for i in self.class_member:
            total += i.get_kor()
        return total/count
    
    def eng_mean(self):
        total = 0
        count = self.count()
        for i in self.class_member:
            total += i.get_eng()
        return total/count
    
    def math_mean(self):
        total = 0
        count = self.count()
        for i in self.class_member:
            total += i.get_math()
        return total/count
    
    def sort_by_age(self):
        sorted_student = sorted(self.class_member, key=lambda x: x.get_age(), reverse=True)
        sorted_by_age = []
        no = 1
        for i in sorted_student:
            sorted_by_age.append({"순위":no,i.get_name():i.get_age()})
            no += 1
        return sorted_by_age
    
    def sort_by_kor(self):
        sorted_student = sorted(self.class_member, key=lambda x: x.get_kor(), reverse=True)
        sorted_by_kor = []
        no = 1
        for i in sorted_student:
            sorted_by_kor.append({"순위":no,i.get_name():i.get_kor()})
            no += 1
        return sorted_by_kor
    
    def sort_by_eng(self):
        sorted_student = sorted(self.class_member, key=lambda x: x.get_eng(), reverse=True)
        sorted_by_eng = []
        no = 1
        for i in sorted_student:
            sorted_by_eng.append({"순위":no,i.get_name():i.get_eng()})
            no += 1
        return sorted_by_eng
    
    def sort_by_math(self):
        sorted_student = sorted(self.class_member, key=lambda x: x.get_math(), reverse=True)
        sorted_by_math = []
        no = 1
        for i in sorted_student:
            sorted_by_math.append({"순위":no,i.get_name():i.get_math()})
            no += 1
        return sorted_by_math

            
# 학생 설정            
A = Student("황준하", 25, 90, 100, 85)
B = Student("이찬희",26 ,0, 0, 0)

# Class 설정
Class = Class()
Class.enroll(A)
Class.enroll(B)
Class.info()
print(Class)

print(Class.sort_by_age())