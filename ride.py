
from datetime import datetime
    
    
    
class Ride:
    def __init__(self, start_location, end_location, vehicle):
        self.start_location = start_location
        self.end_location = end_location
        self.driver = None
        self.rider = None
        self.start_time = None
        self.end_time = None
        self.estimated_fare = self.calculate_fare(vehicle.vehicle_type)
        self.vehicle = vehicle
        
    def set_driver(self, driver):
        self.driver = driver
        
    
    def start_ride(self):
        self.start_time = datetime.now()
    
    def end_ride(self):
        self.end_time = datetime.now()
        self.rider.wallet -= self.estimated_fare
        self.driver.wallet += self.estimated_fare
        
        
    def calculate_fare(self, vichel):
        distance = 10
        fare_per_kel = {
            'car': 40,
            'bike': 20,
            'cng': 25
        }
        
        return distance * fare_per_kel.get(vichel)
        
        
    def __repr__(self):
        return f"Ride details. Started from {self.start_location} to {self.end_location}"
    
    


class RideRequest:
    def __init__(self, rider, end_location):
        self.rider = rider
        self.end_location = end_location 
        
        

class RideMatching:
    def __init__(self, drivers):
        self.avaiable_drivers = drivers
        
    def find_request(self, ride_request):
        if len(self.avaiable_drivers) > 0:
            print("Looking for drivers............")
            driver = self.avaiable_drivers[0]
            ride = Ride(ride_request.rider.current_request, ride_request.end_location)
            
            driver.accept_ride(ride)
            return ride
        
        
        
        
class RideSharing:
    def __init__(self, company_name):
        self.company_name = company_name
        self.riders = []
        self.drivers = []
        self.rides = []
        
    def add_rider(self, rider):
        self.riders.append(rider)

    def add_driver(self, driver):
        self.drivers.append(driver)
        
    def __str__(self):
        return f"Company Name {self.company_name} with riders: {len(self.riders)} and drivers: {len(self.drivers)}"
    
    
    