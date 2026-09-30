# 📈 Stock Portfolio Tracker

A feature-rich console-based Stock Portfolio Tracker built with Python. This project allows users to manage stock investments, calculate portfolio value, generate statistics, and export reports to CSV files.

Developed as part of the **CodeAlpha Python Programming Internship – Task 2**.

---

## 🚀 Features

### 📊 Portfolio Management
- Add stocks to your portfolio
- Remove stocks completely or partially
- Track quantities owned
- Manage multiple stock holdings

### 💹 Investment Tracking
- Calculate individual stock values
- Calculate total portfolio value
- View current investment breakdown

### 📈 Portfolio Statistics
- Total portfolio value
- Total number of shares owned
- Highest-valued holding
- Number of unique stocks

### 💾 CSV Report Generation
- Export portfolio data to CSV format
- Automatically generates timestamped reports
- Includes investment summary

### ✅ Input Validation
- Validates stock symbols
- Prevents invalid quantities
- Handles user input errors gracefully

---

## 🛠 Technologies Used

- Python 3
- CSV Module
- Datetime Module
- Dictionaries
- Functions
- Loops
- Conditional Statements
- Exception Handling
- File Handling

---

## 📂 Project Structure

```text
StockPortfolio/
│
├── main.py
├── README.md
└── portfolio_report_YYYYMMDD_HHMMSS.csv
```

---

## 📋 Available Stocks

The application uses a predefined stock price dictionary:

```python
STOCK_PRICES = {
    "AAPL": 180.00,
    "TSLA": 250.00,
    "GOOGL": 140.00,
    "MSFT": 420.00,
    "AMZN": 170.00,
    "META": 480.00,
    "NVDA": 850.00
}
```

---

## 🖥 Menu Options

```text
===================================
===== STOCK PORTFOLIO TRACKER =====
===================================

1. Add Stock
2. Remove Stock
3. View Portfolio
4. Calculate Total Investment & Stats
5. Save Report to CSV
6. Exit
```

---

## ▶️ How to Run

### Clone the Repository

```bash
git clone https://github.com/Syed-Nazeer-07/StockPortfolio.git
```

### Navigate to the Project Folder

```bash
cd StockPortfolio
```

### Run the Program

```bash
python main.py
```

---

## 🎯 Example Workflow

### Add Stocks

```text
Enter stock symbol: AAPL
Enter quantity owned: 10

Successfully added 10 shares of AAPL.
```

### View Portfolio

```text
Symbol     | Quantity   | Price/Share     | Total Value
-----------------------------------------------------------
AAPL       | 10         | $180.00         | $1800.00
MSFT       | 5          | $420.00         | $2100.00
```

### Portfolio Statistics

```text
Total Portfolio Value:    $3,900.00
Total Number of Shares:   15
Highest Valued Holding:   MSFT ($2,100.00)
Number of Unique Stocks:  2
```

---

## 📄 CSV Report Export

The application can generate a detailed CSV report containing:

- Stock Symbol
- Quantity
- Price Per Share
- Total Value
- Portfolio Summary

Example generated file:

```text
portfolio_report_20250908_143015.csv
```

---

## 🎓 Internship Task

### CodeAlpha Python Programming Internship

**Task 2: Stock Portfolio Tracker**

#### Objective

Build a stock portfolio tracker that:

- Accepts stock names and quantities from users
- Uses a predefined dictionary for stock prices
- Calculates total investment value
- Saves portfolio reports using file handling

This implementation extends the basic requirements by adding portfolio statistics, stock removal functionality, and CSV export support.

---

## 🌟 Future Enhancements

Potential improvements include:

- Real-time stock prices using APIs
- Profit/Loss calculations
- Portfolio performance tracking
- Stock search functionality
- Data visualization with Matplotlib
- Database integration
- GUI version using Tkinter
- User authentication system

---

## 👨‍💻 Author

**Syed Nazeer**

🔗 GitHub Profile: https://github.com/Syed-Nazeer-07

🔗 Repository: https://github.com/Syed-Nazeer-07/StockPortfolio

---

## 📜 License

This project is open-source and available under the MIT License.

---

⭐ If you found this project useful, consider starring the repository!
