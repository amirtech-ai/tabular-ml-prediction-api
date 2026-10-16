\# PROJECT SPEC — Tabular ML Prediction API



\## عنوان پروژه

Tabular ML Prediction API



\## هدف

آموزش یک مدل Classification روی داده‌های ساختاریافته و ارائه‌ی پیش‌بینی از طریق یک API.



\## نوع مسئله

Classification (دسته‌بندی دوتایی)



\## منبع داده

Breast Cancer Wisconsin Dataset — موجود در scikit-learn

مرجع: https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load\_breast\_cancer.html



\## ویژگی‌های ورودی

۳۰ ویژگی عددی استخراج‌شده از تصاویر نمونه‌های توده‌ی پستان

(مثل radius, texture, perimeter, area, smoothness, ...)



\## متغیر هدف (Target)

برچسب دو کلاسه:

\- 0 = malignant (بدخیم)

\- 1 = benign (خوش‌خیم)



\## خروجی مورد انتظار

پیش‌بینی کلاس (0 یا 1) برای ورودی معتبر.



\## معیارهای ارزیابی اولیه

\- Accuracy

\- Precision

\- Recall

\- F1-Score



انتخاب معیار نهایی بر اساس هزینه‌ی خطا و ساختار مسئله.



\## محدودیت‌ها

\- این پروژه صرفاً آموزشی است.

\- مدل ساخته‌شده ابزار تشخیص پزشکی محسوب نمی‌شود.

\- نباید برای تصمیم‌گیری بالینی واقعی استفاده شود.

\- محدودیت در تعمیم‌پذیری مدل به جمعیت‌های دیگر.

\- کیفیت داده محدود به دیتاست اصلی است.

