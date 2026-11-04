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
├── .gitignore              # Git ignore rules (ignores .venv, __pycache__, *.joblib)
├── README.md               # You are here (Project overview)
├── PROJECT_SPEC.md         # Detailed problem definition & limitations
├── DEVLOG.md               # Development log with errors & fixes
├── DEVLOG.html             # HTML version of the error log
├── requirements.txt        # Project dependencies
├── manage.py               # Django main entry point
├── LICENSE                 # MIT License
│
├── /api                    # Django project settings
│   ├── __init__.py
│   ├── settings.py         # Django settings
│   ├── urls.py             # Main URL routing
│   ├── asgi.py
│   └── wsgi.py
│
├── /prediction             # Django app for predictions
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── constants.py        # List of feature names (30 features)
│   ├── models.py
│   ├── serializers.py      # Input validation for API
│   ├── tests.py            # Automated API tests (21 tests)
│   ├── urls.py             # API endpoints (health, predict)
│   └── views.py            # Prediction logic and model loading
│
├── /src                    # Machine Learning scripts
│   ├── __init__.py
│   ├── evaluation.py       # Evaluation and error analysis (Cross-validation, etc.)
│   ├── predict.py          # Model loading and prediction functions
│   └── train.py            # Training and saving the model
│
├── /artifacts              # Saved model artifacts
│   ├── .gitkeep            # Keeps the folder empty in Git
│   └── model.joblib        # Main trained Pipeline (ignored by Git)
│
├── /notebooks              # Jupyter notebooks for EDA
│   ├── initial_data_analysis_1.ipynb  # 📓 Learning Notebook (Step-by-step with errors)
│   └── initial_data_analysis_2.ipynb  # 🚀 Clean & Structured Notebook
│
├── /reports                # Text reports and analysis
│   ├── data_split_analysis.md
│   ├── first_model_evaluation.md
│   ├── learning_notes.md
│   └── test_report.md
│
└── /tests                  # Automated tests (Django + Unit tests)
    └── .gitkeep
```
## 🛠️ Tech Stack

- **Language:** Python 3.14+
- **ML Libraries:** scikit-learn, pandas, numpy, joblib
- **API Framework:** Django, Django REST Framework
- **Testing:** Django TestCase, unittest.mock

---

⚙️ Installation & Setup
bash
# 1. Create a virtual environment
python -m venv .venv

# 2. Activate the environment
# Windows:
.venv\Scripts\Activate.ps1
# Linux/Mac:
source .venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Train the model (if not already done)
python -m src.train

# 5. Run the API server
python manage.py runserver

---

## 🔍 Notebook Guide:
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
| **Accuracy** | 0.6228 | **0.9825** |
| **Precision** | 0.6274 | **0.9820** |
| **Recall** | 1.0000 | **0.9891** |
| **F1-Score** | 0.7709 | **0.9855** |

*For detailed reports, please see the `reports/` directory.*

---

## 🌐 API Endpoints

GET **/api/v1/health/**: Checks service health.

POST **/api/v1/predict/**: Accepts JSON with 30 features and returns a prediction.

Example Request:

```json
{
  "mean radius": 10.0,
  "mean texture": 10.0,
  ...
}
```
Example Response:

```json
{
  "status": "success",
  "prediction": 1,
  "probabilities": {
    "malignant": 0.1,
    "benign": 0.9
  }
}
```

---

## 🧪 Running Tests

```bash
python manage.py test prediction
```

---

## ⚠️ Limitations

- **Educational Purpose Only:** This project is not intended for medical diagnosis or clinical use.
- **Dataset:** The model was trained and evaluated on a public, clean dataset. Real-world data may require more robust preprocessing.

---

## 📜 License
This project is licensed under the MIT License.

## 📄 فایل `requirements.txt` (نسخه نهایی)

```text
pandas>=1.5.0
numpy>=1.23.0
scikit-learn>=1.2.0
joblib>=1.2.0
django>=4.0
djangorestframework>=3.14
```

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
| **API Implementation** | ✅ Complete |
| **Automated Tests** | ✅ Complete |
| **Model Deployment** | ✅ Complete |

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

