import matplotlib.pyplot as plt

def plot_visuals(df):
    try:
        # Pie Chart 1: Metaverse Integration Level
        if 'Metaverse_Integration_Level' in df.columns:
            plt.figure(figsize=(10, 8))
            metaverse_counts = df['Metaverse_Integration_Level'].value_counts()
            plt.pie(metaverse_counts, labels=metaverse_counts.index, autopct='%1.1f%%', startangle=140)
            plt.title('Metaverse Integration Level Distribution')
            plt.show()
        else:
            print(" 'Metaverse_Integration_Level' column is missing from the DataFrame.")

        # Pie Chart 2: Neural Interface Compatibility
        if 'Neural_Interface_Compatible' in df.columns:
            plt.figure(figsize=(10, 8))
            neural_counts = df['Neural_Interface_Compatible'].value_counts()
            plt.pie(neural_counts, labels=['Compatible', 'Not Compatible'], autopct='%1.1f%%', startangle=90)
            plt.title('Neural Interface Compatibility')
            plt.show()
        else:
            print(" 'Neural_Interface_Compatible' column is missing from the DataFrame.")

        # Bar Chart: Top 10 Trending Videos
        if 'Best_Video' in df.columns and 'Engagement_Score' in df.columns:
            top_videos = df.sort_values(by='Engagement_Score', ascending=False).head(10)
            plt.figure(figsize=(10, 8))
            plt.barh(top_videos['Best_Video'], top_videos['Engagement_Score'], color='skyblue')
            plt.xlabel('Engagement Score')
            plt.title('Top 10 Trending Videos by Engagement Score')
            plt.gca().invert_yaxis()
            plt.tight_layout()
            plt.show()
        else:
            print(" 'Best_Video' or 'Engagement_Score' columns are missing from the DataFrame.")

        # Summary from head rows
        head_df = df.head()
        summary = head_df.describe().T[['min', 'max', 'mean', 'std']]
        print("\n Summary Statistics (based on head rows):")
        print(summary)

    except Exception as e:
        print(f" Error during visualization: {e}")
