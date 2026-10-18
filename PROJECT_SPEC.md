\# PROJECT SPEC — Tabular ML Prediction API



\## عنوان پروژه

Tabular ML Prediction API



\## هدف

آموزش یک مدل Classification روی داده‌های ساختاریافته و ارائه‌ی پیش‌بینی از طریق یک API.



\## Problem Definition

\### Problem Type

Classification (دسته‌بندی دوتایی / Binary classification)



\### Objective

Predict the target class from tabular numerical features.

(پیش‌بینی کلاس هدف از روی ویژگی‌های عددی جدولی)



\### Input

A set of numerical features describing one sample.

(۳۰ ویژگی عددی استخراج‌شده از تصاویر نمونه‌های توده‌ی پستان: مثل radius, texture, perimeter, area, smoothness و...)



\### Target

The target class provided by the dataset:

\- 0 = malignant (بدخیم)

\- 1 = benign (خوش‌خیم)



\### Output

A predicted class and, if supported by the model, class probabilities.

(پیش‌بینی کلاس — یعنی 0 یا 1 — و در صورت پشتیبانی مدل، احتمال هر کلاس)



\### Evaluation

The final evaluation metrics will be selected based on the problem and class distribution.

(معیارهای ارزیابی اولیه: Accuracy, Precision, Recall, F1-Score — انتخاب معیار نهایی بر اساس هزینه‌ی خطا و ساختار مسئله)



\### Limitations

\- This is an educational machine learning project.

\- It is not intended for medical diagnosis or clinical use.

\- این پروژه صرفاً آموزشی است و مدل ساخته‌شده ابزار تشخیص پزشکی محسوب نمی‌شود.

\- نباید برای تصمیم‌گیری بالینی واقعی استفاده شود.

\- محدودیت در تعمیم‌پذیری مدل به جمعیت‌های دیگر.

\- کیفیت داده محدود به دیتاست اصلی است.



\## منبع داده

Breast Cancer Wisconsin Dataset — موجود در scikit-learn

مرجع: https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load\_breast\_cancer.html

