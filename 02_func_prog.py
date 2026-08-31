
from students_lib import *

num_of_stud = get_number_of_students(min_stud=2, max_stud=50)

list_of_names = get_student_names(num_of_stud)

list_of_grades = get_student_grades(num_of_stud)

dict_students = create_dict(list_of_names, list_of_grades)

max_name, max_grade = get_max_name_grade(dict_students)

print(f"max grade was {max_grade} and the student was {max_name}")