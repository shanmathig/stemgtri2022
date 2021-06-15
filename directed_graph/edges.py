
class Edges:

    def __init__(self, edge_source, edge_target, edge_weight):
        """
        Initialize class with source node object that edge originates from, target node object that edge points to,
        and the weight of the edge.
        """
        self.source = edge_source
        self.target = edge_target
        self.weight = edge_weight

    def get_source(self):
        """Get the source of the edge, or what node it originates from."""
        return self.source

    def get_target(self):
        """Get the target of the edge, or what node it is directed towards."""
        return self.target

    def get_weight(self):
        """Get the weight of the edge."""
        return self.weight
    
    def __repr__(self):
        """Return the representation of the edges object."""
        return '{} connects to {}'.format(self.source, self.target)
