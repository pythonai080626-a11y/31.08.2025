

def get_number_of_students(min_stud=2, max_stud=50):
    '''
    returns the number of students in the list
    :param min_stud:
    :param max_stud:
    :return: number of students
    '''
    while True:
        number = int(input(f"Enter a number between {min_stud} and {max_stud}: "))
        if min_stud <= number <= max_stud:
            return number
        print('number not in range')

def get_student_names(num_of_stud):
    '''
    returns a list of student names
    :param num_of_stud:
    :return: list of student names
    '''
    names = []
    for i in range(num_of_stud):
        name = input(f"Enter the name of student {i + 1}#: ")
        names.append(name)
    return names

def get_student_grades(num_of_stud):
    grades = []
    for i in range(num_of_stud):
        while True:
            grade = int(input(f"Enter a grades for student {i + 1}#: "))
            if 0 <= grade <= 100:
                break
            print('grades not in range')
        grades.append(grade)
    return grades

def create_dict(names, grades):
    result = {}
    for i in range(len(names)):
        name = names[i]
        garde = grades[i]
        result[name] = garde
    return result

def get_max_name_grade(students):
    max_name = max(students, key=students.get)
    grade = students[max_name]
    return max_name, grade