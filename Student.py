class Student:
    def __init__(self, name, age, kor, eng, math):
        self.name = name
        self.age = age
        self.score = {'kor' : kor, 'eng' : eng, 'math' : math}
    
    def __str__(self):
        return f'이름 : {self.name}, 나이 : {self.age}, 성적 : {self.score}'
    
    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age
    
    def get_score_list(self):
        return self.score

    def get_score(self,key):
        return self.score[key]
    
    def set_score(self,key,value):
        self.score[key] = value
        return self.score[key]

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