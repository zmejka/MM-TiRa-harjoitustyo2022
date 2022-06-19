import heapq as heap

class Queue:
    def __init__(self):
        self.queue = []

    def add_to_queue(self, value):
        heap.heappush(self.queue, (value[1], value[0]))

    def is_empty(self):
        if not self.queue:
            return True
        return False

    def clear_queue(self):
        self.queue = []

    def remove_from_queue(self):
        value = heap.heappop(self.queue)
        return value[1],value[0]

    def get_queue(self):
        return self.queue
