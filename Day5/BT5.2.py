students = [["SV001", "Bob", 23], ["SV002", "Kenny", 34], ["SV003", "Henry", 45]]
#a. Lấy ra thông tin của sinh viên thứ nhất và in ra định dạng "ID: {id}, name: {name} - age: {age}"
a_student = students[0]
print("ID:", {a_student[0]}) #copy xuống dòng Shift + Alt + Mũi tên xuống
print("name:", {a_student[1]})
print("age:", {a_student[-1]})
#b. Lấy ra tuổi của sinh viên thứ hai
print(students[1][-1])
#c. Lấy ra thông tin hai sinh viên cuối cùng
c_students = (students[1:])
print(c_students[0])
print(c_students[-1])
#d. Lấy ra id của sinh viên thứ ba
print(students[-1][0])