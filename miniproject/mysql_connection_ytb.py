# mysql_connection.py

import mysql.connector
from sqlalchemy import create_engine

def connect_and_upload(df, db_config):
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        print("\nConnected to MySQL database successfully.")

        # Create table if it doesn't exist
        create_table = """
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
        print("Table structure created/verified.")

        # Use SQLAlchemy to insert the DataFrame
        engine = create_engine(f"mysql+mysqlconnector://{db_config['user']}:{db_config['password']}@{db_config['host']}/{db_config['database']}")
        df.to_sql('youtube_2025', con=engine, if_exists='replace', index=False)
        print("Data migrated to MySQL successfully.")

        # Sample records
        cursor.execute("SELECT * FROM youtube_2025 LIMIT 5")
        for row in cursor.fetchall():
            print(row)

    except mysql.connector.Error as err:
        print(f"MySQL Error: {err}")
    finally:
        cursor.close()
        conn.close()
        print("MySQL connection closed.")
