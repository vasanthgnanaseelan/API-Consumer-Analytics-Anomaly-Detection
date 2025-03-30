# Streamlit App in Notebook Format 

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Page Configuration
st.set_page_config(page_title="API Anomaly Dashboard", layout="wide")
st.title("API Consumer Analytics & Anomaly Detection")

# Load Data with Caching
@st.cache_data
def load_data():
    df = pd.read_csv("data/api_logs_engineered.csv", parse_dates=['timestamp'])

    return df

df = load_data()


# Sidebar Filters
endpoints = df['api_endpoint'].unique().tolist()
consumers = df['consumer_id'].unique().tolist()

selected_endpoints = st.sidebar.multiselect("Select Endpoints", endpoints, default=endpoints)
selected_consumers = st.sidebar.multiselect("Select Consumers", consumers, default=consumers)
date_range = st.sidebar.date_input("Date Range", [df['timestamp'].min(), df['timestamp'].max()])

# Apply Filters
filtered_df = df[
    (df['api_endpoint'].isin(selected_endpoints)) &
    (df['consumer_id'].isin(selected_consumers)) &
    (df['timestamp'].dt.date >= date_range[0]) &
    (df['timestamp'].dt.date <= date_range[1])
]


# API Usage Over Time
st.subheader("API Traffic Over Time")
time_series = filtered_df.set_index('timestamp').resample('D').size()
fig1, ax1 = plt.subplots(figsize=(12, 4))
time_series.plot(ax=ax1)
ax1.set_ylabel("Requests")
st.pyplot(fig1)

# KPIs
col1, col2, col3 = st.columns(3)
total_requests = len(filtered_df)
total_users = filtered_df['consumer_id'].nunique()
unique_endpoints = filtered_df['api_endpoint'].nunique()

col1.metric("Total Requests", f"{total_requests:,}")
col2.metric("Unique Consumers", f"{total_users:,}")
col3.metric("Endpoints Accessed", f"{unique_endpoints}")

# Hourly Traffic Distribution
st.subheader("API Request Volume by Hour of Day")
filtered_df['hour'] = filtered_df['timestamp'].dt.hour
hourly_counts = filtered_df.groupby('hour').size()
fig3, ax3 = plt.subplots(figsize=(10, 4))
sns.lineplot(x=hourly_counts.index, y=hourly_counts.values, marker="o", ax=ax3)
ax3.set_xlabel("Hour of Day")
ax3.set_ylabel("Request Count")
st.pyplot(fig3)

# Top Consumers by Request Volume
st.subheader("Top Consumers by Total Requests")
top_consumers = (
    filtered_df.groupby('consumer_id')
    .size()
    .sort_values(ascending=False)
    .head(10)
    .reset_index(name='Request Count')
)
st.dataframe(top_consumers)

# Average Response Time by Endpoint
st.subheader("Average Response Time per Endpoint")
response_time_stats = (
    filtered_df.groupby('api_endpoint')['response_time_ms']
    .mean()
    .sort_values(ascending=False)
    .head(10)
)
fig4, ax4 = plt.subplots(figsize=(10, 4))
sns.barplot(x=response_time_stats.values, y=response_time_stats.index, ax=ax4)
ax4.set_xlabel("Avg Response Time (ms)")
st.pyplot(fig4)

# Footer
st.caption("Developed for CST2213 BI Programming Final Project using Streamlit")

