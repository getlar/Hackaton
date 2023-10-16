import pandas as pd

def djikstra_modified(df_nodes, df_edges, start_node):
    road_trip = pd.DataFrame(columns=['dest', 'val'])

    # Tartunk egy listát a még nem vizsgált csomópontokról, és egy halmazt a már vizsgáltakról
    frontier = [(start_node, 24, 0)]
    visited = set()

    while frontier:
        frontier.sort(key=lambda x: x[1])
        
        current_node, cumulative_hours, accumulated_value = frontier.pop(0)

        if current_node in visited:
            continue

        visited.add(current_node)
        new_row = pd.DataFrame({'dest': [current_node], 'val': [accumulated_value]})
        road_trip = pd.concat([road_trip, new_row], ignore_index=True)

        for _, edge in df_edges[df_edges['start'] == current_node].iterrows():
            dest = edge['dest']
            weight = edge['weight']
            node_weight = df_nodes.loc[df_nodes['node'] == dest, 'value'].iloc[0]

            if dest not in visited and cumulative_hours >= weight:
                new_cumulative_hours = cumulative_hours - weight
                if new_cumulative_hours <= 24:
                    frontier.append((dest, new_cumulative_hours, accumulated_value + node_weight))

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
    road_trip = djikstra_modified(df_beers, df_bidirectional, "FL")
    
    # Output formátum
    cumulative_val = road_trip['val'].sum()
    road_list = road_trip['dest'].tolist()
    return f'[{cumulative_val}:{",".join(road_list)}]'

    
if __name__ == "__main__":
    print(main())