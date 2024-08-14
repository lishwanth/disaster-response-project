# Real-Time Disaster Response and Emergency Management System

## Overview
This project is a real-time system designed to monitor social media data during disasters, perform sentiment analysis, and detect emerging topics to assist in disaster response and emergency management.

### Key Features
- **Real-Time Data Collection**: Streams tweets related to disaster events (earthquakes, floods, hurricanes, etc.) using the Twitter API and Kafka.
- **Data Preprocessing**: Cleans and tokenizes the collected tweets, removing noise and irrelevant information.
- **Sentiment Analysis**: Classifies tweets into positive, neutral, or negative sentiments using a fine-tuned BERT model.
- **Topic Modeling**: Identifies key topics within the tweets using Latent Dirichlet Allocation (LDA).
- **Interactive Dashboard**: Provides real-time visualization of sentiment analysis and trending topics using Streamlit.

## Project Structure

- **data/**: Contains scripts for data collection and storage for raw and processed data.
  - `download_tweets.py`: Script for downloading disaster-related tweets.
  
- **notebooks/**: Jupyter notebooks for data collection, preprocessing, sentiment analysis, and topic modeling.
  - `data_collection.ipynb`: Notebook demonstrating real-time data collection using Twitter API and Kafka.
  - `preprocessing.ipynb`: Notebook for cleaning and tokenizing tweets.
  - `sentiment_analysis.ipynb`: Notebook for performing sentiment analysis using BERT.
  - `topic_modeling.ipynb`: Notebook for topic modeling using LDA.
  
- **models/**: Directory for storing the trained sentiment analysis models.

- **scripts/**: Python scripts for various components of the project.
  - `data_collection.py`: Script to collect tweets using Kafka and Twitter API.
  - `preprocess.py`: Script for preprocessing tweets (cleaning, tokenization).
  - `sentiment_analysis.py`: Script for performing sentiment analysis using a BERT model.
  - `topic_modeling.py`: Script for topic modeling with LDA.
  - `streamlit_app.py`: Script for running the Streamlit dashboard.

- **airflow/**: Contains Airflow DAGs and configurations for managing data pipelines.
  - `dags/data_pipeline_dag.py`: DAG for orchestrating data collection, preprocessing, and analysis workflows.
  
- **docker/**: Docker configuration files.
  - `Dockerfile`: Defines the environment for the project.
  - `docker-compose.yml`: Docker Compose configuration for multi-container setup.
  - `k8s/`: Kubernetes deployment files for production-level deployment.

- **requirements.txt**: List of all required Python dependencies.

- **README.md**: Detailed project documentation including installation, usage, and project structure.

- **LICENSE**: License file for the project.

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

## Project Components

### Data Collection
- The `download_tweets.py` script collects tweets using the Twitter API and streams them through Kafka.

### Data Preprocessing
- The `preprocess.py` script cleans, tokenizes, and preprocesses tweets for sentiment analysis.

### Sentiment Analysis
- The `sentiment_analysis.py` script uses a BERT-based model to classify tweets into positive, neutral, or negative sentiments.

### Topic Modeling
- The `topic_modeling.py` script applies LDA to identify and display key topics within the tweets.

### Real-Time Dashboard
- The `streamlit_app.py` script creates a Streamlit-based dashboard that provides real-time visualization of sentiment analysis and trending topics.

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
