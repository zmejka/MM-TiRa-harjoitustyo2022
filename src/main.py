import os
import pygame
from a_star import AStar
from jps import Jps
from map_file import MapFile
from ui.view import View, Button

dirname = os.path.dirname(__file__)
BACKGROUND = (96,123,139)
FILES = ["ca_cave.map",
         "dr_dungeon.map",
         "ht_mansion2.map",
         "brc000d.map",
         "dr_primevalentrance.map",
         "brc201d.map",
         "lt_warehouse_n.map",
         "den012d.map",
         "lt_hangedman.map",
         "lt_undercitydungeon.map"]

ALGORITHMS = {1:"A*", 2:"JPS", 3:"Dijkstra"}
HEURISTICS = {0:"-" ,1:"Manhattan", 2:"Euclidean", 3:{"Diagonal"}}

class Main:
    ''' Args:
            width : leveys pikseleinä
            height : korkeus pikseleinä
            start_point : aloituskoordinaatit
            end_point : kohdekoordinaatit
    '''

    def __init__(self):
        self.map_data = 1
        self.algorithm = 1
        self.heuristic = 2
        self._width = 40
        self._height = 120
        self.start_point = (0,0)
        self.end_point = (0.0)

    def main(self):
        ''' Ohjelman suoritus.
            Huom! pylint tarkastus on poistettu pygame 'no-member' riveiltä.
        '''
        pygame.init() # pylint: disable=no-member
        self.get_map()
        self.get_parameters()
        objects = self.start()
        print(" -------- Reittihaku -------- ")
        print(f"Algoritmi: {ALGORITHMS[self.algorithm]}, Heuristiikka: {HEURISTICS[self.heuristic]}.")
        self.main_loop(objects)

        pygame.quit() # pylint: disable=no-member

    def main_loop(self, objects):
        ''' Pääsilmukka. '''
        clock = pygame.time.Clock()
        clock.tick(20)
        points = objects[1].get_points(objects)
        start_c = (int(points[0][0]/2), int(points[0][1]/2))
        end_c = (int(points[1][0]/2), int(points[1][1]/2))
        if self.algorithm in (1, 3):
            results = objects[6].a_star(start_c, end_c, self.heuristic, self.algorithm)
        else:
            results = objects[6].jps(start_c, end_c)
        if isinstance(results, str):
            print (results)
        else:
            objects[1].update_map(results)

        reset_button = Button(" Uusi kartta ", (objects[2]-130, objects[3]-40))
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: # pylint: disable=no-member
                    raise SystemExit
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if reset_button.click_event(event):
                        pygame.quit()
                        self.main()
            reset_button.show_button(objects[0], reset_button)
            pygame.display.update()
        pygame.display.update()

    def start(self):
        ''' Aloitustoiminnot. '''

        file = FILES[self.map_data-1]
        map_file = MapFile(os.path.join(dirname, "maps", file))
        parameters = map_file.parameters()
        if self.algorithm in (1, 3):
            a_star = AStar(parameters[0])
        else:
            jps = Jps(parameters[0])
        scr_width = self._width + 2*parameters[1]
        scr_height = self._height + 2*parameters[2]
        screen = pygame.display.set_mode((scr_width, scr_height))
        screen.fill(BACKGROUND)
        pygame.display.set_caption("Minne Matka?")
        view = View(screen, scr_width, scr_height)
        view.initialize(parameters)
        pygame.display.update()
        if self.algorithm in (1, 3):
            return (screen, view, scr_width, scr_height, parameters[2], parameters[1], a_star)
        return (screen, view, scr_width, scr_height, parameters[2], parameters[1], jps)
    
    def get_map(self):
        map_file = input("Anna kartan numero (1-10): ")
        try:
            if int(map_file) in range(1, 11):
                self.map_data = int(map_file)
            else:
                print("Jokin meni pieleen. Valittu kartta numero 1. ")
        except ValueError:
            print("Jokin meni pieleen. Valittu kartta numero 1. ")
    
    def get_parameters(self):
        used_algorithm = input("Anna algoritmin koodi 1 = A*, 2 = JPS, 3 = Dijkstra: ")
        try:
            if int(used_algorithm) in range(1, 4):
                self.algorithm = int(used_algorithm)
            else:
                print("Jokin meni pieleen. Valittu algoritmi A*. ")
        except ValueError:
            print("Jokin meni pieleen. Valittu algoritmi A*. ")

        if self.algorithm == 1:
            used_heuristic = input("Heuristiikka. 1= Manhattan, 2= Euclidean, 3= Diagonal: ")
            try:
                if int(used_heuristic) in range(1, 4):
                    self.heuristic = int(used_heuristic)
                else:
                    print("Jokin meni pieleen. Valittu euklidinen heuriistikka. ")
            except ValueError:
                print("Jokin meni pieleen. Valittu euklidinen heuriistikka. ")
        else:
            self.heuristic = 0
