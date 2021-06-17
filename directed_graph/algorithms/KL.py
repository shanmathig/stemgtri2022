
class KL:

    def __init__(self, graph):
        """Initialize the KL algorithm with necessary class variables.
        Requires Netlist_Graph class as graph parameter.
        The left and right sides of the partition are currently created manually to test the algorithm with the textbook problem."""
        self.graph_nodes = graph.get_nodes()
        #self.left_side = dict(list(self.graph_nodes.items())[int(len(self.graph_nodes)/2):])
        #self.right_side = dict(list(self.graph_nodes.items())[:int(len(self.graph_nodes)/2)])

        # to do: find a more efficient way to use indices later in the code so that copies dont need to be created.
        self.left_side_unmodified = {k: v for k, v in self.graph_nodes.items() if k.get_node_id() == 1 or k.get_node_id() == 2 or k.get_node_id() == 4 or k.get_node_id() == 5}
        self.right_side_unmodified = {k: v for k, v in self.graph_nodes.items() if k.get_node_id() == 3 or k.get_node_id() == 6 or k.get_node_id() == 7 or k.get_node_id() == 8}

        self.left_side = self.left_side_unmodified.copy()
        self.right_side = self.right_side_unmodified.copy()
    
    def get_left_side(self):
        """
        Gets the nodes in the left partition.
        Returns a dictionary.
        """
        return self.left_side

    def get_right_side(self):
        """
        Gets the nodes in the right partition.
        Returns a dictionary.
        """
        return self.right_side
        

    def calc_costs(self, node_1, node_2=None, calc_xy_cost=False):
        """
        Calculates all necessary costs, including E_x - I_x, E_y - I_y, and c(x,y)
        """
        # checks whether e_x - i_x should be calculated or whether e_y - i_y and c(x,y) should be calculated
        # e_x - i_x is calculated only once
        # e_y - i_y and c(x,y) are calculated in the same loop because both pairs in the test swap are included
        if node_2 is not None or calc_xy_cost:
            # select which node in the pair to use
            edges = self.graph_nodes[node_2]
            # select which side to compare to to determine external vs internal costs
            external_side = self.left_side
        else:
            edges = self.graph_nodes[node_1]
            external_side = self.right_side
        # base values for costs
        external_cost = 0
        internal_cost = 0
        xy_cost = 0
        # loops through all edges associated with the specified node
        for edge in edges:
            # checks if c(x,y) should be calculated and, if so, checks if there is a direct connection between x and y and stores the edge weight
            if calc_xy_cost and edge.get_target().get_node_id() == node_1.get_node_id():
                xy_cost = edge.get_weight()
            # checks if edge is external or internal
            if edge.get_target() in external_side:
                external_cost += edge.get_weight()
            else:
                internal_cost += edge.get_weight()
        return (external_cost - internal_cost, xy_cost)


    def calc_gain(self, ex_minus_ix, ey_minus_iy, xy_cost):
        """
        Gain formula for KL.
        gain(x,y) = (E_x - I_x) + (E_y - I_y) - 2c(x,y)
        """
        return ex_minus_ix + ey_minus_iy - 2*xy_cost

    def swap_loops(self):
        """Contains main loops used in the KL swaps."""
    
        # number to be incremented in while loop
        swap_num = 0

        # checks if all variations of swaps have been completed based
        while swap_num < max(len(self.left_side_unmodified), len(self.right_side_unmodified)):

            # variables used to store what the best gain is
            max_gain = -999
            max_gain_pair = []
            # used to set the index
            swap_index = []


            # enumerates unmodified dictionary for the left and right sides
            # using the modified dictionary messes with the indices, which means positions would be incorrect in the final array returned by the swap_pairs method
            for index, i in enumerate(self.left_side_unmodified):
                # only checks gains if the node has not already been locked
                if not i.get_lock_status():
                    # calculate costs
                    ex_minus_ix, _ = self.calc_costs(i)

                    # enumerates right side
                    # used to calculate e_y - i_y and c(x,y)
                    for index_2, j in enumerate(self.right_side_unmodified):
                        # only checks gains and costs if node has not already been locked
                        if not j.get_lock_status():
                            # calculate cost (including c(x,y), hence the calc_xy_cost=True param)
                            ey_minus_iy, xy_cost = self.calc_costs(i, j, calc_xy_cost=True)
                            # calculate gain using gain formula
                            current_swap_gain = self.calc_gain(ex_minus_ix, ey_minus_iy, xy_cost)
                            # check if current swap variation is the maximum gain swap
                            # if it is, it updates variables and stores the two nodes that led to this max gain
                            if current_swap_gain > max_gain:
                                max_gain = current_swap_gain
                                max_gain_pair = [i, j]
                                swap_index = [index, index_2]
                                
            # locks nodes with the max gain
            max_gain_pair[0].lock_node()
            max_gain_pair[1].lock_node()
            
            # updates left side and right side dictionaries that store nodes on each side with the maximum gains, thereby completing the swap
            # updates are appended to the end, which is why the indices are a problem using enumeration as mentioned earlier
            self.left_side[max_gain_pair[1]] = self.right_side[max_gain_pair[1]]
            self.right_side[max_gain_pair[0]] = self.left_side[max_gain_pair[0]]
            del self.left_side[max_gain_pair[0]]
            del self.right_side[max_gain_pair[1]]
            
            # adds max gain to specific index in the final array that will be returned in the swap_pairs() method
            self.right_final[swap_index[1]] = max_gain_pair[0]
            self.left_final[swap_index[0]] = max_gain_pair[1]
            # increments swap number (for the while loop)
            swap_num += 1
        

    def swap_pairs(self):
        """Creates class variables that store the final arrays that will be returned."""
        self.left_final = [0] * max(len(self.left_side), len(self.right_side))
        self.right_final = [0] * max(len(self.left_side), len(self.right_side))

        self.swap_loops()
        
        return self.left_final, self.right_final