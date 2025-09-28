# ex1

txt = "Code Journey"
print(txt.index("o"))        # 1
# print(txt.index("x"))      # ValueError

txt = "Code Journey"
print(txt.find("o"))         # 1
print(txt.find("x"))         # -1


name = "Python"
print(name.rjust(10, '-'))   # ----Python
print(name.ljust(10, '*'))   # Python****


text = "Hello\nWorld\nPython"
print(text.splitlines())     # ['Hello', 'World', 'Python']


line = "Name\tAge\tCity"
print(line.expandtabs(4))
# Name    Age    City


s = "Python3"
print(s.index("t"))          # 2
print(s.find("x"))           # -1
print(s.rjust(12, '.'))      # ......Python3
print("Line1\nLine2".splitlines())  # ['Line1', 'Line2']
print("Data\tScience".expandtabs(4)) # Data    Science
print("Hello World".istitle())       # True
print("123".isdigit())               # True

