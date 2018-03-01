class RideDescription(object):
    def __init__(self, rideId, a, b, x, y, s, f):
        self.id = rideId
        self.ride_start = [a, b]
        self.destination_stop = [x, y]
        self.start = s
        self.finish = f
