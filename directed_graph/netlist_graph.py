class Netlist_Graph:
    def __init__(self):
        """
        Initializes dictionary to be used to store Netlist_Nodes and their edges.
        Format:
        {
            <Netlist_Node object>: [<Netlist_Edges objects>]
        }
        """
        self.nodes = {}
        self.clique_netlist = []

    def add_node(self, node_object, edges):
        """Creates a new item in the dictionary and creates an array that can be used to store Netlist_Edges."""
        self.nodes[node_object] = edges

    def append_edge(self, node_object, edge):
        """Method that adds objects to array one by one after creation of array by add_node() method."""
        # to do: add bulk additions after initialization?
        self.nodes[node_object].append(edge)

    def get_nodes(self):
        """Return all the nodes in the netlist."""
        return self.nodes

    def add_to_clique_netlist(self, clique_array):
        """Add an array of nodes representing a clique to clique_netlist array."""
        self.clique_netlist.append(clique_array)

    def get_clique_based_netlist(self):
        """Returns the array of clique netlists for a graph."""
        return self.clique_netlist

    def create_gv_file(self):
        """Create a .gv file for visualization of the netlist."""

        # to do: replace with parameter value if further use of .gv files is needed
        write_string = 'strict graph textbook {\r\n'
        for node in self.nodes.keys():
            write_string += '\t{} [label={}];\r\n'.format(node.get_node_id(), node.get_gate_type())
            for edge in self.nodes[node]:
                write_string += '\t{} -- {};\r\n'.format(node.get_node_id(), edge.get_target().get_node_id())

        write_string += '}'

        with open('textbook.gv', 'w+') as file:
            file.write(write_string)

    def __repr__(self):
        """Return array of all the edges and their human-readable representation."""
        return str(self.nodes.keys())
