class RideDescription(object):
    def __init__(self, a, b, x, y, s, f):
        self.ride = [a, b]
        self.destination = [x, y]
        self.start = s
        self.finish = f
