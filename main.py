from files import read_csv_file, get_item_by_node
from graf_drawing import do_it, build_edges, draw_graph
import networkx as nx
# do_it()

def monta_grafo(no_inicial,edges, itens_saida, mapa):
    itens_entrada = get_item_by_node(no_inicial, entrada, 0)

    # captura as condições dos nós de entrada
    for v in itens_entrada:
        cond_inicial = v[1]
        itens_saida = get_item_by_node(cond_inicial, saida, 1)
        edges = build_edges(no_inicial, itens_saida)
        mapa.add_edges_from(edges)
        edges = []
    for no_inicial in itens_saida:
        monta_grafo(no_inicial[0], edges, itens_saida, mapa)

itens_entrada = []
itens_saida = []
edges = []
entrada = read_csv_file('in_cond.csv')
saida = read_csv_file('out_cond.csv')
no_inicial = input('Digite o no inicial: ').upper()
mapa = nx.Graph()
monta_grafo(no_inicial, edges, itens_saida, mapa)

# do_it()


draw_graph(mapa, node_size=4000, font_size=12)

print()