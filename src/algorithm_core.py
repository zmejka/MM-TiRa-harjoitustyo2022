'''
    Algoritmien yhteiset perustoiminnot.
'''
from math import sqrt
class AlgorithmCore:
    '''
    Args:
        data : karttadata matriisimuodossa
        path : polku alkuruudusta kohderuutuun, alussa tyhjä
    '''
    def __init__(self, data):
        self.map_data = data
        self.path = []

    def get_map(self):
        '''
        Returns:
            Palauttaa karttadatan.
        '''
        return self.map_data

    def set_map(self, data):
        '''
        Args:
            karttadata matriisimuodossa
        Aseta kartaksi annettu matriisi.
        '''
        self.map_data = data

    def heuristic_method(self, start_node, target_node, heuristic):
        '''
        Args:
            start_node : lähtöruudun koordinaatit
            target_node : kohderuudun koordinaatit
            heuristic : kaytettävä heuristiikka
        Lasketaan x- ja y-arvot. Etäisyys lähtöruudusta kohderuutuun.
        Jos heuristiikka:
            Manhattan : x- ja y- arvojen summa
            Euclidean : Pythagoraan lauseen mukaan laskettu etäisyys
            Diagonal : lasketaan niiden siirtymien lukumäärän,
                jolloin et voi ottaa diagonaaliasia siirtymiä, ja vähennetään
                diagonaalisia siirtymiä.
        Returns:
            Palautetaan laskettu heuristinen etäisyys
        '''
        y_value = abs(start_node[0] - target_node[0])
        x_value = abs(start_node[1] - target_node[1])
        if heuristic == 1:
            return y_value+x_value
        if heuristic == 2:
            return sqrt(y_value**2+x_value**2)
        return (y_value+x_value) + (sqrt(2)-2)*(min(y_value,x_value))

    def get_path(self, end, parent):
        ''' Muodostetaan polku alkuruudusta loppuruutuun.
            Args:
                end : kohderuutu
                parent : lista koordinattipareista
                    jossa toinen pari on ruutu itse ja toinen ruudun vanhempi
            Muodostetaan polku kohderuudista alkuruutuun.
            Returns:
                palautetaan käänteinen lista alkuruudusta kohderuutuun.
        '''
        self.path.append(end)
        node = self.path[-1]
        while parent[node] is not None:
            self.path.append(parent.pop(self.path[-1]))
            node = self.path[-1]
        reversed_path = self.path[::-1]
        path_lenght = self.path_lenght(reversed_path)
        return reversed_path, path_lenght
    
    def path_lenght(self, path):
        lenght = 0
        for index in range(len(path)-1):
            start = path[index]
            end = path[index+1]
            price = self.heuristic_method(start, end, 3)
            lenght += price
            print(index,": siirtymä:", start, "->", end, ": kokonaisuus", lenght)
        return lenght
