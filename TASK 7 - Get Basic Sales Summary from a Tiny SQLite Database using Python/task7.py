# STEP 1: Create SQLite Database and Sales Table

import sqlite3

# Connect to SQLite DB
conn = sqlite3.connect("sales_data.db")
cursor = conn.cursor()

# Create a sales table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS sales (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        product TEXT,
        quantity INTEGER,
        price REAL
    )
''')
conn.commit()


# STEP 2: Insert Sample Data

# Insert sample data
sales_data = [
    ("Pen", 10, 5.0),
    ("Notebook", 5, 20.0),
    ("Pencil", 15, 2.0),
    ("Pen", 8, 5.0),
    ("Notebook", 7, 20.0),
    ("Pencil", 10, 2.0)
]

cursor.executemany("INSERT INTO sales (product, quantity, price) VALUES (?, ?, ?)", sales_data)
conn.commit()

# STEP 3: Run SQL Query to Summarize Sales

query = '''
SELECT product, 
       SUM(quantity) AS total_qty, 
       SUM(quantity * price) AS revenue 
FROM sales 
GROUP BY product
'''

# STEP 4: Load Results into Pandas and Plot

import pandas as pd
import matplotlib.pyplot as plt

# Load results
df = pd.read_sql_query(query, conn)
print(df)

# Plot bar chart
df.plot(kind='bar', x='product', y='revenue', color='skyblue')
plt.title("Revenue by Product")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig("sales_chart.png")  # Optional
plt.show()
