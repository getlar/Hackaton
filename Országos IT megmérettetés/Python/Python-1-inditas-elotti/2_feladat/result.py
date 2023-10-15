import pandas as pd

def calc_road_trip(df_nodes, df_edges, start_node):

    """
    A függvény kiszámolja azt a legrövidebb utat, ami a legtöbb sörhöz vezet.

    df_nodes: csomópontokat tartalmazó DataFrame
    df_edges: bidirekcionális éleket tartalmazó DataFrame
    start_node: kezdő node
    """
    
    road_trip = pd.DataFrame(columns=['dest', 'val'])
    frontier = set([start_node])
    cumulative_hours = 24

    # Amíg van fennmaradt idő, addig keresünk egy újabb kocsmát
    while cumulative_hours > 0:
        min_edge = None
        for node in frontier.copy():
            edges = df_edges[df_edges['start'] == node]
            for _, values in edges.iterrows():
                dest = values["dest"]
                weight = values["weight"]
                node_weight = df_nodes.loc[df_nodes['node'] == dest, 'value'].iloc[0]
                
                # Nem feltétlen jó heurisztika, hiszen lokális optimumhoz vezet
                # Nem veszi figyelembe, ha a legjobb útba már nem férünk bele
                # Akkor válassza a még elfogadható legjobb utat
                if min_edge is None or (weight < min_edge[2] and node_weight > min_edge[3]):
                    min_edge = (node, dest, weight, node_weight)
            
            # Ha a legkisebb él súlya nagyobb, mint a fennmaradt idő, akkor elalszunk
            if min_edge[2] > cumulative_hours:
                return road_trip
            
            # Ha van minimum él, akkor hozzáadjuk a road_trip-hez
            if min_edge is not None:
                road_trip_node = df_nodes[df_nodes['node'] == min_edge[1]]
                road_trip = pd.concat([road_trip, pd.DataFrame({'dest': [min_edge[1]], 'val': [road_trip_node['value'].iloc[0]]})])
                frontier.add(min_edge[1])

                # Kivonjuk a súlyt a fennmaradt időből
                cumulative_hours -= min_edge[2]
            
            frontier.remove(node)
    return road_trip
    

def main():
    xls = pd.ExcelFile("oitm_tour.xlsx")
    
    df_beers = pd.read_excel(xls, "TOUR_BEERS", header=None)
    df_beers.columns = ['node', 'value']
    
    df_roads = pd.read_excel(xls, "TOUR_ROADS", header=None)
    df_roads.columns = ['start', 'dest', 'weight']

    # Bidirekcionális gráf készítése
    df_swapped = df_roads.copy()
    df_swapped['start'], df_swapped['dest'] = df_roads['dest'], df_roads['start']
    df_swapped = df_swapped.iloc[3:]

    # Összefűzzük a két gráfot
    df_bidirectional = pd.concat([df_roads, df_swapped])

    # A függvény kiszámolja a legrövidebb utat, ami a legtöbb sörhöz vezet
    road_trip = calc_road_trip(df_beers, df_bidirectional, "FL")
    
    # Output formátum
    cumulative_val = road_trip['val'].sum()
    road_list = ["FL"] + road_trip['dest'].tolist()
    return f'[{cumulative_val}:{",".join(road_list)}]'

    
if __name__ == "__main__":
    print(main())