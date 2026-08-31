stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 150,
    "MSFT": 420,
    "AMZN": 180
}
portfolio={}
while True:
    stock_name = input("Enter stock name (or 'done' to finish): ").upper()
    if stock_name == "DONE":
        break
    if stock_name in stock_prices:
        quantity = int(input("Enter quantity: "))
        portfolio[stock_name] = quantity
    else:
        print("Stock not available")
total_value = 0
for stock_name, quantity in portfolio.items():
    value = stock_prices[stock_name] * quantity
    print(stock_name, "value:", value)
    total_value += value
print("Total Portfolio Value:", total_value)        