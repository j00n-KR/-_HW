class Student:
    def __init__(self, name, age, attendence, in_school, kor, eng, math):
        self.name = name
        self.age = age
        self.attendence = attendence
        self.in_school = in_school
        self.score = {'kor' : kor, 'eng' : eng, 'math' : math}
    
    def __str__(self):
        return f'이름 : {self.name}, 나이 : {self.age}, 성적 : {self.score}'
    
    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age
    
    def get_attendence(self):
        return self.attendence

    def get_in_school(self):
        return self.in_school
    
    def get_score_list(self):
        return self.score

    def get_score(self,key):
        return self.score[key]
    
    def set_score(self,key,value):
        self.score[key] = value
        return self.score[key]
    
    def set_attendence(self,num):
        self.attendence = num
        
    def set_in_school(self,num):
        self.in_school = num

'''
A = Student('황준하',25, 90, 80, 50)

print(type(A.__dict__))
print(A.__dict__)

print(A.score)

print(A)

print(A.get_score('kor'))

print(A.set_score('kor',20))
print(A.get_score('kor'))
'''