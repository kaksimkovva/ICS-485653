from abc import ABCMeta, abstractmethod, abstractproperty, ABC


class Vehicle:
    __metaclass__ = ABCMeta

    def __init__(self, vehicle_type: str, vehicle_cost: str, vehicle_speed: int, vehicle_year: int):
        self.vehicle_type = vehicle_type
        self.cost = vehicle_cost
        self.speed = vehicle_speed
        self.year = vehicle_year

    @property
    @abstractmethod
    def height(self, x: int, y: int, z: int):
        print(self.vehicle_type)
        print(x, y, z)

    @property
    @abstractmethod
    def passengers_count(self, count: int):
        print(self.vehicle_type)
        print(count)

    @property
    @abstractmethod
    def home_port(self, port: str):
        print(self.vehicle_type)
        print(port)


class Aircraft(Vehicle, ABC):

    def height(self, x, y, z):
        print(self.vehicle_type)
        print(x, y, z)

    def passengers_count(self, count):
        print(self.vehicle_type)
        print(count)


class Ship(Vehicle, ABC):
    def passengers_count(self, count):
        print(self.vehicle_type)
        print(count)

    def home_port(self, port):
        print(self.vehicle_type)
        print(port)


aircraft = Aircraft("Flick", "1202", 1200, 1000)
aircraft.height(1, 2, 3)