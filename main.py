# Main file
from read_write import ReadWrite

def main():
    readWrite = ReadWrite()
    ride_description = readWrite.read_file("./resources/b_should_be_easy.in")
    # for ride in ride_description:
    #     print( ride.start )

    moved_vehicles = []
    time = 0

    for ride in ride_description:
        


if __name__ == "__main__":
    main()
