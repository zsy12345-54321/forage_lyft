from datetime import datetime
from car import Car
from engine.capulet_engine import CapuletEngine


class Calliope(Car):
    def __init__(self, last_service_date, engine, battery):
        super().__init__(last_service_date, engine, battery)

    def needs_service(self):
        return self.needs_service()