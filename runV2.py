from db_passengers_oop import *
passengers_table = DBPassengers()

while True:
    print("------------------------------")
    print('Choose an option:')
    print('1 -- Create a Passenger')
    print('2 -- List all flights')
    print('3 -- List all passenger details')
    print('4 -- Add passenger to flight')

    print("------------------------------")

    ui = input('Please choose a number, or exit: ')
    if ui == '1':
        print('You have chosen option 1')
        first_name = input("What is the passenger's first name? ")
        last_name = input("What is the passenger's last name? ")
        passport_num = input("What is the passenger's passport number? ")
        passengers_table.create_passenger(first_name, last_name, passport_num)

    elif ui == '2':
        print('You have chosen option 2')
        passengers_table.print_list_all_flights()

    elif ui == '3':
        print('You have chosen option 3')
        data = passengers_table.list_all_passengers()
        while True:
            row = data.fetchone()
            if row is None:
                break
            print(f"ID: {row.PassengerID} // Name: {row.FirstName} {row.LastName} // Passport Number: {row.PassportNumber}")

    elif ui == '4':
        print('You have chosen option 4')
        print("The list of flights available are:")
        passengers_table.print_list_all_flights()
        flight_id = int(input("Which flight would you like to add a passenger to? Please choose by FlightID:  "))
        print("Passengers currently without a flight are:")
        passengers_table.print_list_all_passengers_without_flight()
        pass_id = int(input("Which passenger would you like to add to to this flight? Please choose by their PassengerID: "))
        passengers_table.add_to_flight(pass_id, flight_id)
        print("Your passenger has been added to the flight.")

    elif 'exit' in ui:
        print("Goodbye! Thank You")
        break

    else:
        print("Sorry I didn't quite catch that...")
