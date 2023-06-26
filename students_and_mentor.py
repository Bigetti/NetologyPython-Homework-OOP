class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_for_l(self, lecturer, course, grade):
        if isinstance(lecturer, Mentor) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.rate_fr_st:
                lecturer.rate_fr_st[course] += [grade]
            else:
                lecturer.rate_fr_st[course] = [grade]
        else:
            return 'Mistake'
        
    def get_average_rate_hw(self):
        total_grades = 0  # Переменная для хранения общей суммы оценок
        total_count = 0  # Переменная для хранения общего количества оценок
        for rates_list in self.grades.values():  # Перебираем списки оценок в словаре
            total_grades += sum(rates_list)  # Добавляем сумму оценок в общую сумму
            total_count += len(rates_list)  # Увеличиваем общее количество оценок
        if total_count == 0:
            return 0  # Возвращаем 0, если нет оценок
        average_rate = total_grades / total_count  # Вычисляем среднюю оценку
        return average_rate


    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.get_average_rate_hw()}\nКурсы в процессе изучения: {self.courses_in_progress}\nЗавершенные курсы: {self.finished_courses}'
        return res
        
    def __lt__(self, other):
        return self.get_average_rate_hw() < other.get_average_rate_hw()


    def __gt__(self, other):
        return self.get_average_rate_hw() > other.get_average_rate_hw()


    def __eq__(self, other):
        return self.get_average_rate_hw() == other.get_average_rate_hw()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course].append(grade)
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
        
        

    
        
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        # self.courses_attached = []
        self.rate_fr_st = {}
       

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.get_average_grade()}'
        return res
    

    
        
    def get_average_grade(self):
        total_grades = 0  # Переменная для хранения общей суммы оценок
        total_count = 0  # Переменная для хранения общего количества оценок
        for grades_list in self.rate_fr_st.values():  # Перебираем списки оценок в словаре
            total_grades += sum(grades_list)  # Добавляем сумму оценок в общую сумму
            total_count += len(grades_list)  # Увеличиваем общее количество оценок
        if total_count == 0:
            return 0  # Возвращаем 0, если нет оценок
        average_grade = total_grades / total_count  # Вычисляем среднюю оценку
        return average_grade


    def __lt__(self, other):
        return self.get_average_grade() < other.get_average_grade()


    def __gt__(self, other):
        return self.get_average_grade() > other.get_average_grade()


    def __eq__(self, other):
        return self.get_average_grade() == other.get_average_grade()

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
    #     # self.courses_attached = []
        

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Mistake'
        

    def __str__(self):
        res = f'Имя:{self.name}\nФамилия:{self.surname},\nкурсы:{self.courses_attached}'
        return res
    
   
        
        

student1 = Student('Kos', 'Barbos', 'male')
student2 = Student('Oleg', 'Kargo', 'male')
student1.courses_in_progress += ['Python']
student1.courses_in_progress += ['C++']
student2.courses_in_progress += ['Python']


reviewer1 = Reviewer('Some', 'Bady')
reviewer2 = Reviewer('Other', 'One')

reviewer1.courses_attached += ['Python']
reviewer1.courses_attached += ['C++']
reviewer2.courses_attached += ['C++']

lecturer1 = Lecturer('Steve', 'Jobs')
lecturer2 = Lecturer('Bill', 'Geyts')
lecturer1.courses_attached += ['Python']
student1.rate_for_l(lecturer2, 'Python', 10)

reviewer1.rate_hw(student1, 'Python', 10)
reviewer1.rate_hw(student2, 'Python', 5)


print(student1)

print(lecturer1 > lecturer2) 
print(lecturer1 == lecturer2) 

print(student1 > student2)
print(student1 == student2)


# print(student1.grades)
# print(reviewer1)
# print(lecturer1.rate_fr_st)
# print(lecturer1)
