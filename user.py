import hashlib
from random import random, randint
from brta import BRTA
from vehicles import Bike, Car, Cng
from ride_manager import uber

license_authority = BRTA()

class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
        pwd_encrypted = hashlib.md5(password.encode()).hexdigest()
        with open('users.txt', 'a+') as file:
            # lines = file.readlines()
            # for line in lines:
            #     if email not in line:
            file.write(f'{email} {pwd_encrypted}\n')
        file.close()
        print(self.name, "User created")

    @staticmethod
    def log_in(email, password):
        with open('users.txt', 'r') as file:
            lines = file.readlines()
            for line in lines:
                if email in line:
                    stored_password = line.split(' ')[1]
        file.close()

        hashed_password = hashlib.md5(password.encode()).hexdigest()
        if hashed_password == stored_password:
            print("Valid user")
            return True
        else:
            print("Invalid user")
            return False

class Rider(User):
    def __init__(self, name, email, password, location, balance):
        self.location = location
        self.balance = balance
        super().__init__(name, email, password)

    def set_location(self, location):
        self.location = location
    def get_location(self):
        return self.location
    def request_trip(self, destination):
        pass
    def start_a_trip(self, fare):
        self.balance -= fare

class Driver(User):
    def __init__(self, name, email, password, location, license):
        super().__init__(name, email, password)
        self.location = location
        self.license = license
        self.valid_driver = license_authority.validate_license(email, license)
        self.earning = 0

    def take_driving_test(self):
        result = license_authority.take_driving_test(self.email)
        if result == False:
            print("Sorry you failed! try again")
        else:
            self.license = result
            self.valid_driver = True
    
    def register_a_vehicle(self, vehicle_type, license_plate, rate):
        if self.valid_driver is True:
            new_vehicle = None
            if vehicle_type == 'car':
                new_vehicle = Car(vehicle_type, license_plate, rate, self)
                uber.add_a_vehicle(vehicle_type, new_vehicle)
            elif vehicle_type == 'bike':
                new_vehicle = Bike(vehicle_type, license_plate, rate, self)
                uber.add_a_vehicle(vehicle_type, new_vehicle)
            else:
                new_vehicle = Cng(vehicle_type, license_plate, rate, self)
                uber.add_a_vehicle(vehicle_type, new_vehicle)
        else:
            print("Your are not a valid driver")
    
    def start_a_trip(self, destination, fare):
        self.earning += fare
        self.location = destination


rider1 = Rider('rider1', 'rider1@gamil.com', 'rider1', randint(0, 30), 5000)
rider2 = Rider('rider2', 'rider2@gamil.com', 'rider2', randint(0, 30), 5000)
rider3 = Rider('rider3', 'rider3@gamil.com', 'rider3', randint(0, 30), 5000)

driver1 = Driver('driver1', 'driver1@gmail.com', 'driver1', randint(0, 30), 5645)
driver1.take_driving_test()
driver1.register_a_vehicle('car', 1245, 10)

driver2 = Driver('driver2', 'driver2@gmail.com', 'driver2', randint(0, 30), 5645)
driver2.take_driving_test()
driver2.register_a_vehicle('car', 3245, 12)

driver3 = Driver('driver3', 'driver3@gmail.com', 'driver3', randint(0, 30), 5645)
driver3.take_driving_test()
driver3.register_a_vehicle('car', 4568, 14)

driver4 = Driver('driver4', 'driver4@gmail.com', 'driver4', randint(0, 30), 5645)
driver4.take_driving_test()
driver4.register_a_vehicle('car', 4558, 14)

print(uber.get_available_cars())
uber.find_a_vehicles(rider1, 'car', 90)

# hero = User('x', 'xyz@gmail.com', 'abcxyz')
# hero.log_in('xyz@gmail.com', 'abcxyz')

# xyz = Driver('xyz', "xyz@gmail.com", '123456', 'dhaka', 4554)

# result = license_authority.validate_license(xyz.email, xyz.license)
# print(result)

# xyz.take_driving_test()
# result = license_authority.validate_license(xyz.email, xyz.license)
# print(result)



