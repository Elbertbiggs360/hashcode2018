from rides import Ride

class ReadWrite(object):

    def read_file(self, file_name):
        fo = open(file_name, "r")
        lines = fo.readlines()
        i = 0
        self.rides = []
        for line in lines:
            auto_increment_id = 0
            if(i == 0):
                p = line.split(' ')
                self.rows = int(p[0])
                self.columns = int(p[1])
                self.vehicles = int(p[2])
                self.rides = int(p[3])
                self.bonus = int(p[4])
                self.steps = int(p[5])
            else:
                p = line.split(' ')
                ride = Ride(int(p[0]), int(p[1]), int(p[2]), int(p[3]), int(p[4]), int(p[5]))
                ride.setId(auto_increment_id)
                self.rides.append(ride)
            i += 1

        self.rides = sorted(self.rides, key=lambda rides: rides.start)
        return self.rides

