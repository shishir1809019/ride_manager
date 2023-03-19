class RideManager:
    def __init__(self):
        print('Ride manager activated')
        self.__income = 0
        self.__trip_history = []
        self.__availableCars = []
        self.__availableBikes = []
        self.__availableCng = []
    
    def add_a_vehicle(self, vehicle_type, vehicle):
        if vehicle_type == 'car':
            self.__availableCars.append(vehicle)
        elif vehicle_type == 'bike':
            self.__availableBikes.append(vehicle)
        else:
            self.__availableCng.append(vehicle)
    
    def get_available_cars(self):
        return self.__availableCars
    
    def total_income(self):
        return self.__income
    def trip_history(self):
        return self.__trip_history

    def find_a_vehicles(self, rider, vehicle_type, destination):
        if vehicle_type == 'car':
            vehicles = self.__availableCars
        elif vehicle_type == 'bike':
            vehicles = self.__availableBikes
        else:
            vehicles = self.__availableCng
        if len(vehicles) == 0:
            print(f'Sorry! no {vehicles} is available')
            return False
        for car in vehicles:
            print("potential", rider.location, car.driver.location)
            if abs(rider.location - car.driver.location) < 10:
                distance = abs(rider.location - destination)
                fare = distance * car.rate
                if rider.balance < fare:
                    print('You do not have enough money for this trip.', fare, rider.balance)
                    return False
                if car.status == 'available':
                    # car.status = 'unavailable'
                    trip_info = f'Match {vehicle_type} for {rider.name} for: {fare} with {car.driver.name} started: {rider.location} to {destination}'
                    print(trip_info)
                    self.__trip_history.append(trip_info)
                    vehicles.remove(car)
                    rider.start_a_trip(fare, trip_info)
                    car.driver.start_a_trip(rider.location, destination, fare*0.8, trip_info)
                    self.__income += fare*0.2
                    return True
uber = RideManager() 
