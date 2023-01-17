# Nhập vào một số nguyên dương n. Đếm số lượng số chẵn và lẻ trong đoạn [0, n]
odd = even = 0

n = int(input("n = "))

while n <= 0:
    print("n phải là số nguyên dương")
    n = int(input("n = "))

for i in range(n+1):
    if i % 2 == 0:
        even += 1
    else:
        odd += 1

print(odd)
print(even)
