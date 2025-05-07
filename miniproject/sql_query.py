# sql_query.py

import mysql.connector

def generate_insights():
    try:
        # Connect to MySQL
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='root',
            database='youtube2025'
        )
        cursor = conn.cursor()
        print("\n Key Analytical Insights\n")

        queries = [
            # 1. Total Videos Uploaded
            ("Total Videos Uploaded Across All Channels:",
             "SELECT SUM(Total_Videos) FROM youtube_2025"),

            # 2. Top 5 Topics by Total Videos and Engagement Score
            ("\nTop 5 Topics by Total Videos and Engagement Score:",
             """
             SELECT Quantum_Computing_Topics, 
                    SUM(Total_Videos) AS Total_Videos, 
                    SUM(Engagement_Score) AS Total_Engagement_Score
             FROM youtube_2025
             GROUP BY Quantum_Computing_Topics
             ORDER BY Total_Videos DESC, Total_Engagement_Score DESC
             LIMIT 5
             """),

            # 3. Averages
            ("\nAverages (Videos, Subscribers, Members, Content Value Index):",
             """
             SELECT AVG(Total_Videos), AVG(Total_Subscribers),
                    AVG(Members_Count), AVG(Content_Value_Index)
             FROM youtube_2025
             """),

            # 4. Distribution of Total Videos by Channel
            ("\nDistribution of Total Videos by Channel:",
             """
             SELECT Channel_Name, SUM(Total_Videos) AS Total_Videos
             FROM youtube_2025
             GROUP BY Channel_Name
             ORDER BY Total_Videos DESC
             """),

            # 5. Trends Based on Metaverse Integration Level
            ("\nTrends Based on Metaverse Integration Level:",
             """
             SELECT Metaverse_Integration_Level,
                    AVG(Engagement_Score) AS Avg_Engagement_Score
             FROM youtube_2025
             GROUP BY Metaverse_Integration_Level
             """),

            # 6. Top Trending Videos
            ("\nTop Trending Videos (based on Engagement Score):",
             """
             SELECT Best_Video, Engagement_Score
             FROM youtube_2025
             ORDER BY Engagement_Score DESC
             LIMIT 10
             """),

            # 7. Metaverse Level vs. Content Value Index
            ("\nCategory-wise Comparison (Metaverse Integration Level vs Content Value Index):",
             """
             SELECT Metaverse_Integration_Level,
                    AVG(Content_Value_Index) AS Avg_Content_Value_Index
             FROM youtube_2025
             GROUP BY Metaverse_Integration_Level
             ORDER BY Avg_Content_Value_Index DESC
             """)
        ]

        # Execute and display results
        for description, query in queries:
            print(description)
            cursor.execute(query)
            results = cursor.fetchall()
            for row in results:
                print(row)
            print("\n" + "-"*50 + "\n")

    except mysql.connector.Error as err:
        print(f" MySQL Error: {err}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()
        print(" MySQL connection closed.\n")
