import random


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lesson(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return print('Ошибка')

    def __avg_grades(self, sum_grades=0, amount_grades=0):
        for hw_grades in self.grades.values():
            amount_grades += len(hw_grades)
            for all_grades in hw_grades:
                sum_grades += all_grades
        if amount_grades > 0:
            return round(sum_grades / amount_grades, 2)
        else:
            return 'Нет оценок'

    def __str__(self):
        res = f'Имя: {self.name}\n' \
              f'Фамилия: {self.surname}\n' \
              f'Средняя оценка за домашнее задание: {self.__avg_grades()}\n' \
              f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n' \
              f'Завершенные курсы: {", ".join(self.finished_courses)}'
        return res

    @staticmethod
    def __compare(other):
        if not isinstance(other, Student):
            return print('Ошибка! Сравнение разных классов')

    def __lt__(self, other):
        self.__compare(other)
        return self.__avg_grades() < other.__avg_grades()

    def __le__(self, other):
        self.__compare(other)
        return self.__avg_grades() <= other.__avg_grades()

    def __eq__(self, other):
        self.__compare(other)
        return self.__avg_grades() == other.__avg_grades()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __avg_grades(self, sum_grades=0, amount_grades=0):
        for lesson_grades in self.grades.values():
            amount_grades += len(lesson_grades)
            for all_grades in lesson_grades:
                sum_grades += all_grades
        if amount_grades > 0:
            return round(sum_grades / amount_grades, 2)
        else:
            return 'Нет оценок'

    def __str__(self):
        res = f'Имя: {self.name}\n' \
              f'Фамилия: {self.surname}\n' \
              f'Средняя оценка за лекции: {self.__avg_grades()}'
        return res

    @staticmethod
    def __compare(other):
        if not isinstance(other, Lecturer):
            return print('Ошибка! Сравнение разных классов')

    def __lt__(self, other):
        self.__compare(other)
        return self.__avg_grades() < other.__avg_grades()

    def __le__(self, other):
        self.__compare(other)
        return self.__avg_grades() <= other.__avg_grades()

    def __eq__(self, other):
        self.__compare(other)
        return self.__avg_grades() == other.__avg_grades()


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return print('Ошибка')

    def __str__(self):
        res = f'Имя: {self.name}\n' \
              f'Фамилия: {self.surname}'
        return res


def avg_stud_course(stud, check_course, sum_grades=0, amount_grades=0):
    stud = all_student
    for i in range(len(all_student)):
        if check_course in all_student[i].courses_in_progress:
            amount_grades += len(all_student[i].grades.get(check_course))
            for grades in all_student[i].grades.get(check_course):
                sum_grades += grades
    return print(f'Средняя оценка студентов по предмету {check_course}: {round(sum_grades / amount_grades, 2)}')


def avg_lecturer_course(lecturer, check_course, sum_grades=0, amount_grades=0):
    stud = all_lecturer
    for i in range(len(all_lecturer)):
        if check_course in all_lecturer[i].courses_attached:
            amount_grades += len(all_lecturer[i].grades.get(check_course))
            for grades in all_lecturer[i].grades.get(check_course):
                sum_grades += grades
    return print(f'Средняя оценка преподавателей по предмету {check_course}: {round(sum_grades / amount_grades, 2)}')


student1 = Student('Igor', 'Ivanov', 'Male')
student2 = Student('Luda', 'Petrova', 'Woman')
lector1 = Lecturer('Alex', 'Bardin')
lector2 = Lecturer('Oleg', 'Bulygin')
reviewer1 = Reviewer('Misha', 'One')
reviewer2 = Reviewer('Petya', 'Two')


student1.finished_courses = ['Java']
student2.finished_courses = ['GameDev', 'DevOps']
student1.courses_in_progress = ['Git', 'Python', 'Telegram Bot']
student2.courses_in_progress = ['Python', 'JS', 'React']
lector1.courses_attached = ['Git', 'Python', 'JS']
lector2.courses_attached = ['Python', 'JS']
reviewer1.courses_attached = ['Git', 'Python']
reviewer2.courses_attached = ['Python', 'JS']

student1.rate_lesson(lector1, 'Python', random.randint(1, 10))
student1.rate_lesson(lector2, 'Python', random.randint(1, 10))
student2.rate_lesson(lector1, 'Python', random.randint(1, 10))
student2.rate_lesson(lector2, 'JS', random.randint(1, 10))

reviewer1.rate_hw(student1, 'Python', random.randint(1, 10))
reviewer1.rate_hw(student2, 'Python', random.randint(1, 10))
reviewer2.rate_hw(student1, 'Python', random.randint(1, 10))
reviewer2.rate_hw(student2, 'JS', random.randint(1, 10))


def show(who):
    if isinstance(who, Student) or isinstance(who, Lecturer):
        for i, j in who.grades.items():
            print(f'Оценки за предмет {i}: {j}')
    return


all_student = [student1, student2]
all_lecturer = [lector1, lector2]

print(student1)
show(student1)
print('\n')
print(student2)
show(student2)
print('\n')
print(lector1)
show(lector1)
print('\n')
print(lector2)
show(lector2)
print('\n')
print(reviewer1)
print('\n')
print(reviewer2)
print('\n')

print(f'student1 > student2 - {student1 > student2}')
print(f'student1 >= student2 - {student1 >= student2}')
print(f'student1 == student2 - {student1 == student2}')
print(f'student1 < student2 - {student1 < student2}')

avg_stud_course(all_student, 'Python')
avg_lecturer_course(all_lecturer, 'Python')