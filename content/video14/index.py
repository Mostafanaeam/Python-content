# ex1

txt = "Code Journey Python"
print(txt.split())          # ['Code', 'Journey', 'Python']
print(txt.split(" ", 1))    # ['Code', 'Journey Python']


txt = "a-b-c-d"
print(txt.rsplit("-", 2))   # ['a-b', 'c', 'd']


word = "Python"
print(word.center(10))        # '  Python  '
print(word.center(10, '*'))   # '**Python**'


s = "banana"
print(s.count("a"))           # 3
print(s.count("a", 2, 5))     # 2


s = "Code Journey"
print(s.swapcase())           # cODE jOURNEY


name = "Code Journey"
print(name.startswith("Code"))         # True
print(name.startswith("Journey", 5))   # True


name = "Code Journey"
print(name.endswith("Journey"))        # True
print(name.endswith("Code", 0, 4))     # True


text = "Learn Python Now"
print(text.split())               # ['Learn', 'Python', 'Now']
print(text.center(20, '-'))       # ---Learn Python Now---
print(text.count("n"))            # 2
print(text.swapcase())            # lEARN pYTHON nOW
print(text.startswith("Learn"))   # True
print(text.endswith("Now"))       # True


