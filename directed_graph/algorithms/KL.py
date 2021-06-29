import datetime
import json
import re

class KL:

    def __init__(self, graph, left_partition_predefined=[]):
        """Initialize the KL algorithm with necessary class variables.
        Requires Netlist_Graph class as graph parameter. 
        left_partition_predefined (for specifying the initial left partition and order of it) is optional and requires node objects.
        The left and right sides of the partition are currently created manually to test the algorithm with the textbook problem."""
        self.cutsize = 0
        self.graph_nodes = graph.get_nodes()
        self.json = {'data': []}

        # create a list of nodes for the left side of the partition if one has not been specified
        if not left_partition_predefined:
            # makes list of the first half of the graph nodes in self.graph_nodes
            filter_list = list(self.graph_nodes.keys())[int(len(self.graph_nodes)/2):]
        else:
            filter_list = left_partition_predefined
        
        # splits nodes into left and right sides
        self.left_side_unmodified = dict(filter(lambda e: e[0] in filter_list, self.graph_nodes.items()))
        self.right_side_unmodified = dict(filter(lambda e: e[0] not in filter_list, self.graph_nodes.items()))

        self.json['data'].append({
            'left_side_unmodified': self.side_to_json(self.left_side_unmodified),
            'right_side_unmodified': self.side_to_json(self.right_side_unmodified)
        })

        self.left_side = self.left_side_unmodified.copy()
        self.right_side = self.right_side_unmodified.copy()

    def side_to_json(self, side):
        side_json = json.loads(str(side))
        side_json_modified = {}
        for x in side_json.keys():
            side_json_modified[x.replace("Node ", "")] = [y.replace("Edge connects to Node ", "") for y in side_json[x]]
        return side_json_modified
    
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

    def calc_initial_cutsize(self):
        """Calculates the initial cutsize so that it can later be used to calculate swap cutsize, which is relative to this."""
        # loop through all the nodes in the left partition
        for node in self.left_side.keys():
            # loop through all the edges in the left partition node
            for edge in self.left_side[node]:
                # check if any edges cross over to the other side and add weights to cutsize if so
                if edge.get_target() in self.right_side:
                    self.cutsize += edge.get_weight()
        
        return self.cutsize

    def after_swap_cutsize(self, left_node, right_node):
        """Calculates cutsize after each swap relative to the initial cutsize."""
        # loops through all the edges in the left side node that was just swapped
        for edge in self.left_side[left_node]:
            # skips finding weight from cutsize if the left side node that was swapped is directly connected to the right side node
            if not edge.get_target() == right_node:
                # adds to cutsize if the edge crosses over to the other side, subtracts from cutsize if not
                if edge.get_target() in self.right_side:
                    self.cutsize += edge.get_weight()
                else:
                    self.cutsize -= edge.get_weight()

        # same as above but for the right side node that was swapped
        for edge in self.right_side[right_node]:
            if not edge.get_target() == left_node:
                if edge.get_target() in self.left_side:
                    self.cutsize += edge.get_weight()
                else:
                    self.cutsize -= edge.get_weight()

        return self.cutsize

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

    @staticmethod
    def calc_gain(ex_minus_ix, ey_minus_iy, xy_cost):
        """
        Gain formula for KL.
        gain(x,y) = (E_x - I_x) + (E_y - I_y) - 2c(x,y)
        """
        return ex_minus_ix + ey_minus_iy - 2*xy_cost

    def run(self):
        """Contains main loops used in the KL swaps."""
    
        # number to be incremented in while loop
        swap_num = 0

        # checks if all variations of swaps have been completed based on which iteration it is
        while swap_num < max(len(self.left_side_unmodified), len(self.right_side_unmodified)):

            swap_start_time = datetime.datetime.now()

            # variables used to store what the best gain is
            max_gain = float('-inf')
            max_gain_pair = []
            # used to set the index
            swap_index = []

            # enumerates unmodified dictionary for the left and right sides
            # using the modified dictionary messes with the indices, which means positions would be incorrect in the final array returned by the swap_pairs method
            for i, first_node_in_pair in enumerate(self.left_side_unmodified):
                # only checks gains if the node has not already been locked
                if not first_node_in_pair.get_lock_status():
                    # calculate costs
                    ex_minus_ix, _ = self.calc_costs(first_node_in_pair)

                    # enumerates right side
                    # used to calculate e_y - i_y and c(x,y)
                    for j, second_node_in_pair in enumerate(self.right_side_unmodified):
                        # only checks gains and costs if node has not already been locked
                        if not second_node_in_pair.get_lock_status():
                            # calculate cost (including c(x,y), hence the calc_xy_cost=True param)
                            ey_minus_iy, xy_cost = self.calc_costs(first_node_in_pair, second_node_in_pair, calc_xy_cost=True)
                            # calculate gain using gain formula
                            current_swap_gain = KL.calc_gain(ex_minus_ix, ey_minus_iy, xy_cost)
                            # check if current swap variation is the maximum gain swap
                            # if it is, it updates variables and stores the two nodes that led to this max gain
                            if current_swap_gain > max_gain:
                                max_gain = current_swap_gain
                                max_gain_pair = [first_node_in_pair, second_node_in_pair]
                                swap_index = [i, j]
                                
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

            # gets time when swap ends
            swap_end_time = datetime.datetime.now()

            # increments swap number (for the while loop)
            swap_num += 1

            # get cutsize after swap
            after_swap_cutsize = self.after_swap_cutsize(max_gain_pair[1], max_gain_pair[0])

            # get time delta in milliseconds
            time_delta = (swap_end_time - swap_start_time).total_seconds() * 1000.0

            # prints out details of the swap after it is complete
            # i, pair, gain, cutsize
            print("{: <20} ({}, {}) \t  {: <20} {: <20} {: <20}".format(
                swap_num, 
                *max_gain_pair,
                max_gain,
                after_swap_cutsize,
                time_delta
            ))

            self.json['data'].append({
                'iteration': swap_num,
                'pair': [max_gain_pair[0].get_node_id(), max_gain_pair[1].get_node_id()],
                'gain': max_gain,
                'cutsize': after_swap_cutsize,
                'swap_time': time_delta
            })

    def write_json_data(self):
        path = 'static/algorithm_json/KL_data.json' # relative path from working directory (in this case where the app.py is located)
        with open(path, 'w') as file:
            json.dump(self.json, file)
        
    def swap_pairs(self):
        """Creates class variables that store the final arrays that will be returned and calculates the initial cutsize."""
        self.left_final = [0] * max(len(self.left_side), len(self.right_side))
        self.right_final = [0] * max(len(self.left_side), len(self.right_side))

        initial_cutsize = self.calc_initial_cutsize()

        # table columns to print out
        # i, pair, gain, cutsize
        print("{: <20} {: <36} {: <20} {: <20} {: <20}".format("i", "pair", "gain", "cutsize", "swap time (milliseconds)"))
        # prints initial cutsize before the first swap
        print("{: <20} {: <36} {: <20} {: <20} {: <20}".format(0, "-", "-", initial_cutsize, "-"))

        self.json['data'].append({
            'iteration': 0,
            'cutsize': initial_cutsize
        })

        self.run()

        self.write_json_data()
        
        return '/static/algorithm_json/KL_data.json'