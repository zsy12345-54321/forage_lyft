from datetime import datetime

from engine.willoughby_engine import WilloughbyEngine
from battery.Spindler_battery import SpindlerBattery
from car import Car

class Glissade(Car):
    def needs_service(self):
        return super().needs_service()