import csv
import datetime

# Hardcoded dictionary of current stock prices (simulating real-time data for this exercise)
STOCK_PRICES = {
    "AAPL": 180.00,
    "TSLA": 250.00,
    "GOOGL": 140.00,
    "MSFT": 420.00,
    "AMZN": 170.00,
    "META": 480.00,
    "NVDA": 850.00
}

# The user's portfolio will be stored as a dictionary mapping Symbol -> Quantity
# e.g., {"AAPL": 10, "MSFT": 5}
portfolio = {}

def display_menu():
    """Displays the main menu options to the user."""
    print("\n" + "="*35)
    print("===== STOCK PORTFOLIO TRACKER =====")
    print("="*35)
    print("1. Add Stock")
    print("2. Remove Stock") # Added enhancement
    print("3. View Portfolio")
    print("4. Calculate Total Investment & Stats")
    print("5. Save Report to CSV")
    print("6. Exit")
    print("="*35)

def add_stock():
    """Prompts the user to add a stock to their portfolio with validation."""
    print("\n--- Add Stock ---")
    print("Available stocks:", ", ".join(STOCK_PRICES.keys()))
    
    symbol = input("Enter stock symbol (e.g., AAPL): ").strip().upper()
    
    # Validate stock symbol exists
    if symbol not in STOCK_PRICES:
        print(f"Error: Stock symbol '{symbol}' not found in available prices.")
        return

    # Validate quantity
    while True:
        try:
            quantity = int(input(f"Enter quantity of {symbol} owned: "))
            if quantity <= 0:
                print("Quantity must be a positive integer. Try again.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a whole number.")

    # Update portfolio (add to existing quantity if already owned)
    if symbol in portfolio:
        portfolio[symbol] += quantity
        print(f"Added {quantity} more shares of {symbol}. Total is now {portfolio[symbol]}.")
    else:
        portfolio[symbol] = quantity
        print(f"Successfully added {quantity} shares of {symbol} to portfolio.")

def remove_stock():
    """Allows user to remove or decrease stock quantity (Optional Enhancement)."""
    print("\n--- Remove Stock ---")
    if not portfolio:
        print("Your portfolio is currently empty.")
        return

    print("Current holdings:", ", ".join(portfolio.keys()))
    symbol = input("Enter stock symbol to remove: ").strip().upper()

    if symbol not in portfolio:
        print(f"Error: You do not own any shares of '{symbol}'.")
        return

    while True:
        try:
            print(f"You currently own {portfolio[symbol]} shares of {symbol}.")
            amount = input("Enter quantity to remove (or 'all' to remove completely): ").strip().lower()
            
            if amount == 'all':
                del portfolio[symbol]
                print(f"Completely removed {symbol} from portfolio.")
                break
            
            quantity_to_remove = int(amount)
            if quantity_to_remove <= 0:
                print("Quantity must be a positive integer.")
            elif quantity_to_remove >= portfolio[symbol]:
                 del portfolio[symbol]
                 print(f"Removed all shares of {symbol}.")
                 break
            else:
                portfolio[symbol] -= quantity_to_remove
                print(f"Removed {quantity_to_remove} shares of {symbol}. Remaining: {portfolio[symbol]}.")
                break
        except ValueError:
            print("Invalid input. Please enter a valid number or 'all'.")

def view_portfolio():
    """Displays the current portfolio in a clean tabular format."""
    print("\n--- Current Portfolio ---")
    if not portfolio:
        print("Your portfolio is currently empty.")
        return

    # Print table header
    print(f"{'Symbol':<10} | {'Quantity':<10} | {'Price/Share':<15} | {'Total Value':<15}")
    print("-" * 59)
    
    # Print table rows
    for symbol, quantity in portfolio.items():
        price = STOCK_PRICES[symbol]
        total_value = quantity * price
        print(f"{symbol:<10} | {quantity:<10} | ${price:<14.2f} | ${total_value:<14.2f}")

def calculate_total():
    """Calculates total portfolio value and displays enhanced statistics."""
    print("\n--- Portfolio Statistics ---")
    if not portfolio:
        print("Your portfolio is currently empty. No stats to show.")
        return

    total_portfolio_value = 0.0
    total_shares = 0
    highest_value_stock = None
    highest_value = 0.0

    # Calculate metrics
    for symbol, quantity in portfolio.items():
        value = quantity * STOCK_PRICES[symbol]
        total_portfolio_value += value
        total_shares += quantity
        
        # Track highest valued holding
        if value > highest_value:
            highest_value = value
            highest_value_stock = symbol

    # Display results
    print(f"Total Portfolio Value:    ${total_portfolio_value:,.2f}")
    print(f"Total Number of Shares:   {total_shares}")
    print(f"Highest Valued Holding:   {highest_value_stock} (${highest_value:,.2f})")
    print(f"Number of Unique Stocks:  {len(portfolio)}")
    return total_portfolio_value

def save_report():
    """Saves the current portfolio and stats to a CSV file."""
    print("\n--- Save Report ---")
    if not portfolio:
        print("Your portfolio is empty. Nothing to save.")
        return
    
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"portfolio_report_{timestamp}.csv"
    
    try:
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            
            # Write Header
            writer.writerow(['Report Generated:', datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")])
            writer.writerow([]) # Empty row for spacing
            writer.writerow(['Symbol', 'Quantity', 'Price Per Share', 'Total Value'])
            
            total_value = 0.0
            
            # Write data rows
            for symbol, quantity in portfolio.items():
                price = STOCK_PRICES[symbol]
                value = quantity * price
                total_value += value
                writer.writerow([symbol, quantity, f"${price:.2f}", f"${value:.2f}"])
            
            # Write footer with summary
            writer.writerow([])
            writer.writerow(['Total Portfolio Value', '', '', f"${total_value:.2f}"])
            
        print(f"Successfully saved portfolio report to '{filename}'.")
    except Exception as e:
         print(f"An error occurred while saving the file: {e}")

def main():
    """Main program loop."""
    print("Welcome to the Stock Portfolio Tracker!")
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ").strip()
        
        if choice == '1':
            add_stock()
        elif choice == '2':
            remove_stock()
        elif choice == '3':
            view_portfolio()
        elif choice == '4':
            calculate_total()
        elif choice == '5':
            save_report()
        elif choice == '6':
            print("\nExiting Stock Portfolio Tracker. Goodbye!")
            break
        else:
            print("\nInvalid choice. Please enter a number between 1 and 6.")

# Entry point of the script
if __name__ == "__main__":
    main()
