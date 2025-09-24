# Frameworks_Assignment
# CORD-19 Data Explorer

## Overview
This project analyzes the CORD-19 dataset's metadata to explore trends in COVID-19 research. It includes data loading, cleaning, analysis, visualization, and a Streamlit web app.

## Findings
- **Publication Trends**: Most papers were published in 2020–2021, peaking during the height of the pandemic.
- **Top Journals**: Journals like *The Lancet* and *Nature* published significant COVID-19 research.
- **Frequent Words**: Common title words include "COVID-19", "coronavirus", "pandemic", and "SARS-CoV-2".
- **Sources**: PubMed and bioRxiv are the primary sources of papers.

## Visualizations
1. **Publications by Year**: Line chart showing the trend of publications over time.
2. **Top Journals**: Bar chart of the top 10 journals by paper count.
3. **Word Cloud**: Visual representation of frequent words in paper titles.
4. **Source Distribution**: Bar chart of paper counts by source.

## Challenges
- Handling missing data in columns like `abstract` and `publish_time`.
- Managing the large dataset size, which required efficient filtering.
- Learning Streamlit for the first time to create an interactive app.

## Learning Outcomes
- Gained experience with pandas for data manipulation.
- Learned to create visualizations with matplotlib and seaborn.
- Built a functional Streamlit app for interactive data exploration.
- Improved debugging and problem-solving skills.

## How to Run
1. Install dependencies: `pip install pandas matplotlib seaborn streamlit wordcloud`
2. Run the Streamlit app: `streamlit run app.py`
3. Open the provided URL in a browser to view the app.
