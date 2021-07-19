from .KL import KL
from netlist_graph import Netlist_Graph
import json

class Mincut:
    def __init__(self, graph: Netlist_Graph, left_partition_predefined:list=None, grid_size:int=1, debug:bool=False) -> None:
        """
        Initializes Mincut class. 
        Required parameters: 
            graph -> instance of Netlist_Graph object
        Optional parameters: 
            left_partition_predefined -> list of Netlist_Node objects, 
            grid_size -> int defining how many nodes should be in the final grid placement - currently only works with 1
            debug -> boolean specifying whether additional info should be printed out
        """
        self.original_graph = graph
        self.graph_nodes = graph.get_nodes()
        if not left_partition_predefined is None:
            self.left_partition_predefined = left_partition_predefined
        else:
            self.left_partition_predefined = []
        # how many gates should be inside each placement - not tested for values greater than 1
        self.grid_size = grid_size
        self.debug = debug
        self.json = {'data': []}

        self.json['data'].append(
            self.side_to_json(self.graph_nodes),
        )

    def side_to_json(self, side:dict) -> dict:
        side_json = json.loads(str(side))
        side_json_modified = {}
        for x in side_json.keys():
            side_json_modified[x.replace("Node ", "")] = [y.replace("Edge connects to Node ", "") for y in side_json[x]]
        return side_json_modified

    def run_KL(self, left_side:list=[]) -> list:
        """Runs KL algorithm with all the unlocked nodes to find the best swap based on cutsize."""
        # initialize KL with predefined left side nodes
        partition = KL(self.original_graph, left_side)
        # runs the KL swap
        partition.swap_pairs()
        # gets the swap with the best cutsize
        partition_final_result = partition.get_best_swap_from_cutsize()

        return partition_final_result

    def run(self, group_nodes:list=[], initial_loop:bool=False, cut_direction:int=0, x_pos:int=0, y_pos:int=0) -> None:
        """
        Runs main recursive quadrature Mincut algorithm.
        The cut_direction parameter stores whether the cut is horizontal or vertical.
        If cut_direction is even, it is a vertical cut, if cut_direction is odd then it is a horizontal cut.
        x and y positions are changed based on whether it is a horizontal or vertical cut and
        based on how many nodes are placed to the top of or to the left of a quadrant.
        """
        # the stop condition - stops when each grid has the specified amount of nodes inside of it
        if len(group_nodes) == self.grid_size:
            # sets the position of the node
            for node in group_nodes:
                node.set_position(x_pos, y_pos)
                # adds the nodes in the final grid to a final array that stores the mincut results
                self.mincut_result.append(node)
            # breaks from recursion
            return

        # unlocks all the nodes needed for this recursion
        # necessary because each run of KL locks nodes
        for node in group_nodes:
            node.unlock_node()

        # checks whether this is the first run of KL or not
        if initial_loop:
            # calls to function to run KL with the initial, specified left partition
            # this only applies to the first run of KL
            KL_data_returned = self.run_KL(self.left_partition_predefined)
            group_1, group_2 = KL_data_returned[0]
            KL_sequence = KL_data_returned[1]
        else:
            # splits nodes in a grid into 2 and runs KL on them
            KL_data_returned = self.run_KL(group_nodes[0:round(len(group_nodes)/2)])

            group_1, group_2 = KL_data_returned[0]
            KL_sequence = KL_data_returned[1]
            #group_1, group_2 = self.run_KL(group_nodes[0:round(len(group_nodes)/4)] + group_nodes[round(len(group_nodes)/2):round(len(group_nodes)*3/4)])

        group_1_x = x_pos
        group_1_y = y_pos

        # check if vertical cut
        if cut_direction % 2 == 0:
            # calculates how big the quadrant to the left will be in order to calculate how much to increment the x position
            # this helps avoid overlap in the final resulting coordinates
            group_2_x = x_pos + int(len(group_1)**(1/2))
            group_2_y = y_pos
        # check if horizontal cut
        else:
            group_2_x = x_pos
            group_2_y = y_pos + int(len(group_1)**(1/2))

        # prints results for extended debugging
        if self.debug:
            print(group_1, x_pos, y_pos)
            print(group_2, group_2_x, group_2_y)

        self.json['data'].append({
            'cut_direction': 'V' if cut_direction % 2 == 0 else 'H',
            'cut_number': cut_direction,
            'group_1_coords': (group_1_x, group_1_y),
            'group_2_coords': (group_2_x, group_2_y),
            'group_1_nodes': [str(node) for node in group_1],
            'group_2_nodes': [str(node) for node in group_2],
            'KL_sequence': KL_sequence
        })

        # recursively runs mincut on each grid created by cuts
        # in the future: make these run in parallel?
        self.run(group_1, cut_direction=cut_direction+1, x_pos=group_1_x, y_pos=group_1_y)
        self.run(group_2, cut_direction=cut_direction+1, x_pos=group_2_x, y_pos=group_2_y)

    def calc_half_perimeter(self) -> float:
        """Calculates the half perimeter and wirelength cost for each clique netlist."""
        clique_netlist = self.original_graph.get_clique_based_netlist()
        wirelength = 0
        
        # loops through all clique netlists in graph
        for netlist in clique_netlist:
            # initializes variables
            min_x = float('Inf')
            min_y = float('Inf')
            max_x = 0
            max_y = 0
            half_perimeter = 0
            # loops through all nodes represented in a clique netlist
            for node in netlist:
                # gets the coordinates of each node
                x, y = node.get_position()

                # adjusts above variables if a max or min is found for x or y
                # this finds the max distance between nodes in a clique netlist
                max_x = max(x, max_x)
                min_x = min(x, min_x)
                max_y = max(y, max_y)
                min_y = min(y, min_y)

            # calculates half perimeter and adds it to wirelength cost
            half_perimeter = (max_x - min_x) + (max_y - min_y)
            wirelength += half_perimeter
        
        return wirelength

    def write_json_data(self) -> None:
        """Writes json data to file so that it can be accessed in the frontend."""
        path = 'static/algorithm_json/mincut_data.json' # relative path from working directory (in this case where the app.py is located)
        with open(path, 'w') as file:
            json.dump(self.json, file)
        
    def quadrature(self) -> None:
        """
        Creates variable to store final Mincut result, starts recursion, and prints out placements determined by Mincut.
        """
        self.mincut_result = []
        self.run([], True)

        #print(self.mincut_result)
        #print(self.json)

        self.write_json_data()

        # prints node positions
        if self.debug:
            for node in self.mincut_result:
                print(str(node) + " " + str(node.get_position()))