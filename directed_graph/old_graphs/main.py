from node import Node
from edges import Edges
from graph import Graph

"""
sample 1 (in yosys):

module AND3 #() (
	input wire a,
	input wire b,
	input wire c,
	output wire o
	);

	assign o = a && b && c;

endmodule

"""

if __name__ == "__main__":

    # stores all edges and nodes in an array
    # use add_node(node_object) and add_edge(edge_object) to add 
    graph = Graph()

    # the 3 input connectors
    # see the sample_diagram.png file for a representation of this code
    input_node_a = Node("INPUT", 2)
    input_node_b = Node("INPUT", 3)
    input_node_c = Node("INPUT", 4)

    """
    a && b -> ab
    ab && c -> abc
    """

    # the two AND gates
    and_node_a_b = Node("AND", 6)
    and_node_ab_c = Node("AND", 5)

    # edge objects connecting input wire a and input wire b to the first AND gate
    edge_object_a = Edges(input_node_a, and_node_a_b, 0)
    edge_object_b = Edges(input_node_b, and_node_a_b, 0)

    # edge objects connecting output from first AND gate and input C to 2nd AND gate
    edge_object_a_b = Edges(and_node_a_b, and_node_ab_c, 0)
    edge_object_ab_c = Edges(input_node_c, and_node_ab_c, 0)

    # node and edge object connecting output from 2nd AND gate to output
    # setting arbitrary value of 7 here until its handled better. using the bit value doesn't work because it'd be the same as another node
    output_node_o = Node("OUTPUT", 7)
    edge_object_output = Edges(and_node_ab_c, output_node_o, 0)

    # this will be automatic in the future once we start reading from JSON files
    graph.add_node(input_node_a)
    graph.add_node(input_node_b)
    graph.add_node(input_node_c)
    graph.add_node(and_node_a_b)
    graph.add_node(and_node_ab_c)
    graph.add_node(output_node_o)

    graph.add_edge(edge_object_a)
    graph.add_edge(edge_object_b)
    graph.add_edge(edge_object_a_b)
    graph.add_edge(edge_object_ab_c)
    graph.add_edge(edge_object_output)

    graph.create_gv_file()