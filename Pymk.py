import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1, 1, 50)# 从(-1,1)均匀取50个点
y = 2 * x

plt.plot(x, y)
plt.show()

x = np.linspace(-1, 1, 50)
y1 = x ** 2
y2 = x * 2
# 这个是第一个figure对象,下面的内容都会在第一个figure中显示
plt.figure()
plt.plot(x, y1)
# 这里第二个figure对象
plt.figure(num=3, figsize=(10, 5))
plt.plot(x, y2)
plt.show()

# Fibonacci series: 斐波纳契数列
# 两个元素的总和确定了下一个数
a, b = 0, 1
while b < 10:
    print(b)
    a, b = b, a+b


# 计算面积函数
def area(width, height):
    return width * height


def print_welcome(name):
    print("Welcome", name)


print_welcome("Runoob")
w = 4
h = 5
print("width =", w, " height =", h, " area =", area(w, h))


# 更新