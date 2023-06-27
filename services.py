from abc import ABC, abstractmethod
from car import Car

class Services(ABC):
    def __init__(self, car_factory):
        self.car_factory = car_factory

    def perform_service(self, engine_type, battery_type):
        car = self.car_factory.create_car(engine_type, battery_type)