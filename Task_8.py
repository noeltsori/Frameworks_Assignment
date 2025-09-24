# Import required libraries
import pandas as pd

try:
    df = pd.read_csv('metadata.csv.zip')
except FileNotFoundError:
    print("File 'metadata.csv.zip' not found. Please check the file path.")
    df = None

if df is not None:
    # ...existing code for examining and cleaning df...
    print("First 5 rows of the dataset:")
    print(df.head())
    # (rest of your code)
else:
    print("DataFrame not created due to missing file.")
try:
    df = pd.read_csv('metadata.csv.zip')
except FileNotFoundError:
    print("File 'metadata.csv.zip' not found. Please check the file path.")
    df = None

if df is not None:
    # ...existing code for examining and cleaning df...
    print("First 5 rows of the dataset:")
    print(df.head())
    # (rest of your code)
else:
    print("DataFrame not created due to missing file.")
# Load the metadata.csv file
# Adjust the file path based on where you save the file
df = pd.read_csv('metadata.csv.zip')

# Examine the first  rows
print("First 5 rows of the dataset:")
print(df.head())

# Check DataFrame dimensions
print("\nDataFrame dimensions (rows, columns):")
print(df.shape)

# Identify data types of each column
print("\nData types of each column:")
print(df.info())

# Check for missing values
print("\nMissing values in each column:")
print(df.isnull().sum())

# Generate basic statistics for numerical columns
print("\nBasic statistics for numerical columns:")
print(df.describe())


# Handle missing data
# Drop columns with more than 80% missing values
threshold = 0.8 * len(df)
df = df.dropna(thresh=threshold, axis=1)

# Fill missing values in key columns
df['abstract'] = df['abstract'].fillna('No abstract')
df['publish_time'] = df['publish_time'].fillna('Unknown')

# Convert publish_time to datetime
df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')

# Extract year from publish_time
df['year'] = df['publish_time'].dt.year

# Create a new column for abstract word count
df['abstract_word_count'] = df['abstract'].apply(lambda x: len(str(x).split()) if x != 'No abstract' else 0)

# Display cleaned DataFrame info
print("\nCleaned DataFrame info:")
print(df.info())

# Save cleaned dataset (optional)
df.to_csv('cleaned_metadata.csv', index=False)


# Import visualization libraries
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
from collections import Counter
import re

# Count papers by publication year
year_counts = df['year'].value_counts().sort_index()

# Create a line chart for publications over time
plt.figure(figsize=(10, 6))
plt.plot(year_counts.index, year_counts.values, marker='o')
plt.title('Number of Publications by Year')
plt.xlabel('Year')
plt.ylabel('Number of Papers')
plt.grid(True)
plt.savefig('publications_by_year.png')
plt.show()

# Identify top 10 journals
top_journals = df['journal'].value_counts().head(10)

# Create a bar chart for top journals
plt.figure(figsize=(10, 6))
sns.barplot(x=top_journals.values, y=top_journals.index, palette='viridis')
plt.title('Top 10 Journals Publishing COVID-19 Research')
plt.xlabel('Number of Papers')
plt.ylabel('Journal')
plt.savefig('top_journals.png')
plt.show()

# Generate word cloud for titles
titles = ' '.join(df['title'].dropna().astype(str))
# Clean text (remove special characters, numbers)
titles = re.sub(r'[^a-zA-Z\s]', '', titles.lower())
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(titles)
plt.figure(figsize=(10, 6))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Word Cloud of Paper Titles')
plt.savefig('title_wordcloud.png')
plt.show()

# Plot distribution of paper counts by source
source_counts = df['source_x'].value_counts().head(10)
plt.figure(figsize=(10, 6))
sns.barplot(x=source_counts.values, y=source_counts.index, palette='magma')
plt.title('Distribution of Papers by Source')
plt.xlabel('Number of Papers')
plt.ylabel('Source')
plt.savefig('source_distribution.png')
plt.show()

# Most frequent words in titles
words = titles.split()
word_freq = Counter(words).most_common(20)
print("\nTop 20 most frequent words in titles:")
print(word_freq)


# Save as app.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
import re

# Load the cleaned dataset
df = pd.read_csv('cleaned_metadata.csv')

# Streamlit app layout
st.title("CORD-19 Data Explorer")
st.write("A simple web application to explore COVID-19 research papers from the CORD-19 dataset.")

# Interactive widget: Year range slider
min_year = int(df['year'].min())
max_year = int(df['year'].max())
year_range = st.slider("Select year range", min_year, max_year, (min_year, max_year))

# Filter data based on year range
filtered_df = df[(df['year'] >= year_range[0]) & (df['year'] <= year_range[1])]

# Display sample of the data
st.subheader("Sample Data")
st.dataframe(filtered_df[['title', 'journal', 'year', 'abstract_word_count']].head(10))

# Visualization 1: Publications by Year
st.subheader("Publications by Year")
year_counts = filtered_df['year'].value_counts().sort_index()
fig, ax = plt.subplots()
ax.plot(year_counts.index, year_counts.values, marker='o')
ax.set_title('Number of Publications by Year')
ax.set_xlabel('Year')
ax.set_ylabel('Number of Papers')
ax.grid(True)
st.pyplot(fig)

# Visualization 2: Top Journals
st.subheader("Top 10 Journals")
top_journals = filtered_df['journal'].value_counts().head(10)
fig, ax = plt.subplots()
sns.barplot(x=top_journals.values, y=top_journals.index, palette='viridis', ax=ax)
ax.set_title('Top 10 Journals Publishing COVID-19 Research')
ax.set_xlabel('Number of Papers')
ax.set_ylabel('Journal')
st.pyplot(fig)

# Visualization 3: Word Cloud
st.subheader("Word Cloud of Paper Titles")
titles = ' '.join(filtered_df['title'].dropna().astype(str))
titles = re.sub(r'[^a-zA-Z\s]', '', titles.lower())
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(titles)
fig, ax = plt.subplots()
ax.imshow(wordcloud, interpolation='bilinear')
ax.axis('off')
ax.set_title('Word Cloud of Paper Titles')
st.pyplot(fig)