from passenger_class import *
from plane_class import *
from flight_trip_class import *


def test_passenger():
    assert Passenger('Joanna Thomson', 'B343123').name == 'Joanna Thomson'
    assert Passenger('Birt Kuman', 'B13927').passport_num == 'B13927'

def test_plane():
    assert Plane('123').plane_num == '123'
    assert Plane('234').plane_num == '234'

def test_flight_trip_initialisation():
    # setup
    new_flight = FlightTrip()
    # assertion
    assert isinstance(new_flight, FlightTrip)

def test_flight_trip_add_destination():
    # setup
    new_flight = FlightTrip()
    new_flight.add_destination("LA")
    # assertion
    assert new_flight.destination == "LA"
    new_flight.add_destination('NYC')
    assert new_flight.destination == 'NYC'

def test_flight_trip_add_plane():
    new_plane = Plane("123")
    new_flight = FlightTrip()
    new_flight.add_plane(new_plane)
    assert new_plane in new_flight.plane

def test_flight_trip_add_origin():
    new_flight = FlightTrip()
    new_flight.add_origin("UK")
    assert new_flight.origin == "UK"
    new_flight.add_origin('US')
    assert new_flight.origin == 'US'

def test_flight_trip_add_passenger():
    new_passenger = Passenger('Joanna Thomson', 'B343123')
    new_flight = FlightTrip()
    new_flight.add_passenger(new_passenger)
    assert new_passenger in new_flight.passenger_list




