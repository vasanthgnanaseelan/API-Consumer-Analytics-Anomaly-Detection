API Analytics Dashboard for Financial Services

APIs are the nervous system of digital finance — but most teams don’t get the visibility they need. This project flips that. It’s a fully on-premise, Python-based system that ingests API log data, applies machine learning for anomaly detection, and visualizes real-time insights through a clean, responsive Streamlit dashboard.

---

What it does

- Tracks API usage over time with dynamic filters
- Highlights top consumers and top endpoints
- Measures system performance (latency, resource use)
- Flags anomalies using Isolation Forest

---

Stack

- Python 3.11+
- Streamlit for UI
- Pandas, Seaborn, Matplotlib for data & viz
- Scikit-learn for ML
- Jupyter Notebooks for dev workflow

---

Run it locally

```bash
pip install -r requirements.txt
streamlit run streamlit_app.py
```

Make sure `data/api_logs_engineered.csv` exists — or generate one via the notebooks.

---

Folder Structure

```
API-Consumer-Analytics-Anomaly-Detection/
├── data/
│   └── api_logs_engineered.csv
├── models/
│   └── isolation_forest_model.pkl
├── notebooks/
│   └── streamlit_app.ipynb
├── streamlit_app.py
├── requirements.txt
├── README.md
```

---

Why this matters

APIs are essential, but their performance and behavior are often hard to monitor without expensive tooling. This project is lightweight, transparent, and extensible — built for teams who want to understand their systems better without vendor lock-in.

---

Built by

Vasanth Gnana Seelan — fueled by Python, clean dashboards, and the occasional espresso.
