import unittest

from car.edison import Edison
from simulation.simulation import Simulation


class TestCarSimulation(unittest.TestCase):
    def setUp(self):
        """Setup the simulation field and other common parameters."""
        self.simulation = Simulation(10, 10)  # A common 10x10 field for most tests

    def test_car_initial_position(self):
        """Test the car's initial position and direction."""
        car = Edison("A", 1, 2, "N", "")
        self.assertEqual(car.x, 1)
        self.assertEqual(car.y, 2)
        self.assertEqual(car.direction, "N")

    def test_car_movement_forward(self):
        """Test that the car moves forward correctly based on its direction."""
        car = Edison("A", 1, 1, "N", "F")
        # car.execute_command("F")
        self.simulation.add_car(car)
        self.simulation.run_simulation()
        self.assertEqual(car.x, 1)
        self.assertEqual(car.y, 2)  # Moving north should increase the y-coordinate

    def test_car_turn_left(self):
        """Test that the car turns left correctly."""
        car = Edison("A", 1, 1, "N", "L")
        # car.execute_command("L")
        self.simulation.add_car(car)
        self.simulation.run_simulation()
        self.assertEqual(
            car.direction, "W"
        )  # After turning left from North, direction should be West

    def test_car_turn_right(self):
        """Test that the car turns right correctly."""
        car = Edison("A", 1, 1, "N", "R")
        # car.execute_command("R")
        self.simulation.add_car(car)
        self.simulation.run_simulation()
        self.assertEqual(
            car.direction, "E"
        )  # After turning right from North, direction should be East

    def test_car_movement_out_of_bounds(self):
        """Test that the car stops moving when it reaches the boundary."""
        car = Edison("A", 9, 9, "N", "F")  # Already at the top boundary
        self.simulation.add_car(car)
        self.simulation.run_simulation()

        # Check that the car did not go out of bounds and correctly stopped
        self.assertEqual(car.x, 9)
        self.assertEqual(car.y, 9)
        self.assertTrue(car.collided)

    def test_car_collision(self):
        """Test if two cars collide at the same position."""
        car_a = Edison("A", 1, 1, "N", "FF")  # Moves forward twice
        car_b = Edison("B", 1, 3, "S", "FF")  # Moves south twice (into car A's path)

        self.simulation.add_car(car_a)
        self.simulation.add_car(car_b)
        self.simulation.run_simulation()

        print(f"car a col {car_a.collided}")
        print(f"car b col {car_b.collided}")

        # Both cars should have collided at (1, 2)
        self.assertTrue(car_a.collided)
        self.assertTrue(car_b.collided)

    def test_no_collision(self):
        """Test that two cars do not collide when they move on different but nearby paths."""

        car_a = Edison("A", 1, 1, "N", "FF")  # Moves forward twice to (1, 3)
        car_b = Edison("B", 2, 2, "N", "FF")  # Moves forward twice to (2, 3)
        self.simulation.add_car(car_a)
        self.simulation.add_car(car_b)
        self.simulation.run_simulation()

        self.assertFalse(car_a.collided)
        self.assertFalse(car_b.collided)

    def test_car_out_of_bounds_prevention(self):
        """Test that the car does not move out of bounds when the next move is invalid."""
        car = Edison("A", 9, 9, "N", "F")  # Heading towards out-of-bounds
        car.set_road_boundary(10, 10)  # Set the boundaries for the car
        # car.execute_command("F")  # This move would take it out of bounds

        self.simulation.add_car(car)
        self.simulation.run_simulation()

        print(f"car col {car.collided}  {car.x} {car.y}")
        self.assertEqual(car.x, 9)
        self.assertEqual(car.y, 9)
        self.assertTrue(car.collided)


if __name__ == "__main__":
    # unittest.main(defaultTest='TestCarSimulation.test_car_movement_forward')

    # unittest.main(defaultTest='TestCarSimulation.test_car_collision')
    unittest.main()
