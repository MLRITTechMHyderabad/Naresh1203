from youtube_2025_dst import load_and_clean_dataset  # Correcting the import
from mysql_connection_ytb import connect_and_upload  # Corrected import based on the file name
from sql_query import  generate_insights
from matplot_visualization import plot_visuals

# File path to the dataset
file_path = r"C:\Users\appal\Downloads\youtube_2025.csv"

# Step 1: Load and clean the dataset into a DataFrame
df = load_and_clean_dataset(file_path)

# Step 2: MySQL database configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'root',
    'database': 'youtube2025'
}

# Step 3: Upload cleaned data to MySQL
connect_and_upload(df, db_config)

# Step 4: Run SQL insights based on the data in MySQL
generate_insights()   # Function in sql_query.py should handle the SQL querie

# Step 5: Generate visualizations based on the cleaned DataFrame
plot_visuals(df)
