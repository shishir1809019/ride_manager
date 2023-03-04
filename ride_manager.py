class RideManager:
    def __init__(self):
        print('Ride manager activated')
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

    def find_a_vehicles(self, rider, vehicle_type, destination):
        if vehicle_type == 'car':
            if len(self.__availableCars) == 0:
                print('Sorry! no car is available')
                return False
            for car in self.__availableCars:
                print("potential", rider.location, car.driver.location)
                if abs(rider.location - car.driver.location) < 10:
                    print('Find a match for you')
                    return True


uber = RideManager()
