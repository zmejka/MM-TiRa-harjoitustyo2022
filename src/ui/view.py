import pygame

COLOR_MAP = {'@': (40,40,40,255), 'T':(0,139,69,255), '.':(238,233,233,255)}
SCALE = 2

class View:
    ''' Käyttöliittymäluokka
        Args:
            screen : pygame ikkuna
            width : leveys pikseleinä
            height : korkeus pikseleinä
    '''
    def __init__(self, screen, width, hight):
        self.screen = screen
        self.width = width
        self.hight = hight

    def initialize(self, parameters):
        ''' Visualisoi karttanäkymä. Kartta näkyy 2 kertaa suurennettuna.
        '''
        self.screen.fill((96,123,139))
        map_view = parameters[0]
        for i in range(len(map_view)):
            for j in range(len(map_view[i])):
                color = COLOR_MAP[map_view[i][j]]
                rect = pygame.Rect(i*SCALE+20,j*SCALE+20,SCALE, SCALE)
                pygame.draw.rect(self.screen, color, rect)

    def place_point(self, coordinates):
        ''' Näyttää kartalla käyttäjän määrittämä piste punaisena.
        '''
        rect = pygame.Rect(coordinates[0], coordinates[1], 2*SCALE, 2*SCALE)
        pygame.draw.rect(self.screen, (255,0,0), rect)
