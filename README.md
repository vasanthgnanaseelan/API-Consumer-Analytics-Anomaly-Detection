API Consumer Analytics & Anomaly Detection Dashboard

This Streamlit dashboard provides insights into API usage behavior, system performance, and consumer activity using synthetic log data. Built for CST2213 BI Programming Final Project, the app highlights traffic patterns, top endpoints, and performance bottlenecks.

---

Features

- KPI Cards: Total Requests, Unique Consumers, Endpoints Accessed
- Traffic Analytics: Requests over time and hourly patterns
- Usage Breakdown: Top endpoints and top consumers
- Performance Insights: Average response times by endpoint
- Interactive Filtering: Filter by endpoint, consumer ID, and date range

---

Technologies Used

- Python 3.11+
- Streamlit for interactive dashboard
- Pandas for data manipulation
- Matplotlib & Seaborn for visualizations
- Scikit-learn for ML pipeline (Phase 5)
- Jupyter Notebooks for development & documentation

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

How to Run

```bash
pip install -r requirements.txt
streamlit run streamlit_app.py
```

Make sure the CSV is available at `data/api_logs_engineered.csv`

---

Insights Delivered

- Discover peak usage hours and most accessed endpoints
- Identify high-traffic consumers and performance-intensive endpoints
- Support business decisions around scaling, optimization, and alerting

---

Author

Developed by Vasanth Gnana Seelan for the final submission of CST2213 - Business Intelligence Programming Project (Phase 6).

---

For academic demonstration purposes only.
