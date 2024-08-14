import streamlit as st
import plotly.express as px
import pandas as pd

# Example sentiment data
sentiment_data = {'Sentiment': ['Positive', 'Neutral', 'Negative'], 'Count': [100, 50, 30]}
df_sentiment = pd.DataFrame(sentiment_data)

# Example topic data
topic_data = {'Topic': ['Earthquake', 'Flood', 'Hurricane'], 'Count': [80, 60, 40]}
df_topic = pd.DataFrame(topic_data)

# Streamlit app layout
st.title('Real-Time Disaster Response and Emergency Management')
st.subheader('Sentiment Analysis')

# Sentiment analysis bar chart
fig_sentiment = px.bar(df_sentiment, x='Sentiment', y='Count', color='Sentiment', title="Sentiment Distribution")
st.plotly_chart(fig_sentiment)

st.subheader('Trending Topics')

# Trending topics bar chart
fig_topics = px.bar(df_topic, x='Topic', y='Count', color='Topic', title="Trending Topics")
st.plotly_chart(fig_topics)
