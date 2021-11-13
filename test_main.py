import unittest
from main import Cell


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)

    def test_if_cell_has_0_neighbours_should_die(self):
        cell = Cell(is_living=True)
        cell.update_state(neighbours=0)
        self.assertFalse(cell.is_living)

    def test_if_cell_has_1_neighbouts_should_die(self):
        cell = Cell(is_living=True)
        cell.update_state(neighbours=1)
        self.assertFalse(cell.is_living)

    def test_if_cell_has_2_neighbouts_should_survive(self):
        cell = Cell(is_living=True)
        cell.update_state(neighbours=2)
        self.assertTrue(cell.is_living)
    
    def test_if_cell_has_3_neighbouts_should_survive(self):
        cell = Cell(is_living=True)
        cell.update_state(neighbours=3)
        self.assertTrue(cell.is_living)

    def test_if_cell_has_4_neighbours_should_die(self):
        cell = Cell(is_living=True)
        cell.update_state(neighbours=4)
        self.assertFalse(cell.is_living)


if __name__ == '__main__':
    unittest.main()
