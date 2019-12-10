from flight_trip_class import *

passenger1 = Passenger('Joanna Thomson', 'B343123')
passenger2 = Passenger('Birt Kuman', 'B13927')
passenger3 = Passenger('Jane Doe', 'B22927')
passenger_list = []
passenger_list.extend([passenger1, passenger2, passenger3])

new_flight1 = FlightTrip()
new_flight1.add_destination("London")
new_flight2 = FlightTrip()
new_flight2.add_destination("New York")
new_flight3 = FlightTrip()
new_flight3.add_destination("Berlin")

flight_list = []
flight_list.extend([new_flight1, new_flight2, new_flight3])

