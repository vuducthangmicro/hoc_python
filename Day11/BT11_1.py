# Định nghĩa 4 hàm add, subtract, divide, multiply (+, -, /, *).
# Mỗi hàm nhận vào hai tham số thực hiện lần lượt các phép toán cộng, trừ, chia, nhân. Lưu ý hàm nên trả về thay vì in ra.

# add
def my_add(x, y):
    return x + y


print(my_add(6, 3))


# subtract
def my_subtract(a, b):
    return a - b


print(my_subtract(6, 3))

# divide


def my_divide(c, d):
    if d != 0:
        return c / d
    return "divide by zero"


print(my_divide(6, 3))

# multiply


def my_multiply(e, f):
    return e * f


print(my_multiply(6, 3))
