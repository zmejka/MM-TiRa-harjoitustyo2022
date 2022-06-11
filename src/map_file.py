import os

dirname = os.path.dirname(__file__)

class MapFile:
    ''' Luokka tiedoston lukua varten.
        Args:
            file : annettu tiedosto
     '''
    def __init__(self, file):
        self.file = file

    def read_map(self):
        ''' Metodi lukee tiedoston ja jakaa riveihin. '''
        map_file = os.path.join(dirname, self.file)
        try:
            with open(map_file, "r", encoding="utf-8") as map_data:
                return map_data.read().splitlines()
        except Exception as exc:
            raise SystemExit from exc

    def parameters(self):
        ''' Metodi kutsuu read_map() metodia ja muuttaa kartan matriisimuotoon.
            Tiedoston ensimmäiset 4 riviä sisältävät otsikkotiedot sekä kartan
            leveys- ja pituustiedot pikseleissä.
            Palauttaa:
            tuple : karttamatriisi, leveys, korkeus
            '''
        data = self.read_map()
        height = int(data[1].split(" ")[1])
        width = int(data[2].split(" ")[1])
        del data[:4]
        map_data = []
        for line in data:
            map_data.append(list(line))
        return (map_data, width, height)
