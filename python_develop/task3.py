def maxProfit(prices):
    min_price = float('inf')
    max_profit = 0
    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > max_profit:
            max_profit = price - min_price
    return max_profit

while True:
    print("Введите цены через пробел или выход для выхода:")
    input_str = input()
    if input_str == 'выход':
        break
    
    prices = list(map(int, input_str.split()))
    print(f"Максимальная прибыль: {maxProfit(prices)}")
    print()