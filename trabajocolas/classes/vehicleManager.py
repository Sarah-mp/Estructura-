from collections import deque
from models import Vehicle
import random

class VehicleManager:
    def __init__(self):
        self.vehicles_to_be_tested = deque()  
        self.tested_vehicles = list() 

    def add_vehicle(self, vehicle: Vehicle):
        self.vehicles_to_be_tested.append(vehicle)  

    def vehicle_tested(self, tuition: str):
        found = False
        length = len(self.vehicles_to_be_tested)
        for _ in range(length):
            vehicle = self.vehicles_to_be_tested.popleft()  
            if vehicle.tuition == tuition and not found:
                self.tested_vehicles.append(vehicle)  
                found = True
            else:
                self.vehicles_to_be_tested.append(vehicle)  

    def get_vehicles_to_be_tested(self):
        return list(self.vehicles_to_be_tested)  

    def get_tested_vehicles(self):
        return self.tested_vehicles
    
    def execute_tests_for_vehicle(self):
        if self.vehicles_to_be_tested:
            vehicle = self.vehicles_to_be_tested[0] 
            for test in vehicle.tests:
                test.result = random.choice([True, False])
            self.vehicle_tested(vehicle.tuition) 
            return vehicle 
        else:
            print("No hay vehículos pendientes para revisar.")
            return None
    
    def remove_pending_vehicle(self, tuition: str):
        found = False
        length = len(self.vehicles_to_be_tested)
        for _ in range(length):
            vehicle = self.vehicles_to_be_tested.popleft()
            if vehicle.tuition == tuition and not found:
                found = True 
            else:
                self.vehicles_to_be_tested.append(vehicle)
        return found

vehicle_manager = VehicleManager()