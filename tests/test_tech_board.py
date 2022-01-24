import unittest

from gaia_project.tech_board import TechBoard


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.tb = TechBoard()

    def test_something(self):
        self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
