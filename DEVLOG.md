# DEVLOG

## تاریخ: 1405/07/25 (روز سوم - چهارشنبه)

### ۱. امروز چه کاری انجام دادم؟
- تحلیل اولیه دیتاست Breast Cancer Wisconsin را کامل کردم.
- ساختار داده، نوع داده‌ها، مقادیر گمشده و توزیع کلاس‌ها را بررسی کردم.
- فایل `PROJECT_SPEC.md` را تکمیل کردم (تعریف مسئله، ورودی، خروجی، محدودیت‌ها).
- متغیرهای `X` (ویژگی‌ها) و `y` (هدف) را از هم جدا کردم و ابعاد آن‌ها را بررسی کردم.
- دستورات پایه‌ی `pandas` (مثل `head()`، `shape`، `dtypes`، `info()`، `describe()`، `isna()`، `unique()`، `value_counts()`) را یاد گرفتم و روی داده پیاده کردم.
- ساختار پوشه‌های پروژه را با استانداردهای پیشنهادی هماهنگ کردم.

### ۲. چه خطاهایی داشتم و چطور حلشان کردم؟
1. **خطای `TypeError: DataFrame.__init__() got an unexpected keyword argument 'target_name'`**
   - **علت:** در ساخت `DataFrame` از پارامتر `target_name='alpo'` استفاده کرده بودم که اصلاً در تابع `pd.DataFrame` وجود ندارد.
   - **راه‌حل:** پارامتر اضافی را حذف کردم و کد صحیح را نوشتم.

2. **خطای `UFuncTypeError: ufunc 'add' did not contain a loop with signature matching types`**
   - **علت:** در تلاش برای چسباندن علامت `%` به درصدها، یک سری عددی (`float64`) را مستقیماً با یک متن (`"%"`) جمع کرده بودم.
   - **راه‌حل:** با استفاده از `astype(str)` اعداد را به متن تبدیل کردم، سپس علامت `%` را به آن‌ها چسباندم. (همچنین از `round(2)` برای کاهش اعشار استفاده کردم).

3. **مشکل منطقی در کد `if percentages == 1`**
   - **علت:** به جای مقایسه‌ی خود کلاس‌ها، سری متنی درصدها را با عدد `1` مقایسه کرده بودم و حلقه هم نداشت.
   - **راه‌حل:** با حلقه‌ی `for` روی `proportions.items()` و شرط `if target_class == 0/1` مشکل برطرف شد.

### ۳. چه سوالات مفهومی داشتم؟
- تفاوت `df.info()` و `df.describe()` چیست؟
- خروجی `np.int64(0)` در `df['mean radius'].isna().sum()` به چه معناست؟
- دستور `unique()` چه کاری انجام می‌دهد و چرا `sorted(y.unique())` استفاده می‌شود؟
- چگونه تعداد نمونه‌های هر کلاس را به دست آوریم و چرا بررسی نوع داده‌ها پیش از آموزش مدل ضروری است؟

### ۴. چه چیزی هنوز ناقص است؟
- هنوز مدل را آموزش نداده‌ام (طبق برنامه، این کار به روزهای بعد موکول شده است).
- تقسیم داده به `Train/Test` هنوز انجام نشده است.
- استفاده از `Pipeline` برای پیش‌پردازش (استانداردسازی) هنوز پیاده‌سازی نشده است.

### ۵. گام بعدی:
- اجرای تقسیم `Train/Test` با `train_test_split`.
- ساخت `Pipeline` برای استانداردسازی داده‌ها.
- ثبت گزارش `data_split_analysis.md`.




## تاریخ: 1405/07/26 (روز چهارم - پنجشنبه) - قسمت اول

### ۱. چه چیزی پیاده‌سازی شد؟
- داده به دو بخش آموزش (۸۰٪) و آزمون (۲۰٪) تقسیم شد.
- از `train_test_split` با پارامترهای `test_size=0.20`، `random_state=42` و `stratify=y` استفاده شد.
- یک `Pipeline` اولیه با `StandardScaler` ساخته شد.
- `X_train` با `fit_transform` استاندارد شد و `X_test` با `transform` استاندارد شد.

### ۲. چرا داده به آموزش و آزمون تقسیم شد؟
- برای ارزیابی واقعی عملکرد مدل روی داده‌های دیده‌نشده. اگر مدل را فقط روی داده آموزش ارزیابی کنیم، ممکن است داده‌ها را حفظ کند (`Overfitting`) و نتیجه واقعی نباشد.

### ۳. چرا از `stratify` استفاده شد؟
- برای حفظ نسبت کلاس‌ها در مجموعه‌های آموزش و آزمون. نسبت کلاس‌ها در داده اصلی ۳۷.۲۶٪ (کلاس ۰) و ۶۲.۷۴٪ (کلاس ۱) است. با `stratify=y`، این نسبت در هر دو مجموعه تقریباً حفظ می‌شود.

### ۴. چگونه از نشت اطلاعات (`Data Leakage`) در استانداردسازی جلوگیری شد؟
- `StandardScaler` فقط روی `X_train` با `fit_transform` برازش شد. یعنی میانگین و انحراف معیار فقط از داده آموزش محاسبه شد.
- روی `X_test` فقط `transform` اجرا شد. یعنی از همان پارامترهای یادگرفته‌شده از داده آموزش استفاده شد و هیچ پارامتر جدیدی از داده آزمون یاد گرفته نشد.

### ۵. چه مواردی هنوز باقی مانده‌اند؟
- آموزش مدل (Baseline و مدل اصلی) هنوز انجام نشده است.
- ارزیابی مدل با معیارهای مناسب (Accuracy، Precision، Recall، F1) هنوز انجام نشده است.
- ساخت `API` برای پیش‌بینی هنوز انجام نشده است.


## تاریخ: 1405/07/26 (روز چهارم - پنجشنبه) قسمت دوم

### ۱. چه چیزی پیاده‌سازی شد؟
- داده به دو بخش آموزش (۸۰٪) و آزمون (۲۰٪) تقسیم شد.
- از `train_test_split` با پارامترهای `test_size=0.20`، `random_state=42` و `stratify=y` استفاده شد.
- یک `Pipeline` اولیه با `StandardScaler` ساخته شد.
- `X_train` با `fit_transform` استاندارد شد و `X_test` با `transform` استاندارد شد.
- یک `Baseline` با `DummyClassifier` ساخته شد.
- یک مدل `Logistic Regression` با `Pipeline` آموزش داده شد.
- پیش‌بینی‌ها تولید و با `y_test` مقایسه شدند.
- معیارهای `Accuracy`، `Precision`، `Recall` و `F1-score` محاسبه شدند.
- `Confusion Matrix` بررسی و تحلیل شد.
- گزارش `first_model_evaluation.md` ساخته شد.

### ۲. چرا داده به آموزش و آزمون تقسیم شد؟
- برای ارزیابی واقعی عملکرد مدل روی داده‌های دیده‌نشده. اگر مدل را فقط روی داده آموزش ارزیابی کنیم، ممکن است داده‌ها را حفظ کند (`Overfitting`) و نتیجه واقعی نباشد.

### ۳. چرا از `stratify` استفاده شد؟
- برای حفظ نسبت کلاس‌ها در مجموعه‌های آموزش و آزمون. نسبت کلاس‌ها در داده اصلی ۳۷.۲۶٪ (کلاس ۰) و ۶۲.۷۴٪ (کلاس ۱) است. با `stratify=y`، این نسبت در هر دو مجموعه تقریباً حفظ می‌شود.

### ۴. چگونه از نشت اطلاعات (`Data Leakage`) در استانداردسازی جلوگیری شد؟
- `StandardScaler` فقط روی `X_train` با `fit_transform` برازش شد. یعنی میانگین و انحراف معیار فقط از داده آموزش محاسبه شد.
- روی `X_test` فقط `transform` اجرا شد. یعنی از همان پارامترهای یادگرفته‌شده از داده آموزش استفاده شد و هیچ پارامتر جدیدی از داده آزمون یاد گرفته نشد.

### ۵. خطاها و مشکلاتی که داشتم و چطور حلشان کردم؟
1. **بدفهمی درباره‌ی `random_state=42`**
   - **علت:** فکر می‌کردم `random_state=42` باعث بهتر شدن مدل می‌شود.
   - **راه‌حل:** با مطالعه و مثال، فهمیدم که `random_state` فقط برای بازتولیدپذیری است و هیچ تأثیری روی عملکرد مدل ندارد. عدد `42` هیچ ارزش جادویی ندارد و فقط یک قرارداد رایج است.

2. **بدفهمی درباره‌ی استفاده از مجموعه آزمون برای انتخاب مدل**
   - **علت:** نمی‌دانستم که این کار باعث `Data Leakage` می‌شود.
   - **راه‌حل:** با مثال دانش‌آموز و امتحان، مفهوم را بهتر درک کردم و یاد گرفتم که مجموعه آزمون فقط باید یک بار و در پایان کار برای ارزیابی نهایی استفاده شود.

3. **سوال درباره‌ی تأثیر بستن `VS Code` بر تقسیم داده**
   - **پاسخ:** با `random_state=42`، تقسیم داده همیشه یکسان است، حتی اگر کامپیوتر را خاموش و روشن کنید. این خاصیت بازتولیدپذیری است.

4. **خطای احتمالی `Data Leakage` در `StandardScaler`**
   - **علت:** ممکن بود `StandardScaler` را روی کل دیتاست (قبل از تقسیم) برازش کنم.
   - **راه‌حل:** از `fit_transform` فقط روی `X_train` و از `transform` فقط روی `X_test` استفاده کردم.

5. **سوال درباره‌ی تفاوت `fit`، `transform` و `fit_transform`**
   - **پاسخ:** `fit` پارامترها را یاد می‌گیرد. `transform` از پارامترها استفاده می‌کند. `fit_transform` هر دو را با هم انجام می‌دهد (فقط برای داده آموزش).

6. **سوال درباره‌ی نحوه استفاده از `Git` و `push` کردن**
   - **پاسخ:** با `git add .`، سپس `git commit -m "پیام"` و در نهایت `git push`. خروجی موفق نشان می‌دهد که همه چیز به درستی ارسال شده است.

### ۶. سوالات مفهومی که داشتم؟
- تفاوت `df.info()` و `df.describe()` چیست؟
- خروجی `np.int64(0)` در `df['mean radius'].isna().sum()` به چه معناست؟
- دستور `unique()` چه کاری انجام می‌دهد و چرا `sorted(y.unique())` استفاده می‌شود؟
- چگونه تعداد نمونه‌های هر کلاس را به دست آوریم و چرا بررسی نوع داده‌ها پیش از آموزش مدل ضروری است؟
- تفاوت `DataFrame` و `Series` چیست؟
- مفهوم `Training Set` و `Test Set` چیست و چرا به `Baseline` نیاز داریم؟
- تفاوت `Accuracy`، `Precision`، `Recall` و `F1-score` چیست و هر کدام چه کاربردی دارند؟
- `Confusion Matrix` چیست و چگونه تفسیر می‌شود؟
- چرا مجموعه آزمون نباید برای انتخاب مکرر مدل و تنظیم پارامترها استفاده شود؟
- چگونه از `Pipeline` برای جلوگیری از `Data Leakage` استفاده کنیم؟

### ۷. نتایج به‌دست‌آمده (خروجی‌های واقعی):
- **Baseline Accuracy:** ۰.۶۲۲۸ (۶۲.۲۸٪)
- **Model Accuracy:** ۰.۹۸۲۵ (۹۸.۲۵٪)
- **Precision:** ۰.۹۸۲۰
- **Recall:** ۰.۹۸۹۱
- **F1-score:** ۰.۹۸۵۵
- **Confusion Matrix:** 


[[37 1]
[ 1 75]]


- True Negatives (TN): ۳۷ (malignant درست پیش‌بینی شد)
- False Positives (FP): ۱ (benign به اشتباه malignant پیش‌بینی شد)
- False Negatives (FN): ۱ (malignant به اشتباه benign پیش‌بینی شد)
- True Positives (TP): ۷۵ (benign درست پیش‌بینی شد)

### ۸. چه مواردی هنوز باقی مانده‌اند؟
- انجام `Cross-validation` برای ارزیابی پایدارتر.
- مقایسه با مدل‌های دیگر (مثل `Random Forest`، `SVM`).
- تحلیل دقیق‌تر نمونه‌هایی که مدل اشتباه پیش‌بینی کرده است.
- ساخت `API` برای پیش‌بینی هنوز انجام نشده است.

### ۹. گام بعدی:
- اجرای `Cross-validation` برای ارزیابی پایدارتر.
- مقایسه با مدل‌های دیگر.
- تحلیل خطاهای مدل.


## تاریخ: 1405/07/25

## Initial Project Status
- **وضعیت اولیه پروژه:** پروژه در مرحله‌ی ساخت مدل اولیه و ارزیابی آن قرار دارد. تحلیل داده و تقسیم‌بندی انجام شده و اولین مدل آموزش دیده است.
- **آخرین اجرای موفق:** اجرای کامل نوتبوک `initial_data_analysis_1.ipynb` بدون خطا (شامل بارگذاری داده تا محاسبه معیارهای ارزیابی).
- **فایل اصلی آموزش:** `notebooks/initial_data_analysis_1.ipynb` (در حال حاضر آموزش و ارزیابی در همین یک فایل انجام می‌شود).
- **فایل اصلی ارزیابی:** `reports/first_model_evaluation.md` (گزارش مکتوب) و بخش ارزیابی در همان نوتبوک.

## Audit Findings
- **بخش‌های کامل:** بارگذاری داده، تحلیل اولیه (EDA)، جداسازی `X` و `y`، تقسیم داده (`train_test_split` با `stratify`)، ساخت `Baseline`، ساخت `Pipeline` (شامل `StandardScaler` و `LogisticRegression`)، تولید پیش‌بینی، محاسبه معیارها (Accuracy, Precision, Recall, F1, Confusion Matrix) و Cross-validation (`StratifiedKFold`).
- **بخش‌های ناقص:** 
  - انتقال کدها از نوتبوک به اسکریپت‌های پایتون (`.py`) در پوشه `/src`.
  - ساخت API (وب‌سرویس پیش‌بینی).
  - نوشتن تست‌های خودکار (`/tests`).
- **بخش‌های انجام نشده:** (هنوز شروع نشده) ساخت فایل `WEEK_02_TASKS.md` برای برنامه‌ریزی دقیق هفته دوم.

## Data Quality
- **تعداد نمونه‌ها:** ۵۶۹ نمونه (ردیف).
- **تعداد ویژگی‌ها:** ۳۰ ویژگی عددی (ستون) + ۱ ستون هدف (`target`).
- **مقادیر کم‌شده:** ۰ (هیچ مقدار گم‌شده‌ای وجود ندارد).
- **ردیف‌های تکراری:** ۰ (هیچ ردیف تکراری یافت نشد).
- **توزیع کلاس‌ها:** کلاس `1` (benign): ۳۵۷ نمونه (۶۲.۷۴٪) | کلاس `0` (malignant): ۲۱۲ نمونه (۳۷.۲۶٪) - داده‌ها کمی نامتعادل هستند.

## Training and Evaluation
- **وضعیت train/test split:** انجام شده. نسبت ۸۰٪ آموزش (۴۵۵ نمونه) و ۲۰٪ آزمون (۱۱۴ نمونه) با `random_state=42` و `stratify=y`.
- **وضعیت baseline:** انجام شده. `DummyClassifier` با `strategy="most_frequent"` و دقت (Accuracy) حدود ۶۲.۲۸٪.
- **وضعیت Logistic Regression:** انجام شده. مدل با دقت (Accuracy) حدود ۹۸.۲۵٪ و F1-score حدود ۰.۹۸۵۵.
- **وضعیت Pipeline:** انجام شده. شامل `StandardScaler` و `LogisticRegression(max_iter=2000)`. از نشت اطلاعات (Data Leakage) جلوگیری شده است (fit_transform فقط روی آموزش).
- **وضعیت Cross-validation:** انجام شده. با `StratifiedKFold` (n_splits=5) روی داده آموزش. میانگین F1-score برابر ۰.۹۸۲۴ و انحراف معیار ۰.۰ (مدل پایدار).

## Tests and Reproducibility
- **دستورات اجراشده:** اجرای مجدد نوتبوک با `Restart & Run All` (اجرای از ابتدا تا انتها).
- **تست‌های موفق:** خروجی‌ها دقیقاً با اجرای قبلی یکسان بودند (به دلیل `random_state=42`). هیچ خطایی در اجرای مجدد رخ نداد. ابعاد داده‌ها و معیارها با گزارش‌ها هماهنگ هستند.
- **تست‌های ناموفق:** هیچ تست ناموفقی در اجرای مجدد مشاهده نشد.
- **مشکلات شناسایی شده:** در حال حاضر مشکل فنی خاصی وجود ندارد. تنها چالش، مرتب‌سازی کدها برای انتقال به مرحله‌ی بعد (ساخت API) است.

## Market Research
- **مشتریان بالقوه:** (طبق انتخاب شما در هفته اول) کسب‌وکارهایی که نیاز به پردازش اسناد فارسی یا پیش‌بینی داده‌های جدولی دارند. (در حال حاضر این بخش هنوز به‌طور کامل در پروژه پیاده‌سازی نشده است).
- **فرضیه‌های مشکل:** فرض بر این است که کسب‌وکارها برای تحلیل داده‌های جدولی خود به ابزارهای سریع و قابل اعتماد نیاز دارند.
- **اقدام بعدی:** شناسایی دقیق ۳ مشتری بالقوه و انجام مصاحبه برای اعتبارسنجی مشکل (طبق برنامه‌ی هفته‌ی اول، این بخش هنوز ناقص است و باید در هفته‌های آینده تکمیل شود).


## تاریخ: 1405/07/26

## Goal
Refactor the training workflow and persist the trained pipeline.

## Code Changes
- **Modules created or updated:** 
  - Created `/src/__init__.py` (to make `src` a package).
  - Created `/src/train.py` (training and evaluation workflow).
  - Created `/src/predict.py` (model loading and prediction interface).
- **Training entry point:** `python -m src.train`
- **Prediction module:** `src/predict.py` with `load_model()` and `predict()` functions.
- **Data loading changes:** Data is now loaded directly inside `train.py` using `load_breast_cancer(as_frame=True)`, and a `.copy()` is used to prevent modifying the original dataset.

## Model Artifact
- **Artifact path:** `artifacts/model.joblib`
- **Full pipeline saved:** Yes (includes `StandardScaler` and `LogisticRegression`).
- **Loading tested:** Yes, successfully loaded using `joblib.load()`.

## Reproducibility
- **Training command:** `python -m src.train`
- **Execution successful:** Yes, the script runs without errors and outputs the evaluation metrics.
- **Dependency versions recorded:** Yes (updated `requirements.txt`).

## Tests
- **Training:** Successful. No errors during model fitting.
- **Artifact creation:** Successful. The file `artifacts/model.joblib` is created.
- **Artifact loading:** Successful. The model loads correctly.
- **Prediction consistency:** Successful. Predictions before saving and after loading are identical (`Are they identical? True`).
- **Invalid input handling:** Successful. The function raises a clear `ValueError` when the input does not have exactly 30 features.

## Market Research
- **Leads followed up:** (این بخش را بر اساس تحقیقات بازار خودتان پر کنید. مثلاً: ۳ مشتری بالقوه در حوزه پردازش اسناد شناسایی شد).
- **Customer workflow insights:** (مثلاً: مشتریان فعلاً از اکسل برای دسته‌بندی اسناد استفاده می‌کنند و زمان زیادی صرف می‌کنند).
- **Next action:** (مثلاً: تماس با مشتری اول برای انجام مصاحبه در روزهای آینده).



## API (In Progress)

The project includes a Django REST Framework API to serve the trained model. 

### Endpoints
- **`GET /api/v1/health/`**
  - **Description:** Checks if the service and the model are loaded and ready.
  - **Response:** `{"status": "ok", "message": "Service is running."}` (HTTP 200)

- **`POST /api/v1/predict/`**
  - **Description:** Validates input and returns a prediction.
  - **Request Format:** JSON object with exactly 30 numerical features (matching the dataset).
  - **Response Format:** `{"status": "success", "prediction": 1, "probabilities": {"malignant": 0.1, "benign": 0.9}}` (HTTP 200)
  - **Errors:**
    - `400 Bad Request`: Invalid JSON, missing fields, extra fields, non-numeric values, NaN/Infinity.
    - `500 Internal Server Error`: Model not loaded or internal prediction error.

### Prerequisites & Installation
Ensure you have the required packages installed:
```bash
pip install -r requirements.txt
Running the Service
To start the Django API server, run:

bash
python manage.py runserver
Running Tests
To run the API tests, use:

bash
python manage.py test prediction
Limitations
This API is for educational purposes only.

It is not intended for medical diagnosis or clinical use.

The model is trained on the Breast Cancer Wisconsin dataset and should not be used with other data without retraining.

text

---

### ۲. به‌روزرسانی فایل `DEVLOG.md`

این متن را به انتهای فایل `DEVLOG.md` خود اضافه کنید:

```markdown
## تاریخ: 1405/07/27 (روز پنجم - جمعه)

### ۱. چه فایل‌هایی تغییر کرده‌اند؟
- ساختار جدید `Django` (شامل `manage.py`، پوشه‌ی `api/` و اپلیکیشن `prediction/`).
- فایل‌های `prediction/constants.py`، `prediction/serializers.py`، `prediction/views.py` و `prediction/urls.py`.
- فایل `api/urls.py` و `api/settings.py`.
- فایل `requirements.txt` (اضافه شدن `django` و `djangorestframework`).

### ۲. چه چیزی واقعاً اجرا شده است؟
- سرور `Django` با دستور `python manage.py runserver` اجرا شده است.
- مسیر سلامت (`/api/v1/health/`) با موفقیت پاسخ داده است.
- `Endpoint` پیش‌بینی (`/api/v1/predict/`) پیاده‌سازی شده و مدل ذخیره‌شده در `artifacts/model.joblib` را بارگذاری می‌کند.
- اعتبارسنجی ورودی (با `Serializer`) پیاده‌سازی شده است.

### ۳. کدام تست‌ها پاس شده‌اند؟
- **(اگر تست‌ها را اجرا کرده‌اید، این بخش را با نتایج واقعی خود پر کنید. مثلاً:)** 
- `test_health_check_success`: پاس شد.
- `test_predict_valid_input`: پاس شد.
- `test_predict_empty_body`: پاس شد.
- `test_predict_missing_feature`: پاس شد.
- `test_predict_non_numeric_value`: پاس شد.
- *(اگر هنوز تست‌ها را اجرا نکرده‌اید، بنویسید: تست‌های خودکار هنوز اجرا نشده‌اند.)*

### ۴. چه خطاهایی باقی مانده‌اند؟
- **(اگر خطایی وجود ندارد، بنویسید:)** خطای فنی فعالی در `API` مشاهده نمی‌شود.
- **(اگر خطایی داشتید، مثلاً:)** در ابتدا خطای `Model not loaded` دریافت کردم که با اصلاح مسیر `MODEL_PATH` برطرف شد. 

### ۵. اولین اقدام روز بعد چیست؟
- تکمیل و اجرای کامل تست‌های `API`.
- تست `API` با ابزارهایی مثل `curl` یا `Postman` از خارج از سرور (تست واقعی).
- بررسی و بهبود مدیریت خطاها (مخصوصاً سناریوهای داخلی).
- به‌روزرسانی `README` و مستندات.
- **اقدام بازار:** تماس با ۳ مشتری بالقوه برای اعتبارسنجی مشکل (مطابق برنامه هفته اول).
