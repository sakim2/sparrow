student_info = {'홍길동': 1234, '철수': 5678, '영희': 9100}
student_name = input("학생 이름을 입력하세요: ")

for d_name in student_info.keys():
    if student_name == d_name:
        student_number = student_info[d_name]
        print("이름 : %s" %(student_name))
        print("학번 : %s" %(student_number))
        break 