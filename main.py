from car.edison import Edison
from simulation import Simulation


def main():
    print("Welcome to Auto Driving Car Simulation!\n")

    width, height = map(
        int,
        input(
            "Please enter the width and height of the simulation field in x y format (e.g., 10 10): "
        ).split(),
    )
    simulation = Simulation(width, height)

    while True:
        print("\nPlease choose from the following options:")
        print("[1] Add a car to field")
        print("[2] Run simulation")
        print("[3] Exit")
        option = input().strip()

        if option == "1":
            car_name = input("Please enter the name of the car: ").strip()
            x, y, direction = input(
                f"Please enter initial position of car {car_name} in x y Direction format (e.g., 1 2 N): "
            ).split()
            x, y = int(x), int(y)
            commands = input(
                f"Please enter the commands for car {car_name} (F, L, R allowed, e.g., FLRFLR): "
            ).strip()
            car = Edison(car_name, x, y, direction, commands, speed=1)
            simulation.add_car(car)

            print("\nYour current list of cars are:")
            for car in simulation.cars:
                print(
                    f"- {car.name}, ({car.x}, {car.y}) {car.direction}, {car.commands}"
                )

        elif option == "2":
            print("\nRunning simulation...")
            simulation.run_simulation()

            print("\nPlease choose from the following options:")
            print("[1] Start over")
            print("[2] Exit")
            restart_option = input().strip()
            if restart_option == "1":
                return main()  # Restart simulation
            else:
                print("Thank you for running the simulation. Goodbye!")
                break


if __name__ == "__main__":
    main()
