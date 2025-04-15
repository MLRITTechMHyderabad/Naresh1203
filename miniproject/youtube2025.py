import pandas as pd
import os
import mysql.connector
from sqlalchemy import create_engine
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

    # Path to your CSV file
file_path = 'youtube_2025.csv'
try:
        # Check if file exists
        if not os.path.exists(r"C:\Users\appal\Downloads\youtube_2025.csv"):
            raise FileNotFoundError(f"The file {r"C:\Users\appal\Downloads\youtube_2025.csv"} does not exist. Please check the path.")

        # Read CSV using pandas
        df = pd.read_csv(r"C:\Users\appal\Downloads\youtube_2025.csv")

        # Display first 5 rows
        print(" Dataset Loaded Successfully!\n")
        print(df.head())

        # Show basic info
        print("\n Dataset Info:")
        print(df.info())

except FileNotFoundError as fnf_error:
        print(f" File Error: {fnf_error}")

except pd.errors.ParserError as parse_error:
        print(f" Parsing Error: {parse_error}")

except Exception as e:
        print(f" An unexpected error occurred: {e}")


# --------------------  Data Cleaning --------------------

#  Remove duplicate rows
df = df.drop_duplicates()
print("\n Removed duplicate rows.")

#  Handle missing/null values
print("\n Missing Values Before:")
print(df.isnull().sum())

# Option 1: Drop rows with any missing values (simple strategy)
df = df.dropna()

# (Optional: you can also use df.fillna(value) if specific strategy needed)
print("\n Missing values handled. Current nulls:")
print(df.isnull().sum())

# Rename columns for clarity
rename_columns = {
    'Channel Name': 'Channel_Name',
    'Youtuber Name': 'Youtuber_Name',
    'Total Videos': 'Total_Videos',
    'Best Video': 'Best_Video',
    'Avg Video Length (min)': 'Avg_Video_Length',
    'Total Subscribers': 'Total_Subscribers',
    'Members Count': 'Members_Count',
    'AI Generated Content (%)': 'AI_Generated_Content_Percent',
    'Neural Interface Compatible': 'Neural_Interface_Compatible',
    'Metaverse Integration Level': 'Metaverse_Integration_Level',
    'Quantum Computing Topics': 'Quantum_Computing_Topics',
    'Holographic Content Rating': 'Holographic_Content_Rating',
    'Engagement Score': 'Engagement_Score',
    'Content Value Index': 'Content_Value_Index'
}
df.rename(columns=rename_columns, inplace=True)
print("\n Columns renamed:")
print(df.columns)

# Convert data types of numeric columns
columns_to_convert = [
    'Total_Videos',
    'Avg_Video_Length',
    'Total_Subscribers',
    'Members_Count',
    'AI_Generated_Content_Percent',
    'Holographic_Content_Rating',
    'Engagement_Score',
    'Content_Value_Index'
]

for col in columns_to_convert:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors='coerce')

print("\n Data types corrected.")

# Filter irrelevant/noisy data
if 'Total_Videos' in df.columns:
    df = df[df['Total_Videos'] >= 10]

if 'Total_Subscribers' in df.columns:
    df = df[df['Total_Subscribers'] >= 100]

if 'Engagement_Score' in df.columns:
    df = df[df['Engagement_Score'] >= 0]

if 'Content_Value_Index' in df.columns:
    df = df[df['Content_Value_Index'] >= 0]

print("\n Noisy data filtered.")

# -------------------- mysql Integration --------------------

# Connect to MySQL using mysql.connector for table creation and specific queries
try:
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='root',
        database='youtube2025'
    )
    cursor = conn.cursor()
    print("\nconnected to MYSQL database successfully")

    # Create table structure if it doesn't exist
    create_table= """
    CREATE TABLE IF NOT EXISTS youtube_2025 (
        Channel_Name VARCHAR(255),
        Youtuber_Name VARCHAR(255),
        Total_Videos INT,
        Best_Video VARCHAR(255),
        Avg_Video_Length FLOAT,
        Total_Subscribers INT,
        Members_Count INT,
        AI_Generated_Content_Percent FLOAT,
        Neural_Interface_Compatible BOOLEAN,
        Metaverse_Integration_Level INT,
        Quantum_Computing_Topics TEXT,
        Holographic_Content_Rating VARCHAR(250),
        Engagement_Score FLOAT,
        Content_Value_Index FLOAT
    );
    """
    cursor.execute(create_table)
    print("\nTable structure Created/Verified.")

    # Use SQLAlchemy for bulk insert of the cleaned dataset
    engine = create_engine("mysql+mysqlconnector://root:root@localhost/youtube2025")
    df.to_sql('youtube_2025', con=engine, if_exists='replace', index=False)
    print("\nData migrated successfully to the 'youtube_2025' table using SQLAlchemy!")

    # Verify migration using cursor
    cursor.execute("SELECT * FROM youtube_2025 LIMIT 5")
    print("\nSample rows from MySQL (using cursor):")
    for row in cursor.fetchall():
        print(row)

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    cursor.close()
    conn.close()
    print("\nMySQL connection closed.")
    # -------------------- Analytical Insights --------------------

print("\n   Key Analytical Insights ")

# 1. Total number of videos
if 'Total_Videos' in df.columns:
    total_video_count = df['Total_Videos'].sum()
    print(f" Total Videos Uploaded Across All Channels: {total_video_count}")
# 2. Most viewed categories
combined = df.groupby('Quantum_Computing_Topics', as_index=False)[['Total_Videos', 'Engagement_Score']].sum()
top_combined = combined.sort_values(by=['Total_Videos', 'Engagement_Score'], ascending=False).head(5)
print("\nTop 5 Topics by Total Videos and Engagement Score:")
print(top_combined)
# Average for relevant numerical columns
average_videos = df['Total_Videos'].mean()
average_subscribers = df['Total_Subscribers'].mean()
average_members = df['Members_Count'].mean()
average_content_value = df['Content_Value_Index'].mean()

print(f"Average Total Videos: {average_videos}")
print(f"Average Total Subscribers: {average_subscribers}")
print(f"Average Members Count: {average_members}")
print(f"Average Content Value Index: {average_content_value}")

# Distribution of Total Videos by Channel Name
channel_video_distribution = df.groupby('Channel_Name')['Total_Videos'].sum().sort_values(ascending=False)
print("\nDistribution of Total Videos by Channel:")
print(channel_video_distribution)

# Trends based on Metaverse Integration Level
metaverse_trends = df.groupby('Metaverse_Integration_Level')['Engagement_Score'].mean()

print("\nTrends Based on Metaverse Integration Level:")
print(metaverse_trends)

#  #  # #             6.visualization     #  #  #  # 
head_df = df.head()

# Manually summarize based on head
summary_from_head = pd.DataFrame({
    "Min": head_df.min(numeric_only=True),
    "Max": head_df.max(numeric_only=True),
    "Mean": head_df.mean(numeric_only=True),
    "Std Dev": head_df.std(numeric_only=True)
})

print("\nSummary Statistics (based on head rows):")
print(summary_from_head)

# --- PIE CHART 1: Metaverse Integration Level 
plt.figure(figsize=(10, 8))
metaverse_counts = df['Metaverse_Integration_Level'].value_counts()
plt.pie(metaverse_counts, labels=metaverse_counts.index, autopct='%1.1f%%', startangle=140)
plt.title('Metaverse Integration Level Distribution')
plt.show()

#  PIE CHART 2: Neural Interface Compatibility 
plt.figure(figsize=(10, 8))
neural_counts = df['Neural_Interface_Compatible'].value_counts()
plt.pie(neural_counts, labels=['Compatible', 'Not Compatible'], autopct='%1.1f%%', startangle=90)
plt.title('Neural Interface Compatibility')
plt.show()

# 2. Top trending videos based on Engagement Score
top_trending_videos = df[['Best_Video', 'Engagement_Score']].sort_values(by='Engagement_Score', ascending=False).head(10)
print("\nTop Trending Videos (based on Engagement Score):")
print(top_trending_videos)

#   BAR CHART: Top 10 Trending Videos 
plt.figure(figsize=(10, 8))
top_videos = df.sort_values(by='Engagement_Score', ascending=False).head(10)
plt.barh(top_videos['Best_Video'], top_videos['Engagement_Score'], color='skyblue')
plt.xlabel('Engagement Score')
plt.title('Top 10 Trending Videos by Engagement Score')
plt.gca().invert_yaxis()
plt.tight_layout()
plt.show()

# 3. Category-wise comparison: Metaverse Integration Level vs. Content Value Index
category_comparison = df.groupby('Metaverse_Integration_Level')['Content_Value_Index'].mean().sort_values(ascending=False)
print("\nCategory-wise Comparison (Metaverse Integration Level vs. Content Value Index):")
print(category_comparison)


