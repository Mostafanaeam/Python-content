x = 10
y = -7
print(type(x))  # <class 'int'>



pi = 3.14159
temp = -2.5
print(type(pi))  # <class 'float'>


z = 5 + 6j
print(type(z))  # <class 'complex'>
print(z.real)   # الجزء الحقيقي: 5.0
print(z.imag)   # الجزء التخيلي: 6.0



a = 5
print(float(a))   # 5.0  (int → float)

b = 7.8
print(int(b))     # 7    (float → int)  ⚠️ يقرب لأسفل دائمًا

c = 4
print(complex(c)) # (4+0j) (int → complex)



z = 3 + 4j
# int(z)  ❌ يسبب خطأ
# float(z) ❌ يسبب خطأ


