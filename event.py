import random

class Event:
    def __init__(self, school):
        self.school = []
        self.enroll(school)
        
    def enroll(self,school):
        for classroom in school:
            self.school.append(classroom)
    
    def transfer(self):
        class_random = 0
        student_random = 0
        class_random = random.randrange(0,len(self.school))
        student_random = random.randrange(0, len(self.school[class_random-1].classroom))
        print(self.school[class_random].classroom[student_random].get_name(),"가 전학을 갔습니다.") # 이름 : 오파바, 나이 : 10, 성적 : {'kor': 77, 'eng': 84, 'math': 74}
        self.school[class_random].classroom[student_random].set_in_school(0)
        return self.school[class_random].classroom[student_random]
    
    def exam(self):
        subject = random.randrange(0,1000)
        print("{0} 시험을 봅니다.".format(str(subject)))
        for classroom in self.school:
            classroom.exam(str(subject))
        return
            
    def late(self):
        class_random = 0
        student_random = 0
        class_random = random.randrange(0,len(self.school))
        student_random = random.randrange(0, len(self.school[class_random-1].classroom))
        self.school[class_random].classroom[student_random].set_attendence(0)
        print(self.school[class_random].classroom[student_random].get_name(),"이/가 지각하였습니다.")
        return self.school[class_random].classroom[student_random]
        
    def dayoff(self):
        print("오늘은 즐거운 휴일 !")
        for classroom in self.school:
            for student in classroom.classroom:
                student.set_attendence(0)
        return
    
    def event_occur(self):
        num = random.randrange(1,101)
        count = random.randrange(1,10)
        if num%3 == 0: # 지각
            for i in range(count):
                self.late()
        if num%5 == 0: # 시험
            for i in range(count%4):
                self.exam()        
        if num%13 == 0: # 전학
            for i in range(count):
                self.transfer()
       # if num %11 == 0: # 공휴일
        #    for i in range(count):
         #       self.dayoff()