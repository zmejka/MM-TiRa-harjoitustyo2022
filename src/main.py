import os
import pygame

from map_file import MapFile
from ui.view import View

dirname = os.path.dirname(__file__)
BACKGROUND = (96,123,139)

class Main:
    ''' Args:
            width : leveys pikseleinä
            height : korkeus pikseleinä
            start_point : aloituskoordinaatit
            end_point : kohdekoordinaatit
    '''
    def __init__(self):
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
        self.main_loop(objects[0], objects[1])
        pygame.quit() # pylint: disable=no-member

    def main_loop(self, screen, view):
        ''' Pääsilmukka. '''
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    raise SystemExit
                if event.type == pygame.MOUSEBUTTONDOWN:
                    position = pygame.mouse.get_pos()
                    self.get_coordinates(position, screen, view)
            pygame.display.update()

    def start(self):
        ''' Aloitustoiminnot. '''
        file = "ca_caverns2.map"
        map_file = MapFile(os.path.join(dirname, "maps", file))
        parameters = map_file.parameters()
        screen_width = self._width + 2*parameters[2]
        screen_height = self._height + 2*parameters[1]
        screen = pygame.display.set_mode((screen_width, screen_height))
        screen.fill(BACKGROUND)
        pygame.display.set_caption("Minne Matka?")
        view = View(screen, screen_width, screen_height)
        view.initialize(parameters)
        pygame.display.update()
        return (screen, view)

    def get_coordinates(self, position, screen, view):
        ''' Aloitus-/kohdepisteen laittaminen kartalle.
            Tarkistetaan, että piste on hyväksytyllä alueella.
            Lisätään piste kartalle ja tallennetaan koordinaatit.
            Args:
                position : hiiren klikkauksen koordinaatit
                screen : ikkuna tiedot
                view : käyttöliittymän tiedot
        '''
        color = screen.get_at(position)
        if color == (238,233,233,255):
            view.place_point(position)
            self.start_point = position
            pygame.display.update()
