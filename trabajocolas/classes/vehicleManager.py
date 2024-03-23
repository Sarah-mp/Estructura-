from models import Vehicle,Test
import random

class Node:
    def __init__(self, value: Vehicle):
        self.value = value
        self.next = None

class VehicleManager:
    def __init__(self):
        self.first_pending = None
        self.last_pending = None
        self.first_tested = None
        self.last_tested = None

    def is_empty(self, queue: str):
        if queue == "pending":
            return self.first_pending is None
        elif queue == "tested":
            return self.first_tested is None

    def enqueue(self, value: Vehicle, queue: str):
        new_node = Node(value)
        if queue == "pending":
            if self.is_empty(queue):
                self.first_pending = new_node
                self.last_pending = new_node
            else:
                self.last_pending.next = new_node
                self.last_pending = new_node
        elif queue == "tested":
            if self.is_empty(queue):
                self.first_tested = new_node
                self.last_tested = new_node
            else:
                self.last_tested.next = new_node
                self.last_tested = new_node

    def add_vehicle(self, vehicle: Vehicle):
        vehicle.tests = self.add_technical_tests(vehicle.type)
        self.enqueue(vehicle, "pending")

    def add_technical_tests(self, vehicle_type: str):
        test_types = {
            'moto': ['frenos', 'luces', 'gases', 'llantas'],
            'carro': ['frenos', 'luces', 'gases', 'llantas'],
            'camion': ['frenos', 'luces', 'aceite', 'aire', 'frenos_de_aire']
        }
        tests = []
        for test_name in test_types.get(vehicle_type, []):
            tests.append(Test(name=test_name, result=False))
        return tests

    # Los demás métodos permanecen igual...
    
    def vehicle_tested(self, tuition: str):
        if not self.is_empty("pending"):
            current = self.first_pending
            previous = None
            while current:
                if current.value.tuition == tuition:
                    if previous:
                        previous.next = current.next
                    else:
                        self.first_pending = current.next
                    if current == self.last_pending:
                        self.last_pending = previous

                    self.enqueue(current.value, "tested")
                    return
                previous = current
                current = current.next
            print(f"Vehículo con matrícula {tuition} no encontrado en la cola de pendientes.")

    def execute_tests_for_vehicle(self):
        if not self.is_empty("pending"):
            vehicle = self.first_pending.value
            for test in vehicle.tests:
                test.result = random.choice([True, False])
            self.vehicle_tested(vehicle.tuition)
            return vehicle
        else:
            print("No hay vehículos pendientes para revisar.")
            return None

    def remove_pending_vehicle(self, tuition: str):
        if not self.is_empty("pending"):
            current = self.first_pending
            previous = None
            while current:
                if current.value.tuition == tuition:
                    if previous:
                        previous.next = current.next
                    else:
                        self.first_pending = current.next
                    if current == self.last_pending:
                        self.last_pending = previous
                    return True
                previous = current
                current = current.next
        return False
vehicle_manager = VehicleManager()