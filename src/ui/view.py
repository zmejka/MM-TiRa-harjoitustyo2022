import pygame

COLOR_MAP = {'@': (40,40,40,255),
             'T':(0,139,69,255),
             '.':(238,233,233,255)}

SCALE = 2
BACKGROUND = (96,123,139)
BUTTONS = (0,191,255)

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
        self.screen.fill(BACKGROUND)
        map_view = parameters[0]
        for i in range(len(map_view)):
            for j in range(len(map_view[i])):
                color = COLOR_MAP[map_view[i][j]]
                rect = pygame.Rect(j*SCALE,i*SCALE,SCALE, SCALE)
                pygame.draw.rect(self.screen, color, rect)
    
    def get_points(self, objects):
        start_button = Button("  Aseta aloituspiste  ", (30, objects[3]-80))
        end_button = Button("  Aseta kohdepiste  ", (30, objects[3]-40))
        start_point = []
        end_point = []
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    raise SystemExit
                if start_button.click_event(event):
                    start_click = True
                    while start_click:
                        for start_event in pygame.event.get():
                            if start_event.type == pygame.QUIT:
                                break
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                start_mouse = pygame.mouse.get_pressed()
                                start_pos = pygame.mouse.get_pos()
                                if start_mouse[0]:
                                    if self.get_coordinates(start_pos, objects[0], objects[1], "Start"):
                                        start_point = (start_pos[1],start_pos[0])
                                        start_button.set_name(f"  Aloituspiste: {start_point[0]}, {start_point[1]}  ")
                                        start_click = False
                if end_button.click_event(event):
                    end_click = True
                    while end_click:
                        for end_event in pygame.event.get():
                            if end_event.type == pygame.QUIT:
                                break
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                end_mouse = pygame.mouse.get_pressed()
                                end_pos = pygame.mouse.get_pos()
                                if end_mouse[0]:
                                    if self.get_coordinates(end_pos, objects[0], objects[1], "End"):
                                        end_point = (end_pos[1],end_pos[0])
                                        end_button.set_name(f"  Kohdepiste: {end_point[0]}, {end_point[1]}  ")
                                        end_click = False
            start_button.show_button(objects[0], start_button)
            end_button.show_button(objects[0], end_button)
            pygame.display.update()
            if start_point:
                if end_point:
                    running = False
        return start_point, end_point
    
    def get_coordinates(self, position, screen, view, point):
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
            view.place_point(position, point)
            pygame.display.update()
            return True

    def place_point(self, coordinates, point):
        ''' Näyttää kartalla käyttäjän määrittämä piste punaisena.
        '''
        colors = {"Start":(255,0,0),"End":(0,0,255), "Map": (139,125,123), "Path": (145,44,238)}
        if point == "Start" or point == "End":
            rect = pygame.Rect(coordinates[0], coordinates[1], 3*SCALE, 3*SCALE)
        else: rect = pygame.Rect(coordinates[0], coordinates[1], 2*SCALE, 2*SCALE)
        pygame.draw.rect(self.screen, colors[point], rect)

    def update_map(self, results):
        for i in results[0]:
            self.place_point((i[1]*SCALE,i[0]*SCALE), "Map")
            pygame.time.delay(4)
            pygame.display.update()
        for i, j in enumerate(results[1]):
            if i == 0:
                self.place_point((j[1]*SCALE,j[0]*SCALE), "Path")
            else:
                coord = results[1][i-1]
                pygame.draw.line(self.screen, (145,44,238), (j[1]*SCALE,j[0]*SCALE),(coord[1]*SCALE, coord[0]*SCALE), SCALE*2)
            pygame.time.delay(10)
            pygame.display.update()

class Button:
    def __init__(self, name, position):
        self.x = position[0]
        self.y = position[1]
        self.font = pygame.font.SysFont("Arial", 18)
        self.name = name
        self.set_name(name)

    def set_name(self, new_name):
        self.text = self.font.render(new_name, True, (25,25,112,255))
        self.size = self.text.get_size()
        self.surface = pygame.Surface(self.size)
        self.surface.fill((96,155,155))
        self.surface.blit(self.text, (0,0))
        self.rect = pygame.Rect(self.x, self.y, (self.size[0]+10), (self.size[1]+10))

    def show_button(self, screen, button):
        screen.blit(button.surface, (self.x, self.y))

    def click_event(self, event):
        position = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                if self.rect.collidepoint(position):
                    return True
        return False
