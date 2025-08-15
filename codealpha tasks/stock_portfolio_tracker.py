def stock_portfolio_tracker():
    # Hardcoded stock prices
    stock_prices = {
        "AAPL": 180,
        "TSLA": 250,
        "GOOGL": 130,
        "AMZN": 140,
        "MSFT": 300
    }
    
    print("📊 Stock Portfolio Tracker")
    print("Available stocks and prices:")
    for stock, price in stock_prices.items():
        print(f"{stock}: ${price}")
    
    portfolio = {}
    total_investment = 0

    while True:
        stock_name = input("\nEnter stock symbol (or 'done' to finish): ").upper()
        if stock_name == "DONE":
            break
        if stock_name not in stock_prices:
            print("⚠ Stock not found. Please choose from the available list.")
            continue

        try:
            quantity = int(input(f"Enter quantity for {stock_name}: "))
            if quantity <= 0:
                print("⚠ Quantity must be positive.")
                continue
        except ValueError:
            print("⚠ Please enter a valid integer for quantity.")
            continue

        portfolio[stock_name] = portfolio.get(stock_name, 0) + quantity
        investment = stock_prices[stock_name] * quantity
        total_investment += investment
        print(f"Added {quantity} shares of {stock_name} worth ${investment}.")

    print("\n📈 Portfolio Summary:")
    for stock, qty in portfolio.items():
        print(f"{stock}: {qty} shares, Value: ${stock_prices[stock] * qty}")

    print(f"💰 Total Investment Value: ${total_investment}")

if __name__ == "__main__":
    stock_portfolio_tracker()
