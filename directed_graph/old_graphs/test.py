"""
This is a file for testing the class methods.
"""
from node import Node
from edges import Edges
from graph import Graph

if __name__ == '__main__':
    
    node_object = Node("OR", 6)
    other_node_object = Node("AND", 5)
    print(node_object.get_gate_type())

    edge_object = Edges(node_object, other_node_object, 5)
    print(str(edge_object))

    graph = Graph()
    graph.add_edge(edge_object)
    graph.add_node(other_node_object)
    graph.add_node(node_object)
    graph.create_gv_file()
    print(graph)