class School:
    def __init__(self, school_id):
        self.school_id = school_id

class Human:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

class Teacher(Human):
    def __init__(self, name, surname, speciality):
        super().__init__(name, surname)
        self.speciality = speciality

class Student(Human):
    def __init__(self, name, surname, class_code):
        super().__init__(name,surname)
        self.class_code = Class(class_code)

class Class:
    def __init__ (self, class_code):
        self.class_code = class_code
        self.students_list = list()

    def add_Student(self, name, surname):
        self.students_list.append(Student(name, surname, self.class_code))

    def remove_Student(self, student_id):
        self.students_list.remove(student_id)



class Lesson:
    def __init__(self, lesson_name, teacher):
        self.lesson_name = lesson_name
        self.teacher = Teacher(Human.name, Human.surname, Teacher.speciality) #правильно ли указаны переменные?

class Record:
    def __init__(self, student_name, score, absent = False): #student_name -- объедение name+surname
        self.student_name = Student.surname+Student.name
        self.absent = absent
        self.score = score

class Journal:
    def __init__(self, school_name, class_code):
        self.school_name = School.school_id
        self.class_code = Class.class_code
        self.records_list = list()

    def add_record(self, record):
        self.records_list.append(Record(Student.surname+Student.name, Record.score, absent = False)) #правильно ли указаны параметры и как было бы лучше на них сослаться?

    def remove_record(self, record):
        self.records_list.remove(Record(Student.surname + Student.name, Record.score, absent=False))  # правильно ли указаны параметры и как было бы лучше на них сослаться?

    def update_record(self):
        pass #Миш, давайте вместе напишем этот метод, плиз?

def main ():
    sc1 = School('SCH123')
    h1 = Human('Gohn', 'Golt')
    h2 = Human ('Jack', 'Sparrow')
    h3 = Human('Semil', 'Glas')
    h4 = Human('Erkul', 'Puaro')
    t1 = h1
    s1 = h2
    s2 = h3
    s3 = h4
    cl1 = Class('6A')
    cl1.add_Student(s1)
    cl1.add_Student(s2)
    cl1.remove_Student(s3)
    l1 = ('art', t1)
    r1 = Record(s1, 6, absent = False)
    j1 = Journal(sc1,cl1)


if __name__ == '__main__':
    main()




