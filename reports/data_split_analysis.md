\# Data Split Analysis



\## Dataset

\- \*\*Dataset name:\*\* Breast Cancer Wisconsin (from scikit-learn)

\- \*\*Total samples:\*\* 569

\- \*\*Number of features:\*\* 30



\## Split Configuration

\- \*\*Test size:\*\* 0.20 (20%)

\- \*\*Random state:\*\* 42

\- \*\*Stratification:\*\* Yes (stratify=y)



\## Results

\- \*\*Training samples:\*\* 455

\- \*\*Test samples:\*\* 114

\- \*\*Training class distribution:\*\*

&#x20; - Class 0 (malignant): 37.25%

&#x20; - Class 1 (benign): 62.75%

\- \*\*Test class distribution:\*\*

&#x20; - Class 0 (malignant): 37.72%

&#x20; - Class 1 (benign): 62.28%



\## Validation

\- \*\*Are feature and target row counts consistent?\*\* 

&#x20; - Yes. X\_train and y\_train both have 455 rows. X\_test and y\_test both have 114 rows.

\- \*\*Are class proportions reasonably preserved?\*\*

&#x20; - Yes. The class proportions in both sets are nearly identical (approximately 37% vs 63%), thanks to stratification.

\- \*\*Is the split reproducible?\*\*

&#x20; - Yes. Running the same code with `random\_state=42` produces identical splits every time. Changing `random\_state` produces a different split.



\## Limitations

\- \*\*Why is the test set kept separate?\*\*

&#x20; - The test set is kept separate to provide an unbiased evaluation of the model on unseen data. If we used the training data for evaluation, the model might overfit and show overly optimistic results.

\- \*\*What risks could affect the evaluation?\*\*

&#x20; - If the test set is too small, evaluation metrics may have high variance.

&#x20; - If the test set is used for model selection or hyperparameter tuning, data leakage occurs and the evaluation becomes unreliable.

&#x20; - If the dataset has hidden biases or is not representative of the real-world population, the evaluation may not generalize well.

