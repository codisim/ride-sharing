from abc import ABC



class Vehicle(ABC):
    def __init__(self, vehicle_type, license_plate, rate):
        self.vehicle_type = vehicle_type
        self.license_plate = license_plate
        self.rate = rate
        
