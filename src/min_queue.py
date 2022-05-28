class Queue:
    def __init__(self):
        self.queue = []

    def add_to_queue(self, value):
        if value not in self.queue:
            self.queue.append(value)

    def is_empty(self):
        if not self.queue:
            return True
        return False

    def clear_queue(self):
        self.queue = []

    def remove_from_queue(self):
        min_index = 0
        for index, _ in enumerate(self.queue):
            if self.queue[index][1] < self.queue[min_index][1]:
                min_index = index
        return self.queue.pop(min_index)

    def get_queue(self):
        return self.queue
