friends = [("Bob", "Male"), ("Anna", "Female"), ("Max", "Male")]

#a. Cho biết chiều dài của friends
print(len(friends))

#b. Lấy ra phần tử đầu, cuối và giữa và kiểm tra kiểu của chúng
first_friends = friends[0]
print(first_friends)
print(type(first_friends))

second_friends = friends[1]
print(second_friends)
print(type(second_friends))

third_friends = friends[-1]
print(third_friends)
print(type(third_friends))

#c. Nhập vào tên (name) và giới tính (gender) của một người bạn sau đó append vào friends tuple gồm hai giá trị (name, gender)
name_Elsa = input("Nhập tên: ")
gender_Elsa = input("Nhập giới tính: ")
friends.append((name_Elsa, gender_Elsa))
print(friends)