from abc import ABC, abstractmethod
from car import Car
from engine import capulet_engine
from engine import willoughby_engine
from engine import sternman_engine


class CarFactory:
    def create_car(self, engine_type, battery_type):
        engine = self._create_engine(engine_type)
        battery = self._create_battery(battery_type)
        return Car(engine, battery)

    def _create_engine(self, engine_type):
        if engine_type == "CapuletEngine":
            return CapuletEngine()
        elif engine_type == "WilloughbyEngine":
            return WilloughbyEngine()
        elif engine_type == "SternmanEngine":
            return SternmanEngine()
        else:
            raise ValueError("Invalid engine type")

    def _create_battery(self, battery_type):
        if battery_type == "NubblerBattery":
            return NubblerBattery()
        elif battery_type == "SpindlerBattery":
            return SpindlerBattery()
        else:
            raise ValueError("Invalid battery type")