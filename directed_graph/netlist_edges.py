class Netlist_Edges:
    def __init__(self, edge_target, edge_weight):
        """Initialize Netlist_Edges class with parameters. Stores the edge targets (which node they point to) and the edge weights."""
        self.weight = edge_weight
        self.target = edge_target

    def get_weight(self):
        """Returns the weight of an edge."""
        return self.weight
    
    def get_target(self):
        """Returns the target node of the edge."""
        return self.target

    def __repr__(self):
        """Return the representation of the edges object."""
        return 'Edge connects to {}'.format(self.target)