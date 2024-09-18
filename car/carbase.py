from abc import ABC, abstractmethod


class CarBase(ABC):
    def __init__(
        self, name: str, x: int, y: int, direction: str, commands: str, speed: int = 1
    ) -> None:
        self.name = name
        self.x = x
        self.y = y
        self.direction = direction
        self.commands = commands
        self.speed = speed

    @abstractmethod
    def direction_vectors(self):
        pass

    @abstractmethod
    def command_map(self):
        pass

    @abstractmethod
    def rotate_left(self):
        pass

    @abstractmethod
    def rotate_right(self):
        pass

    @abstractmethod
    def move_forward(self):
        pass

    @abstractmethod
    def set_speed(self, speed: int):
        pass

    @abstractmethod
    def execute_command(self, command: str):
        pass
