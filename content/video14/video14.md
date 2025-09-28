
# 🎬 الفيديو 014 – دوال السلاسل النصية: الجزء الثاني (String Methods – Part Two)

## 📚 المحتوى والشرح
في هذا الجزء نستكمل أهم الدوال المدمجة للتعامل مع النصوص، مما يسهل عمليات البحث، التقسيم، والتحقق.

---

### 1️⃣ `split()`
- تقسيم النص إلى **قائمة (List)** بناءً على فاصل محدد (افتراضيًا: المسافة).
- يمكنك تحديد **maxsplit** لتحديد أقصى عدد من عمليات التقسيم.

```python
txt = "Code Journey Python"
print(txt.split())          # ['Code', 'Journey', 'Python']
print(txt.split(" ", 1))    # ['Code', 'Journey Python']
```

---

### 2️⃣ `rsplit()`

* مثل `split()` لكن يبدأ التقسيم من **اليمين**.

```python
txt = "a-b-c-d"
print(txt.rsplit("-", 2))   # ['a-b', 'c', 'd']
```

---

### 3️⃣ `center()`

* يضع النص في **الوسط** مع إضافة أحرف حشوة (Padding).
* الوسيط الأول: الطول الكلي المطلوب.
* الوسيط الثاني: حرف الحشوة (افتراضيًا: مسافة).

```python
word = "Python"
print(word.center(10))        # '  Python  '
print(word.center(10, '*'))   # '**Python**'
```

---

### 4️⃣ `count()`

* يحسب عدد مرات ظهور نص فرعي محدد.
* يمكن تحديد نطاق: **start** و **end**.

```python
s = "banana"
print(s.count("a"))           # 3
print(s.count("a", 2, 5))     # 2
```

---

### 5️⃣ `swapcase()`

* يحوّل الحروف الكبيرة إلى صغيرة والعكس.

```python
s = "Code Journey"
print(s.swapcase())           # cODE jOURNEY
```

---

### 6️⃣ `startswith()`

* يتحقق إن كانت السلسلة تبدأ بنص فرعي محدد.
* يعيد **True** أو **False**.
* يمكن تحديد **start** و **end**.

```python
name = "Code Journey"
print(name.startswith("Code"))         # True
print(name.startswith("Journey", 5))   # True
```

---

### 7️⃣ `endswith()`

* يتحقق إن كانت السلسلة تنتهي بنص فرعي محدد.
* يعيد **True** أو **False**.
* يدعم تحديد النطاق.

```python
name = "Code Journey"
print(name.endswith("Journey"))        # True
print(name.endswith("Code", 0, 4))     # True
```

---

## 💻 أمثلة عملية

```python
text = "Learn Python Now"
print(text.split())               # ['Learn', 'Python', 'Now']
print(text.center(20, '-'))       # ---Learn Python Now---
print(text.count("n"))            # 2
print(text.swapcase())            # lEARN pYTHON nOW
print(text.startswith("Learn"))   # True
print(text.endswith("Now"))       # True
```

---

## 📝 تاسكات تدريبية

1. استخدم `split()` لتقسيم الجملة `"Code Journey is Great"` إلى ثلاث كلمات.
2. ضع كلمة `"Developer"` في المنتصف بعرض 15 وحشوة `#`.
3. احسب عدد حروف `"e"` في `"experience"`.
4. اكتب برنامج يتحقق هل الجملة `"Hello World"` تنتهي بكلمة `"World"`.

---

## 🔚 خاتمة

هذه الدوال تمنحك تحكمًا أقوى في النصوص، من البحث والتقسيم إلى التنسيق والتحقق.

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

<img src="../../images/1.png" alt="حقوق الملكية" width="100"/>


© 2025 Code Journey. جميع الحقوق محفوظة.  

- الاستخدام شخصي وتعليمي فقط.  
- لا يُسمح بالنسخ أو النشر أو التوزيع دون إذن كتابي.  
- يمكن الاقتباس مع ذكر المصدر ورابط مباشر.  
- أي تعديل أو إعادة استخدام يحتاج موافقة مسبقة.  

> احترم حقوق الملكية لدعم استمرار وتطوير هذا المشروع التعليمي.
