import unittest
from datetime import datetime
from car import (
    CapuletEngine,
    SternmanEngine,
    WilloughbyEngine,
    NubblerBattery,
    SpindlerBattery,
)


class TestCapuletEngine(unittest.TestCase):
    def setUp(self):
        last_service_date = datetime(2023, 1, 1)
        current_mileage = 50000
        last_service_mileage = 40000
        self.capulet_engine = CapuletEngine(last_service_date, current_mileage, last_service_mileage)

    def test_needs_service(self):
        self.assertTrue(self.capulet_engine.needs_service())


class TestSternmanEngine(unittest.TestCase):
    def setUp(self):
        last_service_date = datetime(2023, 1, 1)
        warning_light_is_on = True
        self.sternman_engine = SternmanEngine(last_service_date, warning_light_is_on)

    def test_needs_service(self):
        self.assertTrue(self.sternman_engine.needs_service())


class TestWilloughbyEngine(unittest.TestCase):
    def setUp(self):
        last_service_date = datetime(2023, 1, 1)
        current_mileage = 70000
        last_service_mileage = 50000
        self.willoughby_engine = WilloughbyEngine(last_service_date, current_mileage, last_service_mileage)

    def test_needs_service(self):
        self.assertTrue(self.willoughby_engine.needs_service())


class TestNubblerBattery(unittest.TestCase):
    def setUp(self):
        self.nubbler_battery = NubblerBattery()

    def test_charge(self):
        # Add specific test cases for charging behavior of NubblerBattery
        pass


class TestSpindlerBattery(unittest.TestCase):
    def setUp(self):
        self.spindler_battery = SpindlerBattery()

    def test_charge(self):
        # Add specific test cases for charging behavior of SpindlerBattery
        pass


if __name__ == "__main__":
    unittest.main()
