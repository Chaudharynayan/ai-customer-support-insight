# 📄 Design Document  
## AI-Powered Customer Support Insight Platform

---

# 1. 🧠 AI Choices

This project uses a combination of pre-trained NLP models and classical machine learning techniques to analyze customer support tickets.

### 🔹 Sentiment Analysis
- **Model:** `distilbert-base-uncased-finetuned-sst-2-english`
- **Library:** Hugging Face Transformers
- **Reason for choice:**
  - Lightweight and fast inference
  - Pre-trained on SST-2 dataset
  - Good accuracy for binary sentiment classification (POSITIVE / NEGATIVE)

---

### 🔹 Ticket Categorization (Zero-Shot Learning)
- **Model:** `facebook/bart-large-mnli`
- **Type:** Zero-shot classification
- **Reason for choice:**
  - No need for labeled training data
  - Flexible category definition
  - Suitable for dynamic business environments

---

### 🔹 Embeddings for Clustering
- **Model:** `all-MiniLM-L6-v2`
- **Library:** Sentence Transformers
- **Reason for choice:**
  - Efficient and lightweight embedding model
  - Captures semantic similarity between customer complaints
  - Good balance between speed and accuracy

---

### 🔹 Clustering Algorithm
- **Algorithm:** KMeans
- **Reason for choice:**
  - Simple and scalable
  - Works well on embedding vectors
  - Good baseline for grouping similar complaints

---

# 2. 📊 Data Model

Each customer support ticket is transformed into a structured format:

### 🔹 Schema

- **ticket_id** → Unique identifier  
- **timestamp** → Time of complaint  
- **customer_id** → Customer reference ID  
- **message** → Raw customer complaint text  
- **sentiment** → AI-generated sentiment label  
- **category** → AI-generated issue category  
- **order_value** → Monetary value of transaction  
- **business_risk** → Risk classification (High / Low)  
- **cluster** → KMeans cluster group  
- **suggested_response** → AI-generated support reply  

---

### 🔹 Data Flow
1. Raw ticket dataset (CSV)
2. Preprocessing using Pandas
3. NLP transformations:
   - Sentiment analysis
   - Zero-shot classification
   - Embedding generation
4. Feature engineering:
   - Risk scoring
   - Clustering
5. Storage:
   - SQLite database
   - Processed CSV file

---

# 3. 📈 Scalability

The system is designed to be extendable and production-ready.

### 🔹 Horizontal Scaling
- Can handle increased ticket volume by:
  - Batch processing embeddings
  - Using distributed systems (e.g., Spark in future)

### 🔹 Real-Time Expansion
- Can be upgraded to:
  - Kafka streaming pipeline
  - Live ticket ingestion system

### 🔹 Model Scalability
- Replace models with:
  - Fine-tuned domain-specific transformers
  - Larger LLM-based classification models

### 🔹 Database Scaling
- Current: SQLite (local storage)
- Future:
  - PostgreSQL / MySQL for production
  - Cloud databases (AWS RDS, BigQuery)

---

# 4. ⚖️ Tradeoffs

| Component | Decision | Tradeoff |
|----------|----------|----------|
| DistilBERT | Fast sentiment model | Lower accuracy than large BERT models |
| Zero-Shot BART | No training required | Slower inference time |
| MiniLM Embeddings | Lightweight & fast | Less expressive than large embedding models |
| KMeans Clustering | Simple & interpretable | Not effective for complex/non-spherical clusters |
| Streamlit UI | Fast development | Limited enterprise scalability |

---

# 5. 🎯 System Goals Achieved

✔ Automated ticket classification  
✔ Sentiment-driven analysis  
✔ Business risk detection  
✔ Revenue impact tracking  
✔ AI-generated support responses  
✔ Interactive analytics dashboard  

---

# 6. 🚀 Future Improvements

- Fine-tuned transformer model on domain data
- Real-time ticket streaming system
- LLM-powered chatbot integration
- Churn prediction model
- Multi-language support system

---
```