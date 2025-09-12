# 🎬 الفيديو 015 – دوال السلاسل النصية: الجزء الثالث (String Methods – Part Three)

## 📚 المحتوى والشرح
استكمالًا للدروس السابقة، نغطي هنا مجموعة جديدة من الدوال المفيدة للتعامل مع النصوص، خاصة للبحث، التنسيق، والتحقق.

---

### 1️⃣ `index()`
- ترجع **فهرس أول ظهور** لسلسلة فرعية.
- تقبل وسيط السلسلة الفرعية، ويمكن تحديد النطاق (start, end).
- إذا لم يتم العثور على السلسلة → تُطلق **ValueError**.

```python
txt = "Code Journey"
print(txt.index("o"))        # 1
# print(txt.index("x"))      # ValueError
```

---

### 2️⃣ `find()`

* مثل `index()` لكن تعيد **-1** إذا لم يتم العثور على السلسلة.

```python
txt = "Code Journey"
print(txt.find("o"))         # 1
print(txt.find("x"))         # -1
```

---

### 3️⃣ `rjust()` و `ljust()`

* **rjust(width, fillchar)**: محاذاة النص لليمين وإضافة أحرف حشوة على اليسار.
* **ljust(width, fillchar)**: محاذاة النص لليسار وإضافة أحرف حشوة على اليمين.
* `fillchar` اختياري (افتراضي: مسافة).

```python
name = "Python"
print(name.rjust(10, '-'))   # ----Python
print(name.ljust(10, '*'))   # Python****
```

---

### 4️⃣ `splitlines()`

* تقسيم النص إلى قائمة من **الأسطر** بناءً على فواصل الأسطر مثل `\n`.

```python
text = "Hello\nWorld\nPython"
print(text.splitlines())     # ['Hello', 'World', 'Python']
```

---

### 5️⃣ `expandtabs()`

* استبدال أحرف الجدولة `\t` بمسافات.
* يمكن تحديد عدد المسافات (الافتراضي 8).

```python
line = "Name\tAge\tCity"
print(line.expandtabs(4))
# Name    Age    City
```

---

### 6️⃣ دوال التحقق (Is Methods)

تُستخدم للتأكد من خصائص النص:

| الدالة      | الوصف                                        | مثال                             |
| ----------- | -------------------------------------------- | -------------------------------- |
| `istitle()` | True إذا كانت كل كلمة تبدأ بحرف كبير.        | `"Hello World".istitle()` → True |
| `islower()` | True إذا كانت كل الأحرف صغيرة.               | `"hello".islower()` → True       |
| `isupper()` | True إذا كانت كل الأحرف كبيرة.               | `"HELLO".isupper()` → True       |
| `isspace()` | True إذا احتوت السلسلة على مسافات بيضاء فقط. | `"   ".isspace()` → True         |
| `isdigit()` | True إذا كانت السلسلة كلها أرقام.            | `"12345".isdigit()` → True       |
| `isalpha()` | True إذا كانت السلسلة كلها أحرف فقط.         | `"Python".isalpha()` → True      |
| `isalnum()` | True إذا كانت السلسلة أحرف وأرقام فقط.       | `"Python3".isalnum()` → True     |

---

## 💻 أمثلة عملية

```python
s = "Python3"
print(s.index("t"))          # 2
print(s.find("x"))           # -1
print(s.rjust(12, '.'))      # ......Python3
print("Line1\nLine2".splitlines())  # ['Line1', 'Line2']
print("Data\tScience".expandtabs(4)) # Data    Science
print("Hello World".istitle())       # True
print("123".isdigit())               # True
```

---

## 📝 تاسكات تدريبية

1. استخدم `find()` للبحث عن الحرف `"o"` في `"Code Journey"` واطبع النتيجة.
2. اجعل كلمة `"Developer"` محاذاة لليمين بطول 15 مع حشوة `*`.
3. حوّل النص `"Name\tAge\tRole"` بحيث يتمدد الجدول إلى 6 مسافات.
4. اكتب برنامج يتحقق إذا كانت `"PYTHON"` كلها حروف كبيرة فقط.

---

## 🔚 خاتمة

هذه المجموعة من الدوال تمنحك مرونة قوية للبحث عن النصوص، تنسيقها، والتحقق من خصائصها بكفاءة.

---


## 💡 عني وطرق التواصل


أنا مصطفى عبد النعيم، مؤسس **Code Journey**.
بشتغل على تمكين الناس من دخول عالم البرمجة بخطوات عملية وواضحة.


### شخصيًا
- 💬 واتساب: [اضغط هنا](https://wa.me/201114938410)
- 📧 الإيميل: mnaeam10@gmail.com  
- 🌐 [الموقع الرسمي](https://mostafa-naeam-web.vercel.app/)  
- 💼 [LinkedIn](https://www.linkedin.com/in/mostafa-naeam/)

### مع Code Journey
- 💬 واتساب: [اضغط هنا](https://wa.me/201555303227)
- 📩 البريد الرسمي: codejourney02@gmail.com  
- 💼 [LinkedIn – Code Journey](https://www.linkedin.com/company/code-journey25/)


## 🛡 حقوق الملكية الفكرية

<img src="../images/1.png" alt="حقوق الملكية" width="100"/>

© 2025 Code Journey. جميع الحقوق محفوظة.  

- الاستخدام شخصي وتعليمي فقط.  
- لا يُسمح بالنسخ أو النشر أو التوزيع دون إذن كتابي.  
- يمكن الاقتباس مع ذكر المصدر ورابط مباشر.  
- أي تعديل أو إعادة استخدام يحتاج موافقة مسبقة.  

> احترم حقوق الملكية لدعم استمرار وتطوير هذا المشروع التعليمي.
