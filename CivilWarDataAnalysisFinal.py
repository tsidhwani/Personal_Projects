import os
import re
import string
from nltk.corpus import stopwords
from textblob import TextBlob
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

root = '/Users/tapansidhwani/CivilWarDataAnalysis'

stop_words = set(stopwords.words('english'))

#keywrods for frequency visualization
keywords = ["demoralized", "support", "patriotism", "war", "loyalty", "slavery", 
            "freedom", "poverty", "bravery", "victory", "sacrifice", "disaster", "bias"]
articles = []

def clean_text(text):
    """Clean and preprocess text by lowercasing, removing punctuation, and filtering stopwords."""
    text = text.lower()  
    text = re.sub(f"[{re.escape(string.punctuation)}]", "", text) 
    words = text.split()
    words = [word for word in words if word not in stop_words]  
    return " ".join(words)

for year in os.listdir(root):
    year_path = os.path.join(root, year)
    if os.path.isdir(year_path):
        for quarter in os.listdir(year_path):
            quarter_path = os.path.join(year_path, quarter)
            if os.path.isdir(quarter_path):
                for file in os.listdir(quarter_path):
                    if file.endswith('.txt'):
                        match = re.match(r"(\d{2})\.(\d{2})\.(\d{4})([A-Za-z]+)\.txt", file)
                        if match:
                            month, day, year, newspaper = match.groups()
                            file_path = os.path.join(quarter_path, file)
                            with open(file_path, 'r', encoding='utf-8') as f:
                                content = f.read()
                            cleaned_content = clean_text(content)
                            blob = TextBlob(cleaned_content)

                            #sentiment stuff try without polarity 
                            sentiment = blob.sentiment.polarity
                            
                            keyword_counts = {keyword: cleaned_content.count(keyword) for keyword in keywords} # Add all information to articles list
                            articles.append({
                                'year': year,
                                'quarter': quarter,
                                'date': f"{year}-{month}-{day}",
                                'newspaper': newspaper,
                                'content': content,
                                'cleaned_content': cleaned_content,
                                'sentiment': sentiment,
                                'keyword_counts': keyword_counts
                            })

df = pd.DataFrame(articles)

sentiment_by_quarter = df.groupby(['year', 'quarter'])['sentiment'].mean().reset_index()

keyword_counts_by_quarter = df.groupby(['year', 'quarter'], as_index=False).apply(
    lambda x: pd.DataFrame(x['keyword_counts'].tolist()).sum()
).reset_index()

#graphs
# Sentiment graph
plt.figure(figsize=(10, 6))
sns.lineplot(data=sentiment_by_quarter, x='quarter', y='sentiment', hue='year')
plt.title('Sentiment of Civil War Articles Over Time')
plt.xlabel('Quarter')
plt.ylabel('Average Sentiment')
plt.legend(title='Year')
plt.show()

# Generate a separate figure for each keyword frequency
for keyword in keywords:
    if keyword in keyword_counts_by_quarter.columns:
        plt.figure(figsize=(10, 6))
        sns.lineplot(data=keyword_counts_by_quarter, x='quarter', y=keyword, hue='year')
        plt.title(f'Keyword Frequency of "{keyword.capitalize()}" Over Time')
        plt.xlabel('Quarter')
        plt.ylabel('Keyword Frequency')
        plt.legend(title='Year')
        plt.show()
    else:
        print(f"Warning: '{keyword}' not found in keyword_counts_by_quarter columns.")


