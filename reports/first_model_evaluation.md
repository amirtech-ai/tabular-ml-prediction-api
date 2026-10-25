# First Model Evaluation

## Problem
Binary classification on a tabular dataset

## Dataset
- **Dataset:** Breast Cancer Wisconsin (from scikit-learn)
- **Number of samples:** 569
- **Number of features:** 30
- **Target:** 0 = malignant, 1 = benign

## Experimental Setup
- **Train/test split:** 80% / 20%
- **Random state:** 42
- **Stratification:** Yes (stratify=y)
- **Preprocessing:** StandardScaler (fitted on X_train, applied to X_test)
- **Baseline:** DummyClassifier (strategy="most_frequent")

## Model
- **Algorithm:** Logistic Regression
- **Pipeline steps:** StandardScaler → LogisticRegression (max_iter=2000)

## Results
- **Baseline Accuracy:** 0.6228 (62.28%)
- **Model Accuracy:** 0.9825 (98.25%)
- **Precision:** 0.9820
- **Recall:** 0.9891
- **F1-score:** 0.9855

## Confusion Matrix
- **Matrix:** 
[[37 1]
[ 1 75]]


- **Interpretation:**
- True Negatives (TN): 37 (malignant correctly predicted as malignant)
- False Positives (FP): 1 (benign incorrectly predicted as malignant)
- False Negatives (FN): 1 (malignant incorrectly predicted as benign)
- True Positives (TP): 75 (benign correctly predicted as benign)

## Error Analysis
- **Main observed errors:** 2 errors out of 114 samples (1 FP and 1 FN). The model performs equally well on both classes.
- **Potential causes:** The dataset is very clean and the classes are linearly separable to a large extent. Logistic Regression is well-suited for this problem.

## Limitations
- **Evaluation limitations:** A single train/test split may not be representative. Cross-validation is needed for more robust evaluation.
- **Potential data leakage risks:** None observed. The test set was not used in fitting the scaler or the model.
- **What remains to be tested:** Cross-validation, comparison with other models (Random Forest, SVM), and analysis of misclassified samples.

## Next Steps
1. Perform Cross-validation for more robust evaluation.
2. Compare with other models (e.g., Random Forest, SVM).
3. Analyze misclassified samples to understand potential patterns.