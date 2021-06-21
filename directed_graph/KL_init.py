from .netlist_node import Netlist_Node
from .netlist_graph import Netlist_Graph
from .netlist_edges import Netlist_Edges

from .algorithms.KL import KL

def main():
    # stores graph nodes in an array
    # use add_node(node_object) 
    graph = Netlist_Graph()

    # create all the nodes for the graph
    # in this case, use practice problem 1 from the textbook
    node_a = Netlist_Node("a", 1)
    node_b = Netlist_Node("b", 2)
    node_c = Netlist_Node("c", 3)
    node_d = Netlist_Node("d", 4)
    node_e = Netlist_Node("e", 5)
    node_f = Netlist_Node("f", 6)
    node_g = Netlist_Node("g", 7)
    node_h = Netlist_Node("h", 8)


    # param 1 is the node target for the edge, param 2 is the edge weight
    # for the KL algorithm, nodes that are connected each have 2 edges.
    # for example, node A has node C as a target, and node C has node A as a target
    edge_object_ae = Netlist_Edges(node_e, 0.5)
    edge_object_ac = Netlist_Edges(node_c, 0.5)

    edge_object_bc = Netlist_Edges(node_c, 0.5)
    edge_object_bd = Netlist_Edges(node_d, 0.5)

    edge_object_ce = Netlist_Edges(node_e, 1)
    edge_object_cf = Netlist_Edges(node_f, 0.5)
    edge_object_cd = Netlist_Edges(node_d, 0.5)
    edge_object_ca = Netlist_Edges(node_a, 0.5)
    edge_object_cb = Netlist_Edges(node_b, 0.5)

    edge_object_df = Netlist_Edges(node_f, 1)
    edge_object_dc = Netlist_Edges(node_c, 0.5)
    edge_object_db = Netlist_Edges(node_b, 0.5)

    edge_object_eg = Netlist_Edges(node_g, 1)
    edge_object_ef = Netlist_Edges(node_f, 0.5)
    edge_object_ec = Netlist_Edges(node_c, 1)
    edge_object_ea = Netlist_Edges(node_a, 0.5)

    edge_object_fh = Netlist_Edges(node_h, 0.5)
    edge_object_fg = Netlist_Edges(node_g, 0.5)
    edge_object_fe = Netlist_Edges(node_e, 0.5)
    edge_object_fc = Netlist_Edges(node_c, 0.5)
    edge_object_fd = Netlist_Edges(node_d, 1)

    edge_object_gh = Netlist_Edges(node_h, 0.5)
    edge_object_gf = Netlist_Edges(node_f, 0.5)
    edge_object_ge = Netlist_Edges(node_e, 1)

    edge_object_hg = Netlist_Edges(node_g, 0.5)
    edge_object_hf = Netlist_Edges(node_f, 0.5)

    # param 1 is the source node, param 2 is the edges array that stores info regarding connected nodes and edge weights
    graph.add_node(node_a, [edge_object_ac, edge_object_ae])
    graph.add_node(node_b, [edge_object_bc, edge_object_bd])
    graph.add_node(node_c, [edge_object_cd, edge_object_ce, edge_object_cf, edge_object_ca, edge_object_cb])
    graph.add_node(node_d, [edge_object_df, edge_object_dc, edge_object_db])
    graph.add_node(node_e, [edge_object_ef, edge_object_eg, edge_object_ec, edge_object_ea])
    graph.add_node(node_f, [edge_object_fg, edge_object_fh, edge_object_fe, edge_object_fc, edge_object_fd])
    graph.add_node(node_g, [edge_object_gh, edge_object_gf, edge_object_ge])
    graph.add_node(node_h, [edge_object_hg, edge_object_hf])

    # creates undirected graph to visualize the initial problem (similar to figure 2.1b)
    #graph.create_gv_file()

    # run KL algorithm
    # to do: look at edge cases and what happens if there is an odd number of nodes in the graph
    partition = KL(graph, [node_a, node_b, node_d, node_e])
    KL_result = partition.swap_pairs()
    # result is tuple containing arrays
    # the arrays are arranged such that index 0 is the topmost node (based on the examples)
    # the 0th tuple index contains the left partition nodes
    # the 1st tuple index contains the right partition nodes
    
    # returns directory of results
    return KL_result

if __name__ == "__main__":
    main()