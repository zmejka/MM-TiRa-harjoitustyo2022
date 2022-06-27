''' JPS - algorithm
    Args:
    COST : verekkäin olevien ruutujen hinta, 1
    DIAG_COST : diagonaalisesti vierekkäin olevien ruutujen hinta, neliöjuuri(2)
    DIRECTIONS : 8 suunnan siirtymäkoordinaatit
'''
from math import sqrt

from min_queue import Queue
from algorithm_core import AlgorithmCore

COST = 1
DIAG_COST = sqrt(2)
DIRECTIONS = [(1,1),(1,-1),(-1,1),(-1,-1), (1,0),(0,1),(0,-1),(-1,0)]

class Jps:
    ''' Args:
            map : karttadata matriisimuodossa
            open_queue : avoin-lista tarkistettavia ruutuja
            closed_list : lista ruutuja, jotka on jo tarkastettu
            path : polku alkuruudusta kohderuutuun
            parent : lista vanhempiruutuja polkun rakentamista varten
            cost : lista, johon on tallennettu etäisyydet alkuruudusta ruutuun
            ready : kohderuutu on loytynyt
            end : kohderuutu
            jps_core : algorithm core olio
            counters : testausta varten
            '''
    def __init__(self, data):
        self.map = data
        self.open_queue = Queue()
        self.close_list = {}
        self.parent = {}
        self.cost = {}
        self.ready = False
        self.end = (0,0)
        self.start = (0,0)
        self.jps_core = AlgorithmCore(self.map)
        self.open_counter = 1
        self.close_counter = 0

    def jps(self, start, end):
        ''' JPS algoritmin päätoiminto:
        Args:
            start : alkuruutu
            end : kohderuutu
        Alkuruutu lisätään avoimelle listalle, parent listalle sekä cost-listalle.
            Alkuruudun hinta on 0.
        Niin kauan, että minimikeossa on ruutuja:
            Tarkistetaan, onko kohderuutu on lyötynyt.
                Jos ei, poimitaan ruutu keosta.
            Jos poimitu ruutu on kohderuutu, kutsutaan polun muodostus metodi ja
                palautetaan tulokset.
            Jos poimittu ruutu on close-listalla, jatketaan seuraavaan ruutuun
            Muuten kutsutaan laajennusmetodi.
        Jos minimikeossa ei ole enää ruutuja tai kohderuutu on löytynyt,
            Kutsutaan polun muodostus metodia tai palautetaan tiedon, että polkua ei löytynyt.
        '''
        self.end = end
        self.start = start
        self.parent[start] = None
        self.cost[start] = 0
        self.open_queue.add_to_queue((start, 0))

        while not self.open_queue.is_empty():
            if self.ready:
                break
            node = self.open_queue.remove_from_queue()
            if node[0] == end:
                result_path = self.jps_core.get_path(self.end, self.parent)
                return (self.parent, result_path, self.open_counter, self.close_counter)
            if node[0] in self.close_list:
                continue
            self.close_list[node[0]] = self.cost[node[0]]
            self.close_counter = self.close_counter + 1
            self.expand_node(node)
        if self.ready:
            results = self.jps_core.get_path(self.end, self.parent)
            return (self.parent, results, self.open_counter, self.close_counter)
        return "Polkua ei löytynyt!"

    def expand_node(self, node):
        ''' Ruudun skannaus 8 suuntaan.
        Args:
            node : tarkastettava ruutu
        Jokaiseen annetun suuntaan:
            Cost-listaan lisätään etäisyys alkuruudusta tarkastettavaan ruutuun.
            Jos tarkistettava suunta on diaginaalinen:
                suoritetaan diagonaalisen skannauksen annettuun suuntaan
            Muulloin:
                suoritetaan joko pysty- tai vaakasuunnan stannaus
            Jos skannaus palauttaa tyhjä tai palautettu koordinaatti on jo close-listalla,
                siirrytään seuraavaan suuntaan
            Muulloin:
                Jos kohderuutu on löytynyt,
                    lisätään parent listaan tarkastettavan ruudun vanhemmaksi annettu ruutu
                    lisätään kekoon tuple : (tarkastettava ruutu, etäisyys 1) ja vanhempi ruutu
                Muulloin:
                    lisätään kekoon tuple : tarkastettava ruutu, vanhempi ruutu
        '''
        for direction in DIRECTIONS:
            distance = self.cost[node[0]]
            if direction[0]!=0 and direction[1]!=0:
                scan = self.diag_jump(node, distance, direction)
            else:
                scan = self.hor_ver_jump(node, distance,direction)
            if scan is None or scan in self.close_list:
                continue
            if self.ready:
                self.parent[self.end] = node[0]
                self.new_jump_point((scan[0], 1), node)
            self.new_jump_point(scan, node)

    def new_jump_point(self, node, parent_node):
        ''' Lisääminen minimikekon.
        Args:
            node : ruutu
            parent_node : ruudun vanhempi
        Lasketaan g-arvo (etäisyys alkuruudusta tarkistettavaan ruutuun).
        Jos ruudun koordinaatit eivät ole cost-listalla tai
        g-arvo on pienempi kuin arvo cost-listalla,
            lisätään cost-listaan g-arvo,
            lasketaan f-arvo (käytetään Diagonal-heuristiikka)
            lisätään parent listaan tarkastettavan ruudun vanhemmaksi annettu ruutu
            lisätään kekoon tuple : koordinaatit, f-arvo
            päivitetään open-listan laskuri yhdellä
        '''
        g_value = node[1]
        if node[0] not in self.cost or g_value < self.cost[node[0]]:
            self.cost[node[0]] = g_value
            f_value = g_value + self.jps_core.heuristic_method(node[0], self.end, 0)
            self.parent[node[0]] = parent_node[0]
            self.open_queue.add_to_queue((node[0], f_value))
            self.open_counter = self.open_counter + 1

    def diag_jump(self, node, distance, direc):
        ''' Diagonaalinen skannaus
        Args:
            node : tarkistettava ruutu
            distance : etäisyys alkuruudusta tarkastettavaan ruutuun
            direc : skannaussuunta
        Tarkastettavan ruudun naapuri annetussa suunnassa:
            Jos naapuriruutu ei ole kartalla, palautetaan tyhjä
            Jos naapuriruutu on este tai ruutu on jo tarkastettu, palautetaan tyhjä
            Jos naapuriruutu on kohderuutu, asetetaan ready arvo True:ksi ja
                palautetaan naapuriruutu ja etäisyys siihen asti
            Jos piste on kulkukelpoinen;
                Jos naapuriruutu on hyppypiste,
                    palautetaan naapuriruutu ja etäisyys siihen asti
                Jos naapuriruudusta suoritettu pysty- tai vaakaskannaus ei ole tyhjä,
                    palautetaan naapuriruutu ja etäisyys siihen asti
            Muulloin jatketaan skannausta samaan diagonaaliseen suuntaan.
        Returns:
            jump-point koordinaatit, etäisyys
        '''
        next_x = node[0][0]+direc[0]
        next_y = node[0][1]+direc[1]
        dist = distance + DIAG_COST
        if next_x > (len(self.map)-2) or next_x < 2:
            return None
        if next_y > len(self.map[0])-2 or next_y < 2:
            return None
        if self.map[next_x][next_y] != '.' or (next_x,next_y) in self.close_list:
            return None
        if (next_x,next_y) == self.end:
            self.ready = True
            return (next_x,next_y), dist
        if self.map[next_x][next_y] == '.':
            if self.map[node[0][0]][next_y]!='.' and self.map[node[0][0]][next_y+direc[1]]=='.' or \
                self.map[next_x][node[0][1]]!='.' and self.map[next_x+direc[0]][node[0][1]]=='.':
                return (next_x,next_y),dist
            if self.hor_ver_jump(((next_x,next_y),0), dist, (direc[0],0)) is not None or \
                self.hor_ver_jump(((next_x,next_y),0), dist, (0, direc[1])) is not None:
                return (next_x,next_y),dist
        return self.diag_jump(((next_x,next_y),0), dist, direc)

    def hor_ver_jump(self, node, distance, direc):
        ''' Pysty- tai vaakasuunnan skannaus
        Args:
            node : tarkistettava ruutu
            distance : etäisyys alkuruudusta tarkastettavaan ruutuun
            direc : skannaussuunta
        Tarkastettavan ruudun naapuri annetussa suunnassa:
            Jos naapuriruutu ei ole kartalla, palautetaan tyhjä
            Jos naapuriruutu on este tai ruutu on jo tarkastettu, palautetaan tyhjä
            Jos naapuriruutu on kohderuutu, asetetaan ready arvo True:ksi ja
                palautetaan naapuriruutu ja etäisyys siihen asti
            Jos piste on kulkukelpoinen;
                Jos naapuriruutu on hyppypiste,
                    palautetaan naapuriruutu ja etäisyys siihen asti
            Muulloin jatketaan skannausta samaan pysty-/vaaka-suuntaan.
        Returns:
            jump-point koordinaatit, etäisyys
        '''
        next_x = node[0][0]+direc[0]
        next_y = node[0][1]+direc[1]
        if next_x > len(self.map)-2 or next_x < 2:
            return None
        if next_y > len(self.map[0])-2 or next_y < 2:
            return None
        dist = distance + COST
        if self.map[next_x][next_y] != '.' or (next_x,next_y) in self.close_list:
            return None
        if (next_x,next_y) == self.end:
            self.ready = True
            return (next_x,next_y), dist
        if self.map[next_x][next_y] == '.':
            if direc[1] == 0:
                if self.map[next_x][next_y-1]!='.' and self.map[next_x+direc[0]][next_y-1]=='.' or \
                    self.map[next_x][next_y+1]!='.' and self.map[next_x+direc[0]][next_y+1]=='.':
                    return (next_x,next_y),dist
            if direc[0] == 0:
                if self.map[next_x-1][next_y]!='.' and self.map[next_x-1][next_y+direc[1]]=='.' or \
                    self.map[next_x+1][next_y]!='.' and self.map[next_x+1][next_y+direc[1]]=='.':
                    return (next_x,next_y),dist
        return self.hor_ver_jump(((next_x,next_y),0), dist, direc)
