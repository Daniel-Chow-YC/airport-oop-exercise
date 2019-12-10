from flight_trip_class import *
from passenger_plane_data import *

while True:
    print("------------------------------")
    print('Choose an option:')
    print('1 -- Create a Passenger')
    print('2 -- List all flights')
    print('3 -- Add passenger to flight')
    print("------------------------------")

    ui = input('Please choose a number, or exit: ')
    if ui == '1':
        print('You have chosen option 1')
        name = input("What is the passengers' name? ")
        passport_num = input("What is the passengers' passport number? ")
        new_passenger = Passenger(name, passport_num)
        passenger_list.append(new_passenger)
        print(f"The passenger {new_passenger.name} with passport number {new_passenger.passport_num} "
              f"has been successfully created.")
        # print(new_passenger.name)
        # print(new_passenger.passport_num)

    elif ui == '2':
        print('You have chosen option 2')
        print("The flights available by destination are:")
        for flight in flight_list:
            print(flight.destination)

    elif ui == '3':
        print('You have chosen option 3')
        print("The available passengers are:")
        count = 0
        for passenger in passenger_list:
            print(str(count) + " -- " + passenger.name)
            count += 1
        pass_num = int(input("To select a passenger to add to a flight input the appropriate number:"))
        f_counter = 0
        for flight in flight_list:
            print(str(f_counter) + " -- " + flight.destination)
            f_counter += 1
        flight_num = int(input("To select the flight to add the passenger to, input the appropriate number:"))
        flight_list[flight_num].add_passenger(passenger_list[pass_num])
        print(f"{passenger_list[pass_num].name} has been added to the flight to {flight_list[flight_num].destination}.")

    if ui == 'exit':
        break

