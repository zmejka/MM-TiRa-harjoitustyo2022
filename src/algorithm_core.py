from math import sqrt
class AlgorithmCore:
    def __init__(self, data):
        self.map_data = data

    def get_map(self):
        return self.map_data

    def set_map(self, data):
        self.map_data = data

    def euclidean(self, start_node, target_node):
        y_value = (start_node[0] - target_node[0])**2
        x_value = (start_node[1] - target_node[1])**2
        h_value = sqrt(y_value+x_value)
        return h_value

    def diagonal(self, start_node, target_node):
        y_value = abs(start_node[0] - target_node[0])
        x_value = abs(start_node[1] - target_node[1])
        h_value = (y_value+x_value) + (sqrt(2)-2)*(min(y_value,x_value))
        return h_value

    def manhattan(self, start_node, target_node):
        y_value = abs(start_node[0] - target_node[0])
        x_value = abs(start_node[1] - target_node[1])
        return y_value+x_value
