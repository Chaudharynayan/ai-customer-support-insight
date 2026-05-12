import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sqlite3

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="AI Customer Support Insight Platform",
    page_icon="📊",
    layout="wide"
)

# -----------------------------
# CUSTOM CSS
# -----------------------------
st.markdown(
    """
    <style>
    .main {
        background-color: #0f172a;
    }

    .stApp {
        background-color: #0f172a;
        color: white;
    }

    h1, h2, h3, h4 {
        color: white;
    }

    .metric-card {
        background: linear-gradient(135deg, #1e293b, #334155);
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.3);
        text-align: center;
        color: white;
    }

    .insight-box {
        background-color: #1e293b;
        padding: 15px;
        border-radius: 10px;
        margin-bottom: 10px;
    }

    .stTextArea textarea {
        background-color: #1e293b;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# -----------------------------
# LOAD DATA
# -----------------------------
df = pd.read_csv("data/processed_tickets.csv")

# -----------------------------
# DATA CLEANING
# -----------------------------
df = df.dropna()
df = df.drop_duplicates()

# -----------------------------
# DATABASE STORAGE
# -----------------------------
conn = sqlite3.connect("support_tickets.db")

df.to_sql(
    "tickets",
    conn,
    if_exists="replace",
    index=False
)

# -----------------------------
# HEADER
# -----------------------------
st.title("📊 AI-Powered Customer Support Insight Platform")

st.markdown(
    "Analyze customer complaints, sentiment, revenue impact, and recurring issues using AI-driven insights."
)

# -----------------------------
# SIDEBAR FILTERS
# -----------------------------
st.sidebar.header("Filters")

selected_sentiment = st.sidebar.multiselect(
    "Select Sentiment",
    options=df["sentiment"].unique(),
    default=df["sentiment"].unique()
)

selected_category = st.sidebar.multiselect(
    "Select Category",
    options=df["category"].unique(),
    default=df["category"].unique()
)

# -----------------------------
# NEW TICKET SECTION
# -----------------------------
st.sidebar.markdown("---")

st.sidebar.subheader("🆕 Add New Ticket")

new_message = st.sidebar.text_area(
    "Customer Complaint"
)

new_order_value = st.sidebar.number_input(
    "Order Value",
    min_value=0
)

if st.sidebar.button("Process Ticket"):

    if new_message != "":

        # simple demo processing
        new_sentiment = "NEGATIVE"

        new_category = "Technical Issue"

        new_risk = (
            "High"
            if new_order_value > 20000
            else "Low"
        )

        new_ticket = pd.DataFrame({
            "message": [new_message],
            "sentiment": [new_sentiment],
            "category": [new_category],
            "order_value": [new_order_value],
            "business_risk": [new_risk]
        })

        df = pd.concat(
            [df, new_ticket],
            ignore_index=True
        )

        st.sidebar.success(
            "Ticket processed successfully"
        )

# -----------------------------
# FILTERED DATA
# -----------------------------
filtered_df = df[
    (df["sentiment"].isin(selected_sentiment)) &
    (df["category"].isin(selected_category))
]

# -----------------------------
# KPI SECTION
# -----------------------------
total_tickets = len(filtered_df)

negative_tickets = len(
    filtered_df[
        filtered_df["sentiment"] == "NEGATIVE"
    ]
)

high_risk_cases = len(
    filtered_df[
        filtered_df["business_risk"] == "High"
    ]
)

average_order_value = round(
    filtered_df["order_value"].mean(),
    2
)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(
        f"""
        <div class="metric-card">
            <h3>Total Tickets</h3>
            <h1>{total_tickets}</h1>
        </div>
        """,
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        f"""
        <div class="metric-card">
            <h3>Negative Tickets</h3>
            <h1>{negative_tickets}</h1>
        </div>
        """,
        unsafe_allow_html=True
    )

with col3:
    st.markdown(
        f"""
        <div class="metric-card">
            <h3>High Risk Cases</h3>
            <h1>{high_risk_cases}</h1>
        </div>
        """,
        unsafe_allow_html=True
    )

with col4:
    st.markdown(
        f"""
        <div class="metric-card">
            <h3>Avg Order Value</h3>
            <h1>₹{average_order_value}</h1>
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown("---")

# -----------------------------
# CHARTS SECTION
# -----------------------------
col_left, col_right = st.columns(2)

# -----------------------------
# CATEGORY CHART
# -----------------------------
with col_left:

    st.subheader("📌 Complaint Categories")

    category_counts = (
        filtered_df["category"]
        .value_counts()
    )

    fig1, ax1 = plt.subplots(figsize=(8, 5))

    sns.barplot(
        x=category_counts.values,
        y=category_counts.index,
        ax=ax1
    )

    ax1.set_xlabel("Number of Tickets")
    ax1.set_ylabel("Category")

    st.pyplot(fig1)

# -----------------------------
# SENTIMENT CHART
# -----------------------------
with col_right:

    st.subheader("😊 Sentiment Distribution")

    sentiment_counts = (
        filtered_df["sentiment"]
        .value_counts()
    )

    fig2, ax2 = plt.subplots(figsize=(6, 5))

    ax2.pie(
        sentiment_counts.values,
        labels=sentiment_counts.index,
        autopct='%1.1f%%'
    )

    st.pyplot(fig2)

# -----------------------------
# REVENUE IMPACT
# -----------------------------
st.subheader("💰 Revenue Impact by Category")

revenue_impact = filtered_df.groupby(
    "category"
)["order_value"].sum().sort_values(
    ascending=False
)

fig3, ax3 = plt.subplots(figsize=(10, 5))

sns.lineplot(
    x=revenue_impact.index,
    y=revenue_impact.values,
    marker="o",
    ax=ax3
)

plt.xticks(rotation=45)

ax3.set_ylabel("Revenue Impact")
ax3.set_xlabel("Category")

st.pyplot(fig3)

# -----------------------------
# BUSINESS INSIGHTS
# -----------------------------
st.subheader("📈 Executive Insights")

most_common_issue = (
    filtered_df["category"]
    .value_counts()
    .idxmax()
)

most_revenue_issue = (
    revenue_impact.idxmax()
)

negative_percent = round(
    (
        negative_tickets / total_tickets
    ) * 100,
    2
)

st.markdown(
    f"""
    <div class="insight-box">
    🔹 Most recurring issue:
    <b>{most_common_issue}</b>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    f"""
    <div class="insight-box">
    🔹 Highest revenue impact category:
    <b>{most_revenue_issue}</b>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    f"""
    <div class="insight-box">
    🔹 Negative sentiment tickets:
    <b>{negative_percent}%</b>
    </div>
    """,
    unsafe_allow_html=True
)

# -----------------------------
# RAW DATA TABLE
# -----------------------------
st.subheader("🗂 Processed Ticket Data")

st.dataframe(filtered_df)

# -----------------------------
# DOWNLOAD BUTTON
# -----------------------------
csv = filtered_df.to_csv(index=False)

st.download_button(
    label="⬇ Download Processed Data",
    data=csv,
    file_name="processed_tickets.csv",
    mime="text/csv"
)