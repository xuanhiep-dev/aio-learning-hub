class MyQueue:
    def __init__(self, capacity):
        self.__capacity = capacity
        self.__queue = []

    def is_full(self):
        if len(self.__queue) == self.__capacity:
            return True
        else:
            return False

    def is_empty(self):
        return len(self.__queue) == 0

    def enqueue(self, value):
        if self.is_full():
            return None
        else:
            self.__queue.append(value)

    def dequeue(self):
        if self.is_empty():
            return None
        else:
            return self.__queue.pop(0)

    def front(self):
        if self.is_empty():
            return None
        else:
            return self.__queue[0]


if __name__ == "__main__":
    queue1 = MyQueue(capacity=5)
    queue1.enqueue(1)
    queue1.enqueue(2)

    print(queue1.is_full())
    print(queue1.front())
    print(queue1.dequeue())
    print(queue1.front())
    print(queue1.dequeue())
    print(queue1.is_empty())
