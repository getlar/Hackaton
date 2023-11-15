import pandas as pd

roads = pd.read_excel('oitm_tour.xlsx', sheet_name='TOUR_ROADS', header=None)
beers = pd.read_excel('oitm_tour.xlsx', sheet_name='TOUR_BEERS', header = None)

terkep = dict()

for r in roads.values:
    city1 = r[0]
    city2 = r[1]
    dist = r[2]

    if city1 not in terkep.keys():
        terkep[city1] = {'szomszedok':set(),'sörök':0}
    if city2 not in terkep.keys():
        terkep[city2] = {'szomszedok':set(),'sörök':0}
    terkep[city1]['szomszedok'].add((city2, dist))
    terkep[city2]['szomszedok'].add((city1, dist))

most = 'FL'
utvonalak = [([most], 0, 0)]

for b in beers.values:
    city = b[0]
    sor = b[1]
    terkep[city]['sörök'] = sor


# KERESÉS:
for utvonal in utvonalak:
    ido = utvonal[2]
    eddig = utvonal[1]
    most = utvonal[0][-1]
    if most not in utvonal[0][:-1]:
        megivott = eddig + terkep[most]['sörök']
    elif utvonal[0][-2:] == utvonal[0][-4:-2]:
        continue
    else:
        megivott = eddig
    if ido < 24:
        for szomszed in terkep[most]['szomszedok']:
            uj =  (utvonal[0]+[szomszed[0]],megivott, ido+szomszed[1])
            utvonalak.append(uj)

dt = pd.DataFrame(utvonalak)
dt.columns = ['utvonal', 'sörök', 'idő']
dt = dt[dt['idő'] <= 24].sort_values('sörök', ascending=False)
print(dt.head())