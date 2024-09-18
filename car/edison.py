from collections import deque

from car.carbase import CarBase


class Edison(CarBase):
    DIRECTION_VECTORS = {"N": (0, 1), "S": (0, -1), "E": (1, 0), "W": (-1, 0)}
    ROTATE_LEFT = {"N": "W", "W": "S", "S": "E", "E": "N"}
    ROTATE_RIGHT = {"N": "E", "E": "S", "S": "W", "W": "N"}
    COMMAND_MAP = {"F": "move_forward", "L": "rotate_left", "R": "rotate_right"}

    def __init__(
        self, name: str, x: int, y: int, direction: str, commands: str, speed: int = 1
    ) -> None:
        super().__init__(name, x, y, direction, commands, speed)
        self.width: int = 0
        self.height: int = 0
        self.radar = deque()  # Tracks positions to detect collisions
        self.collided = False

    def direction_vectors(self):
        return Edison.DIRECTION_VECTORS[self.direction]

    def command_map(self):
        return Edison.COMMAND_MAP[self.direction]()

    def rotate_left(self):
        if not self.collided:
            self.direction = Edison.ROTATE_LEFT[self.direction]

    def rotate_right(self):
        if not self.collided:
            self.direction = Edison.ROTATE_RIGHT[self.direction]

    def set_road_boundary(self, width, height):
        self.width = width
        self.height = height

    def is_out_of_bound(self, new_x, new_y):
        return not (0 <= new_x < self.width and 0 <= new_y < self.height)

    def move_forward(self):
        if not self.collided:
            # Get the next position
            new_x, new_y = self.get_next_position()
            # Check if the new position is out of bounds
            if self.is_out_of_bound(new_x, new_y):
                self.collided = True
                print(f"{self.name} moved out of bounds at ({new_x}, {new_y})!")
                return

            # Check if the new position is already occupied (collision detection)
            if (new_x, new_y) in self.radar:
                self.collided = True
                print(f"{self.name} collided with itself at ({new_x}, {new_y})!")
                return

            # Remove the car's current position from the radar
            # self.radar.discard((self.x, self.y))
            if self.radar:
                self.radar.pop()

            # No collision, update the position to the new one
            self.x = new_x
            self.y = new_y

            # Add the new position to the radar
            self.radar.append((self.x, self.y))

    def get_next_position(self):
        dx, dy = Edison.DIRECTION_VECTORS[self.direction]
        new_x = self.x + dx * self.speed
        new_y = self.y + dy * self.speed
        return new_x, new_y

    def set_speed(self, speed: int):
        self.speed = speed

    def execute_command(self, command: str):
        if command in Edison.COMMAND_MAP:
            getattr(self, Edison.COMMAND_MAP[command])()
