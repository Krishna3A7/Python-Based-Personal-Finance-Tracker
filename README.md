# Python-Based-Personal-Finance-Tracker
The Personal Finance Tracker is a Python-based program that allows users to track their income, expenses, and savings efficiently. It provides data visualization using Matplotlib and Pandas, and stores financial records using SQLite for future access.

1. Requirements Gathering


Before developing the finance tracker, we need to understand the key requirements:

Functional Requirements:


✅ Users can add income sources (salary, freelancing, investments, etc.).

✅ Users can add expenses (food, rent, travel, utilities, etc.).

✅ Users can categorize expenses (e.g., "Essentials", "Entertainment", "Savings").

✅ Users can view a summary of total income, expenses, and savings.

✅ Users can generate monthly reports and visual charts.

✅ Users can export data to CSV files for record-keeping.


Non-Functional Requirements:
⚡ The application should be fast and responsive.

🔐 Data should be stored in a database (SQLite) for persistence.

📊 Users should be able to see a graphical report of their finances.

2. Implementation (Python Code)
   
The project is divided into several modules:

Step 1: Install Dependencies

Make sure you have the necessary libraries installed. Run:

pip install sqlite3 pandas matplotlib tabulate

Step 2: Create Database for Storing Transactions

Step 3: Add Income & Expense Transactions

Step 4: Fetch and Display Transactions

Step 5: Generate a Financial Summary

Step 6: Data Visualization (Pie Chart of Expenses)

Step 7: Export Data to CSV

To Run the Application required steps to be followed

Once all functions are implemented, we can integrate them into a simple menu-driven application:


def main():

    while True:
        
        print("\n📊 Personal Finance Tracker")
        
        print("1. Add Income")
        
        print("2. Add Expense")
        
        print("3. View Transactions")
        
        print("4. View Financial Summary")
        
        print("5. Plot Expenses")
        
        print("6. Export to CSV")
        
        print("7. Exit")

        
        choice = input("Enter your choice: ")

        
        if choice == "1":
        
            category = input("Enter income source (e.g., Salary, Investment): ")
            
            amount = float(input("Enter amount: "))
            
            add_transaction("Income", category, amount)

        
        
        elif choice == "2":
        
            category = input("Enter expense category (e.g., Rent, Food, Travel): ")
            
            amount = float(input("Enter amount: "))
            
            add_transaction("Expense", category, amount)

        
        
        elif choice == "3":
        
            view_transactions()

        
        
        elif choice == "4":
        
            financial_summary()

        
        
        elif choice == "5":
        
            plot_expenses()

        
        
        elif choice == "6":
        
            export_to_csv()

        
        
        elif choice == "7":
        
            print("Exiting...")
            
            break
        
        else
        
        :
        
            print("Invalid choice. Please try again.")


# Run the application

main()

This menu-driven interface allows users to interact with the finance tracker.


Conclusion


✅ We successfully designed and implemented a Personal Finance Tracker in Python.

✅ It allows income/expense tracking, financial summaries, charts, and data export.

✅ SQLite ensures data persistence.
