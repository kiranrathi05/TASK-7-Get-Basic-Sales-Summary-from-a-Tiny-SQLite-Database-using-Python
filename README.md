# 📊 Sales Summary from SQLite using Python

This project demonstrates how to create a basic sales summary by:

- Creating and populating a SQLite database  
- Running SQL queries using Python  
- Loading data into a Pandas DataFrame  
- Visualizing results using Matplotlib

---

## 📁 Project Structure

```
sales_summary_project/
│
├── task7.py # Main script to create DB, run SQL, and plot results
├── sales_data.db # SQLite database (created at runtime)
├── sales_chart.png # Bar chart of revenue by product (auto-generated)
└── README.md # Project documentation
```


---

## 🚀 Requirements

Make sure you have the following Python packages installed:

```bash
pip install pandas matplotlib "numpy<2.0"
```

---> ⚠️ Important: Use numpy<2.0 to avoid compatibility issues with libraries like Matplotlib that may not yet support NumPy 2.x fully.

---

## 🧠 What This Script Does
  - Creates a SQLite database and a sales table
  - Inserts sample sales records
  - Runs an SQL query to compute total quantity and revenue per product
  - Loads the result into Pandas and visualizes it as a bar chart using Matplotlib

---

## 📝 Sample Output (Console)

```

    product  total_qty  revenue
0  Notebook         12    240.0
1      Pen          18     90.0
2    Pencil         25     50.0

```
## 📊 Sample Chart Output

  - A bar chart named sales_chart.png will be generated, showing revenue by product type.


