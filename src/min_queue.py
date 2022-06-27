import heapq as heap

class Queue:
    '''
    queue : alustetaan tyhjä lista
    '''
    def __init__(self):
        self.queue = []

    def add_to_queue(self, value):
        '''
        Lisätään minimikekoon tuple : etäisyys, koordinaatit
        Heap tietorakenne järjestää listan lisämisen jälkeen
            pienemmästä suurempaan.
        '''
        heap.heappush(self.queue, (value[1], value[0]))

    def is_empty(self):
        '''
        Tarkistetaan onko lista tyhjä
        Returns:
            True : jos lista on tyhjä
            False : jos lista ei ole tyhjä
        '''
        if not self.queue:
            return True
        return False

    def remove_from_queue(self):
        '''
        Poimitaan keosta pienemmän etäisyyden.
        Returns:
            koordinaattipari, etäisyys
        '''
        value = heap.heappop(self.queue)
        return value[1],value[0]
