import numpy as np
import pandas as pd
df = pd.read_excel('stations.xlsx', sheet_name='STATIONS',header=None)
data = np.array(df[0])

tank = 0
koltseg = 0
home_index = len(data)
for i in range(len(data)):
    print('#########')

    current_price = data[i]
    print(f'STATION {i}, benzin ára: {current_price}')
    
    consider = list(range(i+1,np.min([i+5, home_index])))
    print(f'Következő állomások: {consider}')
    
    next_prices = data[consider]
    print(f'Következő állomások árai: {next_prices}')
    
    if (next_prices < current_price).any():
        # van a közelben olcsóbb benzinkút, elég, ha odáig van benzinünk
        tavolsag = np.where(next_prices < current_price)[0][0] + 1
    else:
        # nincsen a közelben olcsóbb benzinkút, ezért tele kell tankolni - vagy addig, hogy hazaérjünk
        tavolsag = np.min([i + 4, home_index]) - i

    print(f'Tank érkezéskor: {tank}')
    benzin = tavolsag * 10
    if benzin > tank:
        toltes = benzin-tank
        tank += toltes
        koltseg += toltes*current_price
    else:
        toltes = 0
    print(f'Töltés: {toltes}')
    print(f'Tank tavozaskor: {tank}')

    tank -= 10

print(koltseg)