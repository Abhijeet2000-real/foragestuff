class CarSystem:
    def __init__(self):
        self.cars = []

    def add_car(self, car):
        self.cars.append(car)

    def remove_car(self, car):
        self.cars.remove(car)

    def get_service(self, car):
        # Logic for retrieving service details for a specific car
        pass


class Car:
    def __init__(self, car_model, battery, engine, tire):
        self.car_model = car_model
        self.battery = battery
        self.engine = engine
        self.tire = tire


class Service:
    def __init__(self, service_criteria, oil_change_interval, tire_rotation_interval, other_services):
        self.service_criteria = service_criteria
        self.oil_change_interval = oil_change_interval
        self.tire_rotation_interval = tire_rotation_interval
        self.other_services = other_services


class Battery:
    def __init__(self, type, capacity, brand, other_specs):
        self.type = type
        self.capacity = capacity
        self.brand = brand
        self.other_specs = other_specs


class Engine:
    def __init__(self, type, horsepower, model, other_specs):
        self.type = type
        self.horsepower = horsepower
        self.model = model
        self.other_specs = other_specs


class Tire:
    def __init__(self, type, size, brand, other_specs):
        self.type = type
        self.size = size
        self.brand = brand
        self.other_specs = other_specs
