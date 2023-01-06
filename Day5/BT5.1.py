friends = ["Jen", "Jack", "Kenny", "Jelly", "Bob", "Henry", "Anne"]
#a. Lấy ra 4 người bạn đầu tiên trong friends
a_friends = friends[0:4]
print(a_friends)
#b. Lấy ra 4 người bạn cuối trong friends
b_friends = friends[3:]
print(b_friends)
#c. Đảo ngược danh sách friends
c_friends = friends[::-1]
print(c_friends)
#d. Lấy ra những người bạn từ vị trí 1 đến hết
d_friends = friends[1:]
print(d_friends)
#e. Copy danh sách ban đầu thành một danh sách mới
friends2 = friends.copy()
print(friends2 is friends)
#f. Lấy ra những người bạn từ vị trí 2 đến sát cuối
f_friends = friends[1:-1]
print(f_friends)