# Creating Database for Storing Transactions
import sqlite3

# Connect to the database (or create it if it doesn't exist)
conn = sqlite3.connect("finance_tracker.db")
cursor = conn.cursor()

# Create table for transactions
cursor.execute('''CREATE TABLE IF NOT EXISTS transactions (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    date TEXT,
                    type TEXT,
                    category TEXT,
                    amount REAL
                )''')

conn.commit()
conn.close()
print("Database and table created successfully.")
# This ensures that transactions are stored persistently. The database is created if it doesn't exist, and a table is created to store transactions. The table has columns for the data, type, category, and amount of each transaction. The connection is then closed.
# The database is created in the same directory as the script, and the table is created with the specified columns. The connection is then closed to ensure that the database is not locked and can be accessed by other processes.
# The script prints a message to indicate that the database and table were created successfully. This can be useful for debugging and verifying that the database was created as expected.
# The script is now ready to store transactions in the database. The next step is to implement the functionality to insert, update, and retrieve transactions from the database.
# Add Income & Expense Transactions
def add_transaction(transaction_type, category, amount):
    conn = sqlite3.connect("finance_tracker.db")
    cursor = conn.cursor()
    
    from datetime import datetime
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    cursor.execute("INSERT INTO transactions (date, type, category, amount) VALUES (?, ?, ?, ?)",
                   (date, transaction_type, category, amount))
    
    conn.commit()
    conn.close()
    print(f"Transaction added: {transaction_type} of ${amount} under {category}")
# The add_transaction function takes three arguments: transaction_type, category, and amount. It inserts a new transaction into the database with the current date and time, the specified type, category, and amount.
# The function first establishes a connection to the database and creates a cursor to execute SQL queries. It then gets the current date and time using the datetime module and formats it as a string.
# The function then executes an SQL query to insert the transaction into the transactions table with the provided values. The query uses placeholders (?) to prevent SQL injection attacks and ensure safe parameterized queries.
# This function allows users to add income or expenses dynamically. The transactions are stored in the database with the current date and time, the type (income or expense), the category, and the amount.
# The function commits the changes to the database and closes the connection. It also prints a message to indicate that the transaction was successfully added.

# Example Usage
# add_transaction("Income", "Salary", 5000)
# add_transaction("Expense", "Rent", 1500)
# add_transaction("Expense", "Groceries", 200)

# Fetch and Display Transactions
from tabulate import tabulate

def view_transactions():
    conn = sqlite3.connect("finance_tracker.db")
    cursor = conn.cursor()
    
    cursor.execute("SELECT date, type, category, amount FROM transactions")
    rows = cursor.fetchall()
    
    conn.close()
    
    if not rows:
        print("No transactions found.")
        return
    
    print(tabulate(rows, headers=["Date", "Type", "Category", "Amount"], tablefmt="grid"))

# Example usage
view_transactions()

# The view_transactions function fetches all transactions from the database and displays them in a tabular format using the tabulate library. It first establishes a connection to the database and creates a cursor to execute SQL queries.
# The function then executes an SQL query to select all columns (date, type, category, amount) from the transactions table. It fetches all rows returned by the query and stores them in the rows variable.
# The function then closes the connection to the database. If no transactions are found in the database, the function prints a message indicating that no transactions were found and returns early.
# If transactions are found, the function uses the tabulate function to display the transactions in a tabular format with headers for each column. The table is printed using the grid table format.

# Generate a Financial Summary
def financial_summary():
    conn = sqlite3.connect("finance_tracker.db")
    cursor = conn.cursor()
    
    cursor.execute("SELECT SUM(amount) FROM transactions WHERE type='Income'")
    total_income = cursor.fetchone()[0] or 0

    cursor.execute("SELECT SUM(amount) FROM transactions WHERE type='Expense'")
    total_expenses = cursor.fetchone()[0] or 0

    savings = total_income - total_expenses
    
    conn.close()
    
    print("\n💰 Financial Summary 💰")
    print(f"Total Income: ${total_income}")
    print(f"Total Expenses: ${total_expenses}")
    print(f"Net Savings: ${savings}")

# Example usage
financial_summary()

# This function calculates total income, expenses, and savings. It first establishes a connection to the database and creates a cursor to execute SQL queries.
# The function then executes two SQL queries to calculate the sum of amounts for income and expenses separately. It fetches the results of the queries and stores them in total_income and total_expenses variables.
# If no income or expenses are found, the function sets the corresponding total to 0 using the or operator. The function then calculates the net savings by subtracting total expenses from total income.
# The function closes the connection to the database and prints a financial summary with the total income, total expenses, and net savings.

# Data Visualization (Pie Chart of Expenses)
import matplotlib.pyplot as plt
import pandas as pd

def plot_expenses():
    conn = sqlite3.connect("finance_tracker.db")
    cursor = conn.cursor()
    
    cursor.execute("SELECT category, SUM(amount) FROM transactions WHERE type='Expense' GROUP BY category")
    data = cursor.fetchall()
    
    conn.close()
    
    if not data:
        print("No expenses recorded yet.")
        return
    
    categories, amounts = zip(*data)
    
    plt.figure(figsize=(8, 6))
    plt.pie(amounts, labels=categories, autopct='%1.1f%%', startangle=140, colors=['#ff9999','#66b3ff','#99ff99','#ffcc99'])
    plt.title("Expense Distribution")
    plt.show()

# Example usage
plot_expenses()

# This function creates a pie chart showing expense distribution by category. It first establishes a connection to the database and creates a cursor to execute SQL queries.
# The function then executes an SQL query to select the category and sum of amounts for expenses, grouped by category. It fetches the results of the query and stores them in the data variable.
# The function then closes the connection to the database. If no expenses are found, the function prints a message indicating that no expenses were recorded and returns early.

# Export Data to CSV
def export_to_csv():
    conn = sqlite3.connect("finance_tracker.db")
    df = pd.read_sql_query("SELECT * FROM transactions", conn)
    conn.close()
    
    df.to_csv("finance_data.csv", index=False)
    print("📁 Data exported to finance_data.csv")

# Example usage
export_to_csv()

# Allows users to export financial data for further analysis in Excel. The function first establishes a connection to the database and reads all transactions into a pandas DataFrame using the read_sql_query function.
# The function then closes the connection to the database. The DataFrame is then exported to a CSV file named finance_data.csv using the to_csv method.
# The function prints a message to indicate that the data was successfully exported to the CSV file.