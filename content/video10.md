# 🎬 الفيديو 010 – دمج النصوص والتدريب (Concatenation And Training)

## 📚 المحتوى والشرح
في هذا الدرس نتعرف على **دمج السلاسل النصية (Concatenation)** وكيفية التعامل مع النصوص بطرق متنوعة.

---

### 1️⃣ دمج النصوص (String Concatenation)
- **الدمج** يعني ربط سلسلتين نصيتين أو أكثر لتكوين سلسلة واحدة.
- نستخدم **عامل الجمع `+`** لدمج النصوص.
```python
first = "Code"
second = "Journey"
print(first + " " + second)  # Code Journey
```

> 💡 يجب أن تكون جميع الأجزاء نصوصًا (Strings)، وإلا ستحدث **TypeError**.

---

### 2️⃣ تعريف السلاسل النصية

يمكن تعريف النصوص باستخدام:

* علامات اقتباس فردية `'Hello'`
* علامات اقتباس مزدوجة `"Hello"`
* ثلاث علامات اقتباس فردية أو مزدوجة `'''Hello'''` أو `"""Hello"""` لإنشاء نصوص متعددة الأسطر:

```python
multi = """This is
a multi-line
string."""
print(multi)
```

---

### 3️⃣ استخدام علامات الاقتباس داخل النصوص

* لو أردت كتابة اقتباس داخل النص:

  * استخدم نوعًا مختلفًا من علامات الاقتباس.

  ```python
  print("It's a sunny day")
  print('She said "Hi!"')
  ```

  * أو استعمل **تسلسل الهروب** `\`:

  ```python
  print('It\'s a sunny day')
  print("She said \"Hi!\"")
  ```

---

### 4️⃣ السلاسل الخام (Raw Strings)

* ضع الحرف `r` قبل النص لجعل تسلسلات الهروب غير فعالة، ويُطبع النص كما هو.

```python
path = r"C:\new\folder"
print(path)  # C:\new\folder
```

> ⚡ مفيدة جدًا لمسارات الملفات والـ Regex.

---

## 💻 أمثلة عملية

```python
# دمج نصوص
greeting = "Hello"
name = "Mostafa"
print(greeting + ", " + name + "!")

# نص متعدد الأسطر
story = """Line 1
Line 2
Line 3"""
print(story)

# سلاسل خام
regex = r"\d+"
print(regex)  # \d+
```

---

## 📝 تاسكات تدريبية

1. أنشئ متغيرين نصيين (اسم أول واسم عائلة) وادمجهما في نص واحد مع مسافة بينهما.
2. اكتب نصًا متعدد الأسطر يصف هدفك من تعلم بايثون.
3. اطبع مسارًا على جهازك (مثل `C:\Users\YourName`) باستخدام **raw string**.

---

## 🔚 خاتمة

التحكم في النصوص ودمجها من الأساسيات التي ستحتاجها في كل مشروع برمجي، من التعامل مع المدخلات إلى إنشاء واجهات نصية.

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

