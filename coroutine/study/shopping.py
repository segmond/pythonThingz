# stupid simulation
from random import randint
from time import sleep

class Queue:
    def __init__(self):
        self.queue = []
        self.queue_capacity = 5

    def add(self, item):
        "add to queue"
        if len(self.queue) < self.queue_capacity:
            self.queue.append(item)

    def full(self):
        """ is queue full """
        if len(self.queue) >= self.queue_capacity:
            return True
        else:
            return False

    def contains(self, item):
        return item in self.queue

    def empty(self):
        """ is queue empty """
        return len(self.queue) <= 0

    def remove(self):
        """ leave queue """
        if len(self.queue) > 0:
            item = self.queue[0]
            self.queue.remove(item)
            return item
        else:
            return None

    def dequeue(self):
        """ dequeue """
        if not self.empty():
            self.queue.remove(self.queue[0])

class FittingRoom:
    queue = Queue()
    use_time = 0
    inuse = False

    def request(self, name, use_time):
        """ request to use fitting room """
        print name, " has requested room"
        if self.inuse:
            return False
        print name, " has entered the fitting room"
        self.inuse = True
        self.use_time = use_time
        return True

    def can_use(self):
        """ can we use the fitting room """
        return True if self.use_time > 0 else False

    def use(self):
        """ use fitting room """
        if self.use_time > 0:
            self.use_time = self.use_time - 1

    def leave(self):
        """ leave fitting room """
        self.inuse = False
        self.queue.dequeue()

    def join_queue(self, item):
        """ join queue """
        self.queue.add(item)
        return


class Person:
    def __init__(self, name, use_time):
        self.name = name
        self.has_room = False
        self.total_use_time = use_time

    def request_fitting_room(self):
        use_time = randint(1, 3)
        if not fitting_room.queue.contains(self.name):
            self.has_room = fitting_room.request(self.name, use_time)
        if not self.has_room and not fitting_room.queue.contains(self.name):
            fitting_room.join_queue(self.name)

    def use(self):
        while fitting_room.can_use():
            fitting_room.use()
            print self.name, " is using the the fitting room"
            self.total_use_time = self.total_use_time -  1
            yield True
        yield False

    def simulate(self):
        if self.has_room == False:
            if self.total_use_time > 0:
                self.request_fitting_room()
            else:
                return
        else:
            turn = self.use()

            if not turn.next():
                print self.name, " has left the fitting room"
                fitting_room.leave()
                self.has_room = False

fitting_room = FittingRoom()
# people using fitting room, for about n times
sam = Person("sam", 4)
sally = Person("sally", 6)
andy = Person("andy", 10)

while True:
    sam.simulate()
    sally.simulate()
    andy.simulate()
