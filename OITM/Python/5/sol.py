
def append_to(element, to=[]):
    to.append(element)
    return to

lista_1 = append_to("soproni")
lista_1 = append_to("borsodi", lista_1)

lista_2 = append_to("heineken")
print(lista_2)
lista_2 = append_to("staropramen", lista_2)

lista_3 = append_to("aranyaszok", lista_1)

print(lista_1)
print(lista_2)
print(lista_3)

import pandas as pd

data = {
    'ID': [1, 5, 6, 4, 2],
    'A': ['import', 'import', 'hazai', 'hazai', 'import'],
    'B': ['Heineken', 'Hoegaarden', 'Soproni', 'Borsodi', 'Budweiser'],
    'C': [300, 400, 300, 400, 500]
}

df = pd.DataFrame(data)

print(df.loc[6:4,'B':'B'])
print('----------------')
print(df.loc[2:4,'B':'C'])
print('----------------')
print(df.loc[6:4,'B':'C'])
print('----------------')
print(df.loc[df['A'] == 'hazai', 'B':'B'])
print('----------------')
print(df.iloc[2:4,1:2])
print('----------------')
print(df.iloc[2:3,1:2])
print('----------------')

df = df.iloc[2:4,1:2]
print(df.head)