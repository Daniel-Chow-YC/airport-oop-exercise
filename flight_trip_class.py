from passenger_class import *
class FlightTrip():
    def __init__(self):
        self.destination = ""
        self.plane = []
        self.origin = ""
        self.passenger_list = []

    def add_destination(self, destination):
        self.destination = destination

    def add_plane(self, plane):
        self.plane.append(plane)

    def add_origin(self, origin):
        self.origin = origin

    def add_passenger(self, passenger):
        self.passenger_list.append(passenger)




