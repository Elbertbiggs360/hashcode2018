class Ride(object):
    def __init__(self, a, b, x, y, s, f):
        self.ride_start = [a, b]
        self.destination_stop = [x, y]
        self.earliest_start_step = s
        self.latest_finish_step = f

    def setId(self, rideId):
        ''' Sets Ride ID'''
        self.rideId = rideId
