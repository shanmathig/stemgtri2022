
class Netlist_Node:

    def __init__(self, gate_type, node_id, locked=False):
        """
        Constructor that initializes object with specified gate type (ex. OR, AND, etc...) and a node ID 
        (currently determined by the bits value given by yosys).
        """
        self.gate_type = gate_type
        self.id = node_id
        self.locked = locked
        self.edges = []

    def lock_node(self):
        """Locks a node for KL algorithm."""
        self.locked = True

    def add_edge(self, edge):
        """Adds an edge to the array. 
        Used this instead of adding nodes to store extra info about weight of edges.
        The Netlist_Edges class stores the targets for directed graphs."""
        self.edges.append(edge)

    def get_edges(self):
        """Returns the array of edges associated with the node."""
        return self.edges

    def get_gate_type(self):
        """Return the gate type."""
        return self.gate_type

    def get_node_id(self):
        """Return the node ID."""
        return self.id

    def get_lock_status(self):
        """Accessor method that returns whether Node is locked (used in algorithms)."""
        return self.locked

    def __repr__(self):
        """Return the ID of the node."""
        return 'Node {}'.format(self.id)