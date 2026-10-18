\# Initial Data Analysis



\## 1. Dataset Overview

\- \*\*Dataset name:\*\* Breast Cancer Wisconsin (from scikit-learn)

\- \*\*Number of rows:\*\* 569

\- \*\*Number of columns:\*\* 31 (30 features + 1 target)

\- \*\*Feature columns:\*\* 30 numeric features (e.g., mean radius, mean texture, ...)

\- \*\*Target column:\*\* target (0 = malignant, 1 = benign)



\## 2. Data Types

\- \*\*Numeric columns:\*\* 31 (30 float64 + 1 int64)

\- \*\*Non-numeric columns:\*\* 0

\- \*\*Unexpected data types:\*\* None



\## 3. Data Quality

\- \*\*Missing values:\*\* 0 (No missing values in any column)

\- \*\*Duplicate rows:\*\* 0 (No duplicate rows found)

\- \*\*Potential data quality issues:\*\* None. The dataset is clean, but the target distribution is imbalanced.



\## 4. Target Distribution

\- \*\*Class counts:\*\* 

&#x20; - Class 0 (malignant): 212

&#x20; - Class 1 (benign): 357

\- \*\*Class proportions:\*\* 

&#x20; - Class 0: 37.26%

&#x20; - Class 1: 62.74%

\- \*\*Is the target distribution imbalanced?\*\* Yes, moderately imbalanced (approximately 63% vs 37%).



\## 5. Initial Observations

1\. Malignant tumors tend to have significantly larger `mean radius` and `mean area` compared to benign tumors.

2\. Features related to concavity (e.g., `worst concave points`) show higher values in malignant cases, indicating more irregular tumor shapes.

3\. The dataset is very clean (no missing values or duplicates), but the class imbalance means we should not rely solely on accuracy (the baseline of predicting the majority class is 62.74%).



\## 6. Limitations

\- \*\*What can we not conclude from this analysis?\*\* 

&#x20; - We cannot conclude causality or definitive predictive power of any single feature just from mean differences.

&#x20; - We cannot confirm if the model will generalize well until we perform a proper train/test split and train a model.

\- \*\*What needs further investigation?\*\*

&#x20; - Feature scaling (since features have different ranges).

&#x20; - Handling class imbalance (e.g., using stratified splits or class weights).

&#x20; - Checking for multicollinearity between features.

