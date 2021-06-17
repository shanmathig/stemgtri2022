class Node:

    def __init__(self, gate_type, node_id, locked=False):
        """
        Constructor that initializes object with specified gate type (ex. OR, AND, etc...) and a node ID 
        (currently determined by the bits value given by yosys).
        """
        self.gate_type = gate_type
        self.id = node_id
        self.locked = locked

    def lock_node(self):
        self.locked = True

    def get_gate_type(self):
        """Return the gate type."""
        return self.gate_type

    def get_node_id(self):
        """Return the node ID."""
        return self.id

    def get_lock_status(self):
        return self.locked

    def __repr__(self):
        """Return the ID of the node."""
        return 'Node {}'.format(self.id)