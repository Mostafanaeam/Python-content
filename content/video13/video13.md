# 🎬 الفيديو 013 – دوال السلاسل النصية: الجزء الأول (String Methods – Part One)

## 📚 المحتوى والشرح
**الدوال (Methods)** هي وظائف مدمجة تُنفّذ عمليات معيّنة على النصوص بسهولة ودون كتابة منطق معقد.

---

### 1️⃣ دالة `len()`
- ليست خاصة بالنصوص فقط، لكنها تعيد **عدد العناصر** في أي كائن قابل للتكرار.
```python
text = "Code Journey"
print(len(text))  # 12
```

---

### 2️⃣ إزالة المسافات البيضاء (Strip Methods)

* **strip()**: تزيل المسافات البيضاء من البداية والنهاية.
* **lstrip()**: من اليسار فقط.
* **rstrip()**: من اليمين فقط.
* يمكن تمرير أحرف مخصّصة لإزالتها.

```python
txt = "   hello   "
print(txt.strip())   # "hello"
print(txt.lstrip())  # "hello   "
print(txt.rstrip())  # "   hello"

marks = "---Python---"
print(marks.strip("-"))  # "Python"
```

---

### 3️⃣ تحويل حالة الأحرف (Case Transformation)

* **capitalize()**: أول حرف كبير والباقي صغير.
* **title()**: أول حرف من كل كلمة كبير.
* **upper()**: كل الأحرف كبيرة.
* **lower()**: كل الأحرف صغيرة.

```python
s = "hello world"
print(s.capitalize())  # Hello world
print(s.title())       # Hello World
print(s.upper())       # HELLO WORLD
print(s.lower())       # hello world
```

---

### 4️⃣ دالة `zfill()`

* تضيف أصفارًا في بداية النص للوصول لطول محدد.
* مفيدة لتنسيق الأرقام (مثل أرقام فواتير أو كود).

```python
num = "7"
print(num.zfill(3))   # 007

id_str = "123"
print(id_str.zfill(6))  # 000123
```

---

## 💻 أمثلة عملية

```python
data = "   Code Journey   "
print(len(data.strip()))      # 12
print("hello".upper())        # HELLO
print("42".zfill(5))          # 00042
```

---

## 📝 تاسكات تدريبية

1. احسب طول النص `"   Python  "` بعد إزالة المسافات البيضاء.
2. أنشئ نصًا بعنوان كتابك المفضل واجعله بحروف كبيرة بالكامل.
3. استخدم `zfill()` لتحويل `"15"` إلى `"00015"`.

---

## 🔚 خاتمة

هذه الدوال توفر وقتًا كبيرًا وتُسهل التعامل مع النصوص، وهي أدوات أساسية لكل مبرمج.

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
