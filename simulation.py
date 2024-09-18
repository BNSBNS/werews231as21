from typing import Optional

from car.edison import Edison


class Simulation:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.cars = []
        self.combine_radar = set()

    def add_car(self, car: Edison):
        """Adds a car to the simulation and sets the field boundaries."""
        car.set_road_boundary(self.width, self.height)
        self.cars.append(car)

    def run_simulation(self):
        """Runs the simulation by executing each car's commands step by step."""
        max_steps = max(len(car.commands) for car in self.cars)

        for step in range(max_steps):
            for car in self.cars:
                if step < len(car.commands) and not car.collided:
                    for other_car in self.cars:
                        if other_car != car and (car.x, car.y) == (
                            other_car.x,
                            other_car.y,
                        ):
                            car.collided = True
                            other_car.collided = True
                            break

                if not car.collided:
                    car.execute_command(car.commands[step])

        self.display_results()

    def display_results(self):
        """Display the final positions and statuses of all cars."""
        print("\nFinal Results:")
        for car in self.cars:
            if car.collided:
                print(f"- {car.name}, collided and stopped at ({car.x}, {car.y})")
            else:
                print(
                    f"- {car.name}, ended at ({car.x}, {car.y}) facing {car.direction}"
                )
