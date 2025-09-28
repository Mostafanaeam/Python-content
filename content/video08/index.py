# ex1

x = 10        #* x نوعه int
x = "Hello"   #* الآن نوعه str
print(type(x))  #* <class 'str'>


import keyword
print(keyword.kwlist)

a, b, c = 1, 2, 3
print(a, b, c)  # 1 2 3


x, y = 5, 10  # ✅
x, y, z = 5, 10  # ❌ ValueError

m = n = p = 0

# ديناميكية النوع
data = 42
print(type(data))  # int
data = 3.14
print(type(data))  # float
data = "Dynamic!"
print(type(data))  # str

# تعيين متعدد
x, y, z = "A", "B", "C"
print(x, y, z)