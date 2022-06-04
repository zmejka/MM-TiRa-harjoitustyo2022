import os
import pygame
from a_star import AStar
from jps import Jps
from map_file import MapFile
from ui.view import View

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

class Main:
    ''' Args:
            width : leveys pikseleinä
            height : korkeus pikseleinä
            start_point : aloituskoordinaatit
            end_point : kohdekoordinaatit
    '''

    def __init__(self, map_data, algorithm):
        self.map_data = int(map_data)
        self.algorithm = int(algorithm)
        self._width = 40
        self._height = 120
        self.start_point = (0,0)
        self.end_point = (0.0)

    def main(self):
        ''' Ohjelman suoritus.
            Huom! pylint tarkastus on poistettu pygame 'no-member' riveiltä.
        '''
        pygame.init() # pylint: disable=no-member
        objects = self.start()
        self.main_loop(objects)

        pygame.quit() # pylint: disable=no-member

    def main_loop(self, objects):
        ''' Pääsilmukka. '''
        clock = pygame.time.Clock()
        clock.tick(20)
        points = objects[1].get_points(objects)
        start_c = (int(points[0][0]/2), int(points[0][1]/2))
        end_c = (int(points[1][0]/2), int(points[1][1]/2))
        if self.algorithm == 1:
            results = objects[6].a_star(start_c, end_c)
        else:
            results = objects[6].jps(start_c, end_c)

        objects[1].update_map(results)

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: # pylint: disable=no-member
                    raise SystemExit

        pygame.display.update()

    def start(self):
        ''' Aloitustoiminnot. '''

        file = FILES[self.map_data-1]
        map_file = MapFile(os.path.join(dirname, "maps", file))
        parameters = map_file.parameters()
        if self.algorithm == 1:
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
        if self.algorithm == 1:
            return (screen, view, scr_width, scr_height, parameters[2], parameters[1], a_star)
        return (screen, view, scr_width, scr_height, parameters[2], parameters[1], jps)
