student_list = []
def student_data():
    student_name = input("enter the name of the student :\t")
    student_class = int(input("standard :\t"))
    student_record = {
          "name": student_name,
          "mark": [],
          "std" : student_class
    }
    return(student_record)


def add_student_mark(student):
    number = int(input("number of subject :"))
    while number==0:
        return 0
    if number !=0:
        for j in range(1,number+1):
            marks = int(input("enter the {} subject mark :".format(j)))
            student['mark'].append(marks)
def student_average(student):
    num = len(student['mark'])
    if num==0:
        return 0
    total = sum(student['mark'])
    average = total/num
    return(average)
   

def student_details(student):    
    print("Name :{}, class:{} std,  marks: {}, average mark is :{}".format(student['name'],student['std'],student['mark'],student_average(student)))

def print_student_list(students):
    for student in students:
        student_details(student)
    
  
def menu():
    print("welcome to the student open house")
    print("a----> add the student to the record\nm----> add the marks\np---->find the average of the student\n"
           "q----> quit the record  ")
    user_input = input("enter your option : ")
    while user_input != 'q':
        if user_input == 'a':
            student_list.append(student_data())
            user_input = input("enter your option : ")
        elif user_input == 'm':
            number = int(input("enter the student ID, to enter the marks of the student"))
            student = student_list[number]
            add_student_mark(student) 
            user_input = input("enter your option : ")
        elif user_input =='p':
            print_student_list(student_list)
            user_input = input("enter your option : ")

menu()


