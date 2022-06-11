from math import sqrt
class AlgorithmCore:
    def __init__(self, data):
        self.map_data = data
        self.path = []

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

    def get_path(self, start, end, parent):
        ''' Muodostetaan polku alkuruudusta loppuruutuun.
            Args:
                start : alkuruutu
                end : loppuruutu
                parent : lista koordinateista,
                    jossa toinen pari on ruutu itse ja toinen ruudun vanhempi
        '''
        self.path.append(end)
        node = self.path[-1]
        while parent[node] is not None:
            if self.path[-1] == start:
                break
            self.path.append(parent.pop(self.path[-1]))
            node = self.path[-1]
        reversed_path = self.path[::-1]
        return reversed_path
