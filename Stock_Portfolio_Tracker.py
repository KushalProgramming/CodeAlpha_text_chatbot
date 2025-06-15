import yfinance as yf

portfolio = {}

def add_stock():
    symbol = input("Enter stock symbol: ").strip().upper()
    try:
        shares = int(input("Enter number of shares: "))
        purchase_price = float(input("Enter purchase price per share: "))
        if symbol in portfolio:
            portfolio[symbol]["shares"] += shares
        else:
            portfolio[symbol] = {"shares": shares, "purchase_price": purchase_price}
        print(f"✅ Added {shares} shares of {symbol} at ₹{purchase_price}")
    except ValueError:
        print("❌ Invalid input. Try again.")

def remove_stock():
    symbol = input("Enter stock symbol to remove: ").strip().upper()
    if symbol in portfolio:
        del portfolio[symbol]
        print(f"✅ Removed {symbol} from portfolio")
    else:
        print("❌ Stock not found in portfolio")

def get_live_price(symbol):
    try:
        stock = yf.Ticker(symbol)
        price = stock.history(period="1d")["Close"].iloc[-1]
        return round(price, 2)
    except:
        return None

def view_portfolio():
    if not portfolio:
        print("🪙 Your portfolio is empty.")
        return

    print("\n--- Portfolio Overview ---")
    total_value = 0
    total_investment = 0

    for symbol, data in portfolio.items():
        shares = data["shares"]
        purchase_price = data["purchase_price"]
        live_price = get_live_price(symbol)

        if live_price is None:
            print(f"{symbol} - ⚠️ Could not fetch live data")
            continue

        current_value = shares * live_price
        investment = shares * purchase_price
        profit_loss = current_value - investment

        total_value += current_value
        total_investment += investment

        print(f"{symbol} | Shares: {shares}")
        print(f"  Buy @ ₹{purchase_price} | Live ₹{live_price} | Value: ₹{current_value:.2f}")
        print(f"  P/L: {'+' if profit_loss >= 0 else ''}{profit_loss:.2f}\n")

    print(f"Total Investment: ₹{total_investment:.2f}")
    print(f"Current Value: ₹{total_value:.2f}")
    print(f"Net P/L: {'+' if total_value - total_investment >= 0 else ''}{total_value - total_investment:.2f}")

def menu():
    while True:
        print("\n====== Stock Portfolio Tracker ======")
        print("1. Add Stock")
        print("2. Remove Stock")
        print("3. View Portfolio")
        print("4. Exit")

        choice = input("Choose an option (1-4): ").strip()

        if choice == '1':
            add_stock()
        elif choice == '2':
            remove_stock()
        elif choice == '3':
            view_portfolio()
        elif choice == '4':
            print("👋 Exiting Portfolio Tracker.")
            break
        else:
            print("❌ Invalid option.")

if __name__ == "__main__":
    menu()