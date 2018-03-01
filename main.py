# Main file
from read_write import ReadWrite
from vehicle import Vehicle

def main():
    readWrite = ReadWrite()
    ride_description = readWrite.read_file("./resources/b_should_be_easy.in")

    moved_vehicles = []
    time = 0
    initial_vehicle_position = [0, 0]
    initial_vehicle_time = 0

    for ride in ride_description:
        print (distance(ride.ride_start, initial_vehicle_position))


def distance(ride_position, vehicle_position):
    return abs(ride_position[0]-vehicle_position[0])+abs(ride_position[1]-vehicle_position[1])

if __name__ == "__main__":
    main()
