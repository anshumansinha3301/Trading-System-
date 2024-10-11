# Data
stock_market = {
    "AAPL": 175.23,
    "GOOGL": 2835.46,
    "MSFT": 310.75,
    "TSLA": 735.46,
    "AMZN": 3472.75
}

portfolio = {}
transaction_history = []
account_balance = 10000.0

def show_stock_market():
    print("\nStock Market:")
    for index, (symbol, price) in enumerate(stock_market.items(), start=1):
        print(f"{index}. {symbol} - ${price:.2f}")

def view_stock_details():
    show_stock_market()
    choice = input("Enter the stock symbol for details: ").upper()
    if choice in stock_market:
        print(f"\nStock: {choice}\nCurrent Price: ${stock_market[choice]:.2f}")
    else:
        print("Invalid stock symbol.")

def buy_stock():
    global account_balance
    show_stock_market()
    symbol = input("Enter the stock symbol to buy: ").upper()
    if symbol in stock_market:
        try:
            quantity = int(input(f"Enter quantity to buy: "))
        except ValueError:
            print("Invalid quantity entered.")
            return
        total_cost = stock_market[symbol] * quantity
        if total_cost > account_balance:
            print("Insufficient balance to complete the purchase.")
        else:
            account_balance -= total_cost
            portfolio[symbol] = portfolio.get(symbol, 0) + quantity
            transaction_history.append(f"Bought {quantity} of {symbol} at ${stock_market[symbol]:.2f}")
            print(f"Bought {quantity} of {symbol} for ${total_cost:.2f}. New balance: ${account_balance:.2f}")
    else:
        print("Invalid stock symbol.")

def sell_stock():
    global account_balance
    if not portfolio:
        print("You have no stocks to sell.")
        return
    symbol = input("Enter the stock symbol to sell: ").upper()
    if symbol in portfolio:
        try:
            quantity = int(input(f"Enter quantity to sell: "))
        except ValueError:
            print("Invalid quantity entered.")
            return
        if quantity > portfolio[symbol]:
            print("You don't have enough quantity to sell.")
        else:
            portfolio[symbol] -= quantity
            if portfolio[symbol] == 0:
                del portfolio[symbol]
            total_value = stock_market[symbol] * quantity
            account_balance += total_value
            transaction_history.append(f"Sold {quantity} of {symbol} at ${stock_market[symbol]:.2f}")
            print(f"Sold {quantity} of {symbol} for ${total_value:.2f}. New balance: ${account_balance:.2f}")
    else:
        print("Stock not found in your portfolio.")

def view_portfolio():
    if not portfolio:
        print("Your portfolio is empty.")
    else:
        print("\nYour Portfolio:")
        total_value = 0
        for symbol, quantity in portfolio.items():
            current_value = stock_market[symbol] * quantity
            total_value += current_value
            print(f"{symbol} - Quantity: {quantity}, Current Value: ${current_value:.2f}")
        print(f"Total Portfolio Value: ${total_value:.2f}")

def check_balance():
    print(f"\nAccount Balance: ${account_balance:.2f}")

def view_transaction_history():
    if not transaction_history:
        print("No transactions made yet.")
    else:
        print("\nTransaction History:")
        for transaction in transaction_history:
            print(transaction)

def main():
    while True:
        print("\nAdvanced Trading System:")
        print("1. Show Stock Market")
        print("2. View Stock Details")
        print("3. Buy Stock")
        print("4. Sell Stock")
        print("5. View Portfolio")
        print("6. Check Account Balance")
        print("7. View Transaction History")
        print("8. Exit")
        
        choice = input("Enter your choice: ")
        if choice == "1":
            show_stock_market()
        elif choice == "2":
            view_stock_details()
        elif choice == "3":
            buy_stock()
        elif choice == "4":
            sell_stock()
        elif choice == "5":
            view_portfolio()
        elif choice == "6":
            check_balance()
        elif choice == "7":
            view_transaction_history()
        elif choice == "8":
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
