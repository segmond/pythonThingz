# produce/consume simulation
from random import randint
class Queue:
    queue = []
    queue_capacity = 5

    def full(self):
        if len(self.queue) >= self.queue_capacity:
            return True
        else:
            return False

    def empty(self):
        return len(self.queue) <= 0

    def add(self, item):
        if len(self.queue) < self.queue_capacity:
            self.queue.append(item)

    def remove(self):
        if len(self.queue) > 0:
            item = self.queue[0]
            self.queue.remove(item)
            return item
        else:
            return None

queue = Queue()

def produce():
    item = 0
    while True:
        produce_n = randint(0,5)
        while produce_n > 0 and not queue.full():
            item = item + 1
            print "producer made ", item
            queue.add(item)
            produce_n = produce_n - 1
        yield


def consume():
    while True:
        consume_n = randint(0,5)
        while consume_n > 0 and not queue.empty():
            item = queue.remove()
            print "consumer got ", item
            consume_n = consume_n - 1
        yield

p = produce()
c = consume()
while True:
    while p.next():
        pass
    while c.next():
        pass
