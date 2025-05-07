# youtube_2025_dataset.py

import pandas as pd
import os

def load_and_clean_dataset(file_path):
    try:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"The file {file_path} does not exist. Please check the path.")

        df = pd.read_csv(file_path)
        print("Dataset Loaded Successfully!\n")
      # print(df.head())
        print("\nDataset Info:")
      # print(df.info())

        # Remove duplicate rows
        df = df.drop_duplicates()
        print("\nRemoved duplicate rows.")

        # Handle missing values
        print("\nMissing Values Before:")
        print(df.isnull().sum())
        df = df.dropna()
        print("\nMissing values handled. Current nulls:")
        print(df.isnull().sum())

        # Rename columns
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
        print("\nColumns renamed:")
        #rint(df.columns)

        # Convert data types
        numeric_cols = [
            'Total_Videos', 'Avg_Video_Length', 'Total_Subscribers', 'Members_Count',
            'AI_Generated_Content_Percent', 'Holographic_Content_Rating',
            'Engagement_Score', 'Content_Value_Index'
        ]
        for col in numeric_cols:
            if col in df.columns:
                df[col] = pd.to_numeric(df[col], errors='coerce')

        print("\nData types corrected.")

        # Filter noise
        df = df[df['Total_Videos'] >= 10]
        df = df[df['Total_Subscribers'] >= 100]
        df = df[df['Engagement_Score'] >= 0]
        df = df[df['Content_Value_Index'] >= 0]

        print("\nNoisy data filtered.")

        return df.head(5)

    except FileNotFoundError as e:
        print(f"File Error: {e}")
    except pd.errors.ParserError as e:
        print(f"Parsing Error: {e}")
    except Exception as e:
        print(f"Unexpected Error: {e}")
