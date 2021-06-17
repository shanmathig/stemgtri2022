class Graph:

    def __init__(self):
        """Construct the graph class and initialize empty arrays for the node and edges objects."""
        self.nodes = []
        self.edges = []

    def add_node(self, node_object):
        """Append a node object to the nodes array."""
        self.nodes.append(node_object)
        
    def add_edge(self, edge_object):
        """Append an edge object to the edges array."""
        self.edges.append(edge_object)

    def get_nodes(self):
        """Get all the nodes of the graph."""
        return self.nodes

    def get_edges(self):
        """Get all the edges of the graph."""
        return self.edges

    def create_gv_file(self):
        """Create a .gv file which can be opened online for a quick visualization."""

        # should replace 'AND3' with parameter value at some point
        write_string = 'strict digraph AND3 {\r\n'
        for node in self.nodes:
            write_string += '\t{} [label={}];\r\n'.format(node.get_node_id(), node.get_gate_type())

        for edge in self.edges:
            write_string += '\t{} -> {};\r\n'.format(edge.get_source().get_node_id(), edge.get_target().get_node_id())

        write_string += '}'

        with open('AND3.gv', 'w+') as file:
            file.write(write_string)


    def __repr__(self):
        """Return array of all the edges."""
        return str(self.edges)