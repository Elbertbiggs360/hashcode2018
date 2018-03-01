from ride_description import RideDescription

class ReadWrite(object):

    def read_file(self, file_name):
        fo = open(file_name, "r")
        lines = fo.readlines()
        i = 0
        self.ride_description = []
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
                self.ride_description.append(
                    RideDescription(
                        auto_increment_id, 
                        int(p[0]), 
                        int(p[1]), 
                        int(p[2]), 
                        int(p[3]), 
                        int(p[4]), 
                        int(p[5])
                    )
                )
            i += 1

        self.ride_description = sorted(self.ride_description, key=lambda ride_description: ride_description.start)
        return self.ride_description

