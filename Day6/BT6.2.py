set_a = set()

#a. Thêm 'Anna' vào set_a
set_a.add("Anna")
print(set_a)

#b. Thêm một tuple ('Kenny', 'Jen', 'Danny')
set_a.update(('Kenny', 'Jen', 'Danny'))

#c. In ra set_a và tính chiều dài của nó
print(set_a)
print(len(set_a))

#d. Xóa 'Jen' ra khỏi set_a
set_a.remove('Jen')
print(set_a)

#e. Xóa tất cả các giá trị từ set_a
set_a.clear