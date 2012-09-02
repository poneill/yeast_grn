import networkx as nx

def get_data():
    with open("yeast.sig") as f:
        lines = [line.strip().split(" ") for line in f.readlines()]
    data = [(line[0],line[5]) for line in lines]
    return data

def make_graph(data):
    g = nx.DiGraph()
    for d in data:
        g.add_edge(*d)
    return g
    
def find_longest_path(g):
    paths = (nx.all_pairs_shortest_path_length(g))
    longest_path = max([paths[start_node][end_node]
                        for start_node in paths
                        for end_node in paths[start_node]])
    return longest_path

def main():
    g = make_graph(get_data())
    longest_path = find_longest_path(g) 
    return longest_path #== 5
