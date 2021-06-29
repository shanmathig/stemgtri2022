from netlist_node import Netlist_Node
from netlist_graph import Netlist_Graph
from netlist_edges import Netlist_Edges

from algorithms.Mincut import Mincut

def main():
    graph = Netlist_Graph()

    # create all the nodes for the graph
    # in this case, use practice problem 1 from the Mincut textbook chapter
    node_a = Netlist_Node("a", 1)
    node_b = Netlist_Node("b", 2)
    node_c = Netlist_Node("c", 3)
    node_d = Netlist_Node("d", 4)
    node_e = Netlist_Node("e", 5)
    node_f = Netlist_Node("f", 6)
    node_g = Netlist_Node("g", 7)
    node_h = Netlist_Node("h", 8)
    node_i = Netlist_Node("i", 9)
    node_j = Netlist_Node("j", 10)
    node_k = Netlist_Node("k", 11)
    node_l = Netlist_Node("l", 12)
    node_m = Netlist_Node("m", 13)
    node_n = Netlist_Node("n", 14)
    node_o = Netlist_Node("o", 15)
    node_p = Netlist_Node("p", 16)

    # param 1 is the node target for the edge, param 2 is the edge weight
    # for the KL algorithm, nodes that are connected each have 2 edges.
    # for example, node A has node C as a target, and node C has node A as a target
    edge_object_ae = Netlist_Edges(node_e, 0.5)
    edge_object_ai = Netlist_Edges(node_i, 0.5)

    edge_object_bg = Netlist_Edges(node_g, 0.5)
    edge_object_bf = Netlist_Edges(node_f, 0.5)

    edge_object_cg = Netlist_Edges(node_g, 0.5)
    edge_object_cl = Netlist_Edges(node_l, 0.5)

    edge_object_dl = Netlist_Edges(node_l, 0.5)
    edge_object_dh = Netlist_Edges(node_h, 0.5)

    edge_object_ea = Netlist_Edges(node_a, 0.5)
    edge_object_ei = Netlist_Edges(node_i, 1)
    edge_object_ef = Netlist_Edges(node_f, 1)
    edge_object_ej = Netlist_Edges(node_j, 0.5)

    edge_object_fg = Netlist_Edges(node_g, 0.5)
    edge_object_fb = Netlist_Edges(node_b, 0.5)
    edge_object_fe = Netlist_Edges(node_e, 1)
    edge_object_fj = Netlist_Edges(node_j, 1)

    edge_object_gf = Netlist_Edges(node_f, 0.5)
    edge_object_gk = Netlist_Edges(node_k, 0.5)
    edge_object_gj = Netlist_Edges(node_j, 0.5)
    edge_object_gb = Netlist_Edges(node_b, 0.5)
    edge_object_gl = Netlist_Edges(node_l, 0.5)
    edge_object_gc = Netlist_Edges(node_c, 0.5)

    edge_object_hp = Netlist_Edges(node_p, 1)
    edge_object_hl = Netlist_Edges(node_l, 0.5)
    edge_object_hd = Netlist_Edges(node_d, 0.5)

    edge_object_ie = Netlist_Edges(node_e, 1)
    edge_object_ia = Netlist_Edges(node_a, 0.5)
    edge_object_im = Netlist_Edges(node_m, 0.5)
    edge_object_ij = Netlist_Edges(node_j, 0.5)

    edge_object_je = Netlist_Edges(node_e, 0.5)
    edge_object_jg = Netlist_Edges(node_g, 0.5)
    edge_object_jf = Netlist_Edges(node_f, 1)
    edge_object_jk = Netlist_Edges(node_k, 0.5)
    edge_object_jm = Netlist_Edges(node_m, 0.5)
    edge_object_ji = Netlist_Edges(node_i, 0.5)
    edge_object_jn = Netlist_Edges(node_n, 0.5)

    edge_object_kg = Netlist_Edges(node_g, 0.5)
    edge_object_ko = Netlist_Edges(node_o, 0.5)
    edge_object_kn = Netlist_Edges(node_n, 0.5)
    edge_object_kj = Netlist_Edges(node_j, 0.5)

    edge_object_lc = Netlist_Edges(node_c, 0.5)
    edge_object_ld = Netlist_Edges(node_d, 0.5)
    edge_object_lo = Netlist_Edges(node_o, 0.5)
    edge_object_lp = Netlist_Edges(node_p, 0.5)
    edge_object_lh = Netlist_Edges(node_h, 0.5)
    edge_object_lg = Netlist_Edges(node_g, 0.5)
    edge_object_ld = Netlist_Edges(node_d, 0.5)

    edge_object_mn = Netlist_Edges(node_n, 0.5)
    edge_object_mi = Netlist_Edges(node_i, 1)
    edge_object_mj = Netlist_Edges(node_j, 0.5)

    edge_object_nm = Netlist_Edges(node_m, 0.5)
    edge_object_no = Netlist_Edges(node_o, 0.5)
    edge_object_nj = Netlist_Edges(node_j, 0.5)
    edge_object_nk = Netlist_Edges(node_k, 0.5)

    edge_object_op = Netlist_Edges(node_p, 0.5)
    edge_object_ol = Netlist_Edges(node_l, 0.5)
    edge_object_ok = Netlist_Edges(node_k, 0.5)
    edge_object_on = Netlist_Edges(node_n, 0.5)

    edge_object_ph = Netlist_Edges(node_h, 1)
    edge_object_pl = Netlist_Edges(node_l, 0.5)
    edge_object_po = Netlist_Edges(node_o, 0.5)
    
    # param 1 is the source node, param 2 is the edges array that stores info regarding connected nodes and edge weights
    graph.add_node(node_a, [edge_object_ae, edge_object_ai])
    graph.add_node(node_b, [edge_object_bg, edge_object_bf])
    graph.add_node(node_c, [edge_object_cg, edge_object_cl])
    graph.add_node(node_d, [edge_object_dh, edge_object_dl])
    graph.add_node(node_e, [edge_object_ea, edge_object_ef, edge_object_ei, edge_object_ej])
    graph.add_node(node_f, [edge_object_fb, edge_object_fe, edge_object_fg, edge_object_fj])
    graph.add_node(node_g, [edge_object_gl, edge_object_gb, edge_object_gc, edge_object_gf, edge_object_gj, edge_object_gk])
    graph.add_node(node_h, [edge_object_hd, edge_object_hl, edge_object_hp])
    graph.add_node(node_i, [edge_object_ia, edge_object_ie, edge_object_ij, edge_object_im])
    graph.add_node(node_j, [edge_object_je, edge_object_jf, edge_object_jg, edge_object_ji, edge_object_jk, edge_object_jm, edge_object_jn])
    graph.add_node(node_k, [edge_object_kg, edge_object_kj, edge_object_kn, edge_object_ko])
    graph.add_node(node_l, [edge_object_lc, edge_object_ld, edge_object_lg, edge_object_lh, edge_object_lo, edge_object_lp])
    graph.add_node(node_m, [edge_object_mi, edge_object_mj, edge_object_mn])
    graph.add_node(node_n, [edge_object_nj, edge_object_nk, edge_object_nm, edge_object_no])
    graph.add_node(node_o, [edge_object_ok, edge_object_ol, edge_object_on, edge_object_op])
    graph.add_node(node_p, [edge_object_ph, edge_object_pl, edge_object_po])

    # stores cliques in the graph
    graph.add_to_clique_netlist([node_e, node_f])
    graph.add_to_clique_netlist([node_a, node_e, node_i])
    graph.add_to_clique_netlist([node_b, node_f, node_g])
    graph.add_to_clique_netlist([node_c, node_g, node_l])
    graph.add_to_clique_netlist([node_d, node_l, node_h])
    graph.add_to_clique_netlist([node_e, node_i, node_j])
    graph.add_to_clique_netlist([node_f, node_j])
    graph.add_to_clique_netlist([node_g, node_j, node_k])
    graph.add_to_clique_netlist([node_l, node_o, node_p])
    graph.add_to_clique_netlist([node_h, node_p])
    graph.add_to_clique_netlist([node_i, node_m])
    graph.add_to_clique_netlist([node_j, node_m, node_n])
    graph.add_to_clique_netlist([node_k, node_n, node_o])

    #print(graph.get_clique_based_netlist())

    # creates undirected graph to visualize the initial problem
    #graph.create_gv_file()

    # testing the half perimeter calculations
    """node_n.set_position(0, 0)    
    node_b.set_position(1, 0)
    node_c.set_position(2, 0)
    node_o.set_position(3, 0)
    node_j.set_position(0, 1)
    node_f.set_position(1, 1)
    node_g.set_position(2, 1)
    node_k.set_position(3, 1)
    node_m.set_position(0, 2)
    node_e.set_position(1, 2)
    node_l.set_position(2, 2)
    node_p.set_position(3, 2)
    node_i.set_position(0, 3)
    node_a.set_position(1, 3)
    node_d.set_position(2, 3)
    node_h.set_position(3, 3)"""

    # run Mincut algorithm
    placement = Mincut(graph, [node_n, node_f, node_j, node_b, node_m, node_e, node_i, node_a], debug=True)
    mincut_result = placement.quadrature()
    #print(mincut_result)
    """
    this result represents the following mincut grid placement
    [
        [i, j, k, g],
        [m, n, o, c],
        [a, e, d, h],
        [b, f, l, p]
    ]
    """
    # calculate the wirelength
    wirelength = placement.calc_half_perimeter()
    print(wirelength)

    # currently returns nothing
    #return mincut_result

if __name__ == "__main__":
    main()