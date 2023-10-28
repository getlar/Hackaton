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

print('-------------------')

unique_stores = sorted_df['store'].unique()

best_price = {}


for i in range(len(unique_stores)):
    for j in range(i+1, len(unique_stores)):
        store1 = unique_stores[i]
        store2 = unique_stores[j]

        store1_df = sorted_df.loc[sorted_df['store'] == store1]
        store2_df = sorted_df.loc[sorted_df['store'] == store2]

        merged_df = pd.merge(store1_df, store2_df, on='ingredient')
        tmp_price = 0
        for index, row in merged_df.iterrows():
            if row['price_x'] > row['price_y']:
                tmp_price += row['price_y']
            else:
                tmp_price += row['price_x']

        best_price[(store1, store2)] = tmp_price

for key, value in sorted(best_price.items(), key=lambda item: item[1], reverse=True):
    print(key, value)