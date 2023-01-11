art_students = {"John", "Max", "Anna", "Bob", "Obito"}
math_students = {"Max", "Mery", "David", "Anna", "Naruto", "John"}

#Tìm những người bạn học cả vẽ lẫn toán
art_math_students = art_students.intersection(math_students)
print(art_math_students)
print(art_students & math_students) #toán tử


#Tìm những người bạn học vẽ nhưng không học toán
set2 = art_students.difference(math_students)
print(set2)
print(art_students-math_students) #Toán tử

#Tìm những người bạn học toán nhưng không học vẽ
set3 = math_students.difference(art_students)
print(set3)
print(math_students-art_students) #Toán tử

#Tìm những người bạn học vẽ hay toán không phải cả hai
set4 = art_students.symmetric_difference(math_students)
print(set4)
print(art_students^math_students) #toán tử

#Tìm tất cả những người bạn
set5 = art_students.union(math_students)
print(set5)
print(art_students|math_students)
