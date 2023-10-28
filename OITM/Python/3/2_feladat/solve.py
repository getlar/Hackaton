import pulp
import pandas as pd

# Load data from the Excel sheets
prices_df = pd.read_excel('ingredients.xlsx', sheet_name='PRICES')
quantities_df = pd.read_excel('ingredients.xlsx', sheet_name='QUANTITIES')

merged_df = pd.merge(prices_df, quantities_df, on='ingredient')

merged_df['new_price'] = merged_df['price'] * merged_df['quantity']

print(merged_df)

merged_df.drop(['price', 'quantity'], axis=1, inplace=True)

print(merged_df)

merged_df.rename(columns={'new_price': 'price'}, inplace=True)

print(merged_df)

sorted_df = merged_df.sort_values(by='store')

print(sorted_df)

total_prices = sorted_df.groupby('store')['price'].sum().reset_index()

#best_store = total_prices.loc[total_prices['price'].idxmin()]

#print(best_store)

total_prices = total_prices.sort_values(by='price', ascending=False)

print(total_prices)
from itertools import combinations

store_combinations = list(combinations(total_prices['store'], 2))

# Calculate the cost for each combination
best_stores = None
min_cost = float('inf')

for combination in store_combinations:
    cost = total_prices.loc[total_prices['store'].isin(combination)]['price'].sum()
    if cost < min_cost:
        min_cost = cost
        best_stores = combination

print(best_stores)
print(min_cost)

print(1983*2 + 62 * 10 + 92 + 87 * 100 + 155*48)
print(1982*2 + 62 * 10 + 85 + 87 * 100 + 153*48)

print(2010*2 + 81 * 10 + 86 + 87 * 100 + 134*48)

print(2010*2 + 79 * 10 + 92 + 87 * 100 + 132*48)

print(2000*2 + 70 * 10 + 92 + 87 * 100 + 150*48)
print(1983*2 + 62 * 10 + 86 + 90 * 100 + 134*48)
print(1982*2 + 62 * 10 + 85 + 92 * 100 + 134*48)