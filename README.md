# Voice Analysis & Parkinson’s Disease Detection

A concise end‑to‑end pipeline that trains and evaluates machine‑learning models on open voice‑recording datasets to predict whether a subject has Parkinson’s disease.

> This project was completed for *CAP 3784 - Introduction to Data Analytics* at the University of North Florida. It is **not** intended for clinical use.

---

## Project highlights

| Step | What happens |
|------|--------------|
| **Data ingest** | Kaggle voice‑measurement CSVs are downloaded to `data/raw/` (or dropped in manually). |
| **Pre‑processing** | Outliers removed (z‑score > 3) and features scaled with *MinMaxScaler* inside a scikit‑learn `Pipeline`. |
| **Model** | Random‑Forest classifier (baseline logistic & SVM included for comparison). 5‑fold cross‑validation with fixed random seed for reproducibility. |
| **Results** | Confusion matrix, ROC‑AUC, F1‑score and feature‑importance plots saved to `/artifacts`. |
| **App** | `streamlit_app.py` → get PD probability and see validation stats. |

---

## Quick start

```bash
# 1. clone
$ git clone https://github.com/AndreasInk/Data-Analytics-Group-Project.git
$ cd Data-Analytics-Group-Project

# 2. create env (conda or venv)
$ python -m venv .venv && source .venv/bin/activate
$ pip install -r requirements.txt

# 3. train & evaluate
$ python src/train.py            # writes model.joblib

# 4. (optional) launch demo
$ streamlit run src/app.py
```

Tested on **Python 3.11**.

---

## Repo layout

```
├── data/               # raw & processed datasets (git‑ignored)
├── src/                # training / inference code
│   ├── dataset.py
│   ├── train.py
    |── outliers.py
│   └── app.py
├── notebooks/          # EDA & experiment notebooks
├── artifacts/          # plots & saved model
├── reports/            # final PDF report
└── README.md
```

---

## Datasets

* **Parkinson’s Disease Data Set** – Vikas Ukani, Kaggle.
* **Parkinson’s Disease Voice Measurements** – Dutta et al., Kaggle.

See Kaggle pages for details.

---

## Results (baseline)

| Metric | Random Forest |
|--------|---------------|
| Accuracy | ~89% |
| F1‑score | ~0.89 |

Full figures are in `/artifacts` and the [final report](reports/Data Analytics Team 5 Final Report.pdf).

---

## Contributing / reuse

Feel free to fork. Open a PR with a short description of the change and we’ll take a look.

---

## License

This repository is released under the **MIT License**. See `LICENSE` for details.

> **Medical disclaimer:** This code and the accompanying report are for academic demonstration only and should **not** be used for medical diagnosis or decision‑making.

---

## Authors
Kayla Ciego - Andreas Ink - Steven Taylor - Muskan Patel - Zain Malik
