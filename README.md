# Real-Time Disaster Response and Emergency Management System

## Overview
This project is a comprehensive real-time system designed to monitor social media data during disasters, perform sentiment analysis, and detect emerging topics. The goal is to assist in disaster response and emergency management by providing actionable insights through an interactive dashboard.

## Project Structure and Tools Used

```plaintext
disaster-response-management/
│
├── data/
│   ├── raw/                                # Raw data files
│   ├── processed/                           # Processed data files
│   └── download_tweets.py                   # Script to collect tweets using Twitter API and Kafka
│
├── notebooks/                               # Jupyter notebooks for experimentation and analysis
│   ├── data_collection.ipynb                # Notebook for data collection process
│   ├── preprocessing.ipynb                  # Notebook for data preprocessing
│   ├── sentiment_analysis.ipynb             # Notebook for sentiment analysis
│   └── topic_modeling.ipynb                 # Notebook for topic modeling
│
├── models/                                  # Trained models and checkpoints
│   └── sentiment_model/                     # Fine-tuned BERT sentiment analysis model
│
├── scripts/                                 # Python scripts for various components of the project
│   ├── data_collection.py                   # Script for data collection using Kafka and Twitter API
│   ├── preprocess.py                        # Script for cleaning, tokenizing, and preparing tweets
│   ├── sentiment_analysis.py                # Script for performing sentiment analysis using BERT
│   ├── topic_modeling.py                    # Script for topic modeling using LDA
│   └── streamlit_app.py                     # Script for running the Streamlit dashboard
│
├── airflow/                                 # Airflow DAGs and configurations for data pipeline management
│   ├── dags/
│   │   └── data_pipeline_dag.py             # DAG file for orchestrating the workflow in Airflow
│   └── configs/
│
├── docker/                                  # Docker configuration files for containerization
│   ├── Dockerfile                           # Dockerfile to define the environment and dependencies
│   ├── docker-compose.yml                   # Docker Compose file for setting up the services
│   └── k8s/                                 # Kubernetes deployment files for production deployment
│
├── requirements.txt                         # List of all required Python dependencies
├── README.md                                # Project documentation
└── LICENSE                                  # License file for the project
```

### 1. Data Collection
**Tools Used:** 
- **Twitter API:** For streaming real-time tweets related to disasters.
- **Kafka:** For handling real-time data streams.
- **Tweepy:** Python library for accessing the Twitter API.

### 2. Data Preprocessing
**Tools Used:** 
- **NLTK:** For text preprocessing, including tokenization and stopword removal.
- **Hugging Face Transformers:** For tokenization compatible with BERT models.

### 3. Sentiment Analysis
**Tools Used:**
- **BERT (from Hugging Face):** Pre-trained model for sentiment analysis.
- **PyTorch:** For model inference and handling tensor operations.

### 4. Topic Modeling
**Tools Used:**
- **Scikit-learn:** For performing Latent Dirichlet Allocation (LDA) to identify topics in tweets.
- **CountVectorizer:** To convert tweets into a matrix of token counts.

### 5. Real-Time Dashboard
**Tools Used:**
- **Streamlit:** For creating an interactive dashboard to visualize sentiment analysis and topic trends.
- **Plotly:** For creating dynamic, interactive visualizations.
  
### 6. Workflow Orchestration
**Tools Used:**
- **Apache Airflow:** To automate and orchestrate data pipelines.

### 7. Containerization and Deployment
**Tools Used:**
- **Docker:** To containerize the application for consistency across different environments.
- **Docker Compose:** For managing multi-container Docker applications.
- **Kubernetes:** For orchestrating Docker containers in a production environment.

## Installation

### Prerequisites
- **Python 3.8+**
- **Docker & Docker Compose**
- **Apache Kafka & Zookeeper**
- **Apache Airflow**

### Setup Instructions

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/disaster-response-management.git
   cd disaster-response-management
   ```

2. **Install Dependencies:**
   Ensure you have Python 3.8+ installed. Then, install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up Kafka and Zookeeper:**
   Use Docker Compose to set up Kafka and Zookeeper:
   ```bash
   docker-compose up -d
   ```

4. **Run Airflow:**
   Initialize and run Airflow to manage the data pipelines:
   ```bash
   airflow initdb
   airflow scheduler & airflow webserver
   ```

5. **Run the Streamlit Dashboard:**
   Start the Streamlit app to visualize the data in real-time:
   ```bash
   streamlit run scripts/streamlit_app.py
   ```

6. **Access the Dashboard:**
   The dashboard will be accessible at `http://localhost:8501`. It will display real-time sentiment analysis and trending topics based on the streamed tweets.

## Project Workflow

1. **Data Collection:** Tweets are collected in real-time using the Twitter API and streamed to Kafka.
2. **Data Preprocessing:** Collected tweets are cleaned, tokenized, and preprocessed for analysis.
3. **Sentiment Analysis:** Preprocessed tweets are analyzed to determine the sentiment (positive, neutral, negative).
4. **Topic Modeling:** Key topics within the tweets are identified using LDA.
5. **Visualization:** The results are visualized in a real-time Streamlit dashboard.
6. **Orchestration:** Apache Airflow is used to automate and orchestrate the entire workflow.

## Deployment

### Docker
- The project is containerized using Docker for easy deployment and scalability. Docker Compose is used to manage multi-container applications.

### Kubernetes
- For production-level deployment, the project includes Kubernetes deployment files to orchestrate the Docker containers.

## Usage

### Running Locally
- Follow the installation instructions to set up the environment and run the components locally.

### Running in Production
- Use the Kubernetes files in the `docker/k8s/` directory to deploy the project on a cloud-based Kubernetes cluster.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
