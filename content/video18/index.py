# ex1

name = "Mostafa"
age = 28
print("My name is {} and I am {} years old.".format(name, age))
# My name is Mostafa and I am 28 years old.


print("{1} {0}".format("World", "Hello"))
# Hello World



num = 12.3456
print("Number: {:>10.2f}".format(num))  # محاذاة يمين وعرض 10 ورقمين عشريين


print("Integer: {:d}".format(42))



name = "Mostafa"
age = 28
print(f"My name is {name} and I am {age} years old.")
# My name is Mostafa and I am 28 years old.


pi = 3.14159
print(f"Pi rounded: {pi:.2f}")          # Pi rounded: 3.14
print(f"{'Hi':^10}")                    # محاذاة وسط بعرض 10


num = 1000000
print(f"{num:,}")   # 1,000,000
print(f"{num:_}")   # 1_000_000



