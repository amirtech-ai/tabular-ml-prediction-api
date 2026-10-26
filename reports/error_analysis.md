# Error Analysis

## Model
Logistic Regression

## Dataset
Breast Cancer Wisconsin

## Evaluation Setup
- **Train/test split:** 80% / 20%
- **Random state:** 42
- **Number of test samples:** 114

## Observed Performance
- **Accuracy:** 0.9825 (98.25%)
- **Precision:** 0.9820
- **Recall:** 0.9891
- **F1-score:** 0.9855

## Misclassified Samples
- **Number of errors:** 2 (out of 114 samples)
- **Observed patterns:**
  - 1 False Positive (actual = malignant, predicted = benign)
  - 1 False Negative (actual = benign, predicted = malignant)
  - The model performs equally well on both classes (balanced error distribution).
- **Potential explanations:**
  - The misclassified samples may have feature values that are borderline or overlap between the two classes (e.g., tumor size and concavity features that are not clearly separable).
  - Logistic Regression assumes a linear decision boundary; a few samples may lie near this boundary and be misclassified.
  - The dataset is very clean and the classes are largely separable, so only 2 errors are expected.

## Limitations
- **What cannot be concluded from the observed errors?**
  - We cannot conclude that the model will always perform this well on new, unseen data.
  - We cannot identify the exact feature(s) responsible for each misclassification without deeper analysis (e.g., feature importance, SHAP values).
  - Two errors are too few to draw statistically meaningful conclusions about systematic patterns.
- **What further analysis is needed?**
  - Cross-validation to obtain a more robust estimate of model performance.
  - Analysis of feature distributions for misclassified samples compared to correctly classified ones.
  - Comparison with other models (e.g., Random Forest, SVM) to see if the errors are model-specific or data-specific.

## Next Steps
1. Perform 5-fold Cross-validation to evaluate model stability.
2. Compare with other classification models (Random Forest, SVM, Gradient Boosting).
3. Investigate the misclassified samples in more detail (e.g., feature values, nearest neighbors) to understand potential causes.