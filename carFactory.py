from abc import ABC, abstractmethod
from car import Car
from engine.capulet_engine import capulet_engine
from engine.willoughby_engine import willoughby_engine
from engine.sternman_engine import sternman_engine
from battery.nubblerbattery import nubblerbattery
from battery.spindlerbattery import spindlerbattery


class CarFactory(ABC):
    def create_car(self, engine_type, battery_type):
        engine = self._create_engine(engine_type)
        battery = self._create_battery(battery_type)
        return Car(engine, battery)

    def _create_engine(self, engine_type):
        if engine_type == "CapuletEngine":
            return capulet_engine()
        elif engine_type == "WilloughbyEngine":
            return willoughby_engine()
        elif engine_type == "SternmanEngine":
            return sternman_engine()
        else:
            raise ValueError("Invalid engine type")

    def _create_battery(self, battery_type):
        if battery_type == "NubblerBattery":
            return nubblerbattery()
        elif battery_type == "SpindlerBattery":
            return spindlerbattery()
        else:
            raise ValueError("Invalid battery type")