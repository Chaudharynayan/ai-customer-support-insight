# 📊 AI-Powered Customer Support Insight Platform

## 📌 Overview

The AI-Powered Customer Support Insight Platform is an end-to-end system designed to analyze customer support tickets and extract actionable business insights using NLP and Machine Learning.

It processes raw complaint data, identifies sentiment, classifies issues, detects business risk, and generates automated responses to improve customer support efficiency and decision-making.

---

## ⚙️ How It Works (Step-by-Step)

### 1. Data Ingestion

* Loads customer support ticket dataset (`CSV`)
* Extracts fields such as message, order value, and metadata
* Cleans and preprocesses text using Pandas

---

### 2. Sentiment Analysis

* Uses **DistilBERT (`sst-2` fine-tuned model)**
* Classifies each complaint as:
  - POSITIVE
  - NEGATIVE
* Helps identify dissatisfied customers quickly

---

### 3. Ticket Categorization (Zero-Shot Learning)

* Uses **Facebook BART (`bart-large-mnli`)**
* Assigns category without labeled training data
* Categories include:
  - Refund Issue
  - Delivery Delay
  - Payment Problem
  - Technical Issue
  - Login Issue
  - Wrong Product
  - Customer Support Complaint

---

### 4. Embedding & Clustering

* Converts messages into embeddings using **MiniLM (`all-MiniLM-L6-v2`)**
* Applies **KMeans clustering**
* Groups similar complaints together for pattern discovery

---

### 5. Business Risk Detection

* Rules-based risk engine:
  - High order value + NEGATIVE sentiment → HIGH RISK
  - Otherwise → LOW RISK
* Helps prioritize critical business cases

---

### 6. Insight Generation

Generates key business insights such as:

* Most recurring complaint categories
* Revenue-impacting issues
* Sentiment distribution
* High-risk transactions

---

### 7. Dashboard Visualization

Built using **Streamlit**, the dashboard displays:

* KPI metrics (tickets, risk cases, sentiment)
* Category distribution charts
* Sentiment analysis visualization
* Revenue impact trends
* Filterable interactive insights

---

## 📊 Data Model

Each ticket is transformed into a structured format:

- **ticket_id** → Unique identifier  
- **timestamp** → Time of complaint  
- **customer_id** → Customer reference ID  
- **message** → Raw complaint text  
- **sentiment** → AI-generated sentiment label  
- **category** → AI-generated issue type  
- **order_value** → Transaction value  
- **business_risk** → High / Low risk classification  
- **cluster** → KMeans cluster group  
- **suggested_response** → Auto-generated support reply  

---

## 🧠 Key Features

* Sentiment analysis using Transformer models  
* Zero-shot ticket classification  
* Semantic clustering of complaints  
* Business risk detection engine  
* Revenue impact analysis  
* AI-generated support responses  
* Interactive Streamlit dashboard  

---

## ⚠️ Limitations

* Zero-shot classification may not always be domain-perfect  
* KMeans assumes spherical clusters (may miss complex patterns)  
* Rule-based risk system is simplistic  
* Requires better fine-tuning for production accuracy  

---

## 🚀 Future Improvements

* Fine-tuned domain-specific transformer model  
* Real-time ticket streaming pipeline (Kafka)  
* LLM-based intelligent support chatbot  
* Multi-language complaint support  
* Predictive customer churn modeling  
* Advanced anomaly detection for fraud cases  

---

## ▶️ How to Run

### 1. Install dependencies

```

pip install streamlit pandas matplotlib seaborn scikit-learn transformers sentence-transformers

```

---

### 2. Run Streamlit App

```

streamlit run app.py

```

---

### 3. Dataset

Ensure the dataset file exists:

```

data/processed_tickets.csv

```

---

## 📁 Project Structure

```

AI-Customer-Support-Insight/
│
├── app.py
├── notebook.ipynb
├── tickets.csv
├── processed_tickets.csv
├── support_tickets.db
├── requirements.txt
└── README.md

```

---

## 🎯 Conclusion

This project demonstrates how NLP and Machine Learning can transform raw customer support data into actionable business intelligence.

It focuses on automation, interpretability, and scalability, making it useful for real-world customer support systems and enterprise analytics.
```

---