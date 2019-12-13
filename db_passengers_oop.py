from db_connect_oop import *


class DBPassengers(MSDBConnection):

    def __sql_query(self, sql_query):
        return self.cursor.execute(sql_query)

    # create a passenger
    def create_passenger(self, first_name, last_name, passport_num):
        query = f"INSERT INTO Passengers (FirstName, LastName, PassportNumber) VALUES ('{first_name}', '{last_name}', '{passport_num}' )"
        data_to_insert = self.__sql_query(query)
        self.docker_airport.commit()
        return data_to_insert

    # list all flights
    def list_all_flights(self):
        query = f"SELECT * FROM Flights;"
        data = self.__sql_query(query)
        return data

    def list_all_passengers(self):
        query = f"SELECT * FROM Passengers ORDER BY LastName;"
        data = self.__sql_query(query)
        return data

    def add_to_flight(self, pass_id, flight_id):
        query = f"UPDATE Passengers SET FlightID = {flight_id} WHERE PassengerID = {pass_id}"
        data = self.__sql_query(query)
        self.docker_airport.commit()
        return data

    def print_list_all_flights(self):
        data = DBPassengers.list_all_flights(self)
        while True:
            row = data.fetchone()
            if row is None:
                break
            print(f"FlightID: {row.FlightID} - {row.Origin} to {row.Destination}")

    def list_all_passengers_without_flight(self):
        query = f"SELECT * FROM Passengers WHERE FlightID IS Null ORDER BY LastName;"
        data = self.__sql_query(query)
        return data

    def print_list_all_passengers_without_flight(self):
        data = DBPassengers.list_all_passengers_without_flight(self)
        while True:
            row = data.fetchone()
            if row is None:
                break
            print(f"ID: {row.PassengerID} // Name: {row.FirstName} {row.LastName} // Passport Number: {row.PassportNumber}")





