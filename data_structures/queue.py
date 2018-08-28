class Queue(object):
    """
    First in first out / last in last out.

    Ideal for:
    - Processing data as it comes in sequentially (e.g. processing requests to web server)
    """

    def __init__(self):
        self.queue = []

    def enqueue(self, data):
        self.queue.insert(data, 0)

    def dequeue(self):
        return self.queue.pop(0)

    def is_empty(self):
        return self.size() <= 0

    def size(self):
        return len(self.queue)
