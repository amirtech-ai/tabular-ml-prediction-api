# 🚀 Tabular ML Prediction API

> An end-to-end, production-ready machine learning pipeline for binary classification on tabular data.

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![scikit-learn](https://img.shields.io/badge/scikit--learn-1.0%2B-orange)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 📖 Overview

This repository contains an educational, yet professionally structured, machine learning project. It demonstrates a complete workflow from raw data analysis to model evaluation and error analysis, using the **Breast Cancer Wisconsin** dataset.

The goal is not only to build a predictive model but to showcase best practices in **data preprocessing**, **model evaluation**, and **reproducibility**.

---

## 🎯 Problem Definition

- **Task:** Binary Classification
- **Input:** 30 numerical features (e.g., mean radius, mean texture, etc.)
- **Target:** 0 (Malignant) or 1 (Benign)

---

## 📂 Repository Structure

We have organized the project to separate learning from production-ready code. Here is the current structure:

```text
/tabular-ml-prediction-api
│
├── README.md               # You are here
├── PROJECT_SPEC.md         # Detailed problem definition & limitations
├── DEVLOG.md               # Development log with errors & fixes
├── DEVLOG.html             # HTML version of the error log
├── requirements.txt        # Project dependencies
├── .gitignore              # Git ignore rules
├── LICENSE                 # MIT License
│
├── /data                   # Dataset folder
│   └── .gitkeep
│
├── /notebooks              # Learning and experimentation
│   ├── initial_data_analysis_1.ipynb  # 📓 Learning Notebook (Step-by-step with errors)
│   └── initial_data_analysis_2.ipynb  # 🚀 Clean & Structured Notebook
│
├── /reports                # Evaluation reports and notes
│   ├── initial_data_analysis_1.md
│   ├── data_split_analysis.md
│   ├── first_model_evaluation.md
│   ├── error_analysis.md
│   └── learning_notes.md
│
├── /src                    # (Future) Python scripts for the API
│   └── .gitkeep
│
└── /tests                  # (Future) Unit tests
    └── .gitkeep
```
### 🔍 Notebook Guide:
- **`initial_data_analysis_1.ipynb`**: This is our **learning lab**. It contains exploratory steps, trial & error, and detailed Persian explanations. It shows *how* we arrived at the solution.
- **`initial_data_analysis_2.ipynb`**: This is the **clean, production-ready version**. It contains only the essential code with English markdown documentation. **This is the file you should review for a quick understanding of the project.**

---

## ⚙️ Current Implementation

- [x] **Initial Data Analysis:** Checked shape, dtypes, missing values, and target distribution.
- [x] **Train/Test Split:** 80/20 split with `stratify=y` and `random_state=42`.
- [x] **Baseline Classifier:** `DummyClassifier` (most frequent) to set a performance floor.
- [x] **Logistic Regression Pipeline:** `StandardScaler` + `LogisticRegression` (preventing data leakage).
- [x] **Classification Metrics:** Accuracy, Precision, Recall, F1-Score, and Confusion Matrix.
- [x] **Error Analysis:** Inspected misclassified samples.
- [x] **Cross-Validation:** 5-Fold `StratifiedKFold` to ensure stability.

---

## 📊 Evaluation Results

| Metric | Baseline | Logistic Regression |
| :--- | :--- | :--- |
| **Accuracy** | 0.63 | **0.98** |
| **Precision** | 0.63 | **0.99** |
| **Recall** | 1.00 | **0.99** |
| **F1-Score** | 0.77 | **0.99** |

*For detailed reports, please see the `reports/` directory.*

---

## ⚠️ Limitations

- **Educational Purpose Only:** This project is not intended for medical diagnosis or clinical use.
- **Dataset:** The model was trained and evaluated on a public, clean dataset. Real-world data may require more robust preprocessing.

---

## 🚧 Current Status

| Feature | Status |
| :--- | :--- |
| Data Analysis | ✅ Complete |
| Train/Test Split | ✅ Complete |
| Baseline & Model | ✅ Complete |
| Evaluation & Metrics | ✅ Complete |
| Error Analysis | ✅ Complete |
| Cross-Validation | ✅ Complete |
| **API Implementation** | 🔄 Not Started |
| **Automated Tests** | 🔄 Not Started |
| **Model Deployment** | 🔄 Not Started |

---

## 🚀 Next Steps

1.  **API Development:** Build a FastAPI/Flask endpoint to serve predictions.
2.  **Automated Testing:** Write unit tests for preprocessing and model inference.
3.  **Model Deployment:** Containerize the API with Docker and deploy.

---

## 👨‍💻 Author

**Amir AI(SI)** – Applied AI Engineer Roadmap

- GitHub: [@amirtech-ai](https://github.com/amirtech-ai)
- LinkedIn: [Amir Mohammad Fallah](https://www.linkedin.com/in/amir-mohammad-fallah-11831342b/)