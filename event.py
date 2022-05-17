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
        self.school[class_random].classroom[student_random].set_in_school(0)
        return "{0}가 전학을 갔습니다.".format(self.school[class_random].classroom[student_random].get_name())
    
    def exam(self):
        subject = random.randrange(0,1000)
        for classroom in self.school:
            classroom.exam(str(subject))
        return "{0} 시험을 봅니다.".format(str(subject))
            
    def late(self):
        class_random = 0
        student_random = 0
        class_random = random.randrange(0,len(self.school))
        student_random = random.randrange(0, len(self.school[class_random-1].classroom))
        self.school[class_random].classroom[student_random].set_attendence(0)
        return "{0}이/가 지각하였습니다.".format(self.school[class_random].classroom[student_random].get_name())
        
    def dayoff(self):
        for classroom in self.school:
            for student in classroom.classroom:
                student.set_attendence(0)
        return str("은 즐거운 휴일 !")
    
    def event_occur(self):
        num = random.randrange(1,101)
        count = random.randrange(1,10)
        if num%3 == 0: # 지각
            for i in range(count):
                return self.late()
        if num%5 == 0: # 시험
            for i in range(count%4):
                return self.exam()        
        if num%13 == 0: # 전학
            for i in range(count):
                return self.transfer()
        if num %11 == 0: # 공휴일
           return self.dayoff()