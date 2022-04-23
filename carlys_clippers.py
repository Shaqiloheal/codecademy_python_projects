hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]
prices = [30, 25, 40, 20, 20, 35, 50, 35]
last_week = [2, 3, 5, 8, 4, 4, 6, 2]
new_prices = [price - 5 for price in prices]
cuts_under_30 = [hairstyles[i] for i in range(len(hairstyles)) if prices[i] < 30]

total_price = 0
total_revenue = 0

for price in prices:
  total_price += price
  average_price = total_price / len(prices)
print("Average Haircut Price:", average_price)
print(new_prices)

for i in range(len(hairstyles)):
  total_revenue += prices[i] * last_week[i]
  daily_average_revenue = total_revenue / 7
print("Total Revenue:", total_revenue)
print("Average Daily Revenue:", daily_average_revenue)
print(cuts_under_30)