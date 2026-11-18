import unittest
from decimal import Decimal
from menu_calculator import calculate, main


class CalculatorTests(unittest.TestCase):
    def test_operations(self):
        self.assertEqual(calculate("1", "2.5", "1.2"), Decimal("3.7"))
        self.assertEqual(calculate("2", 5, 3), 2)
        self.assertEqual(calculate("3", 5, 3), 15)
        self.assertEqual(calculate("4", 6, 2), 3)

    def test_errors(self):
        with self.assertRaises(ZeroDivisionError):
            calculate("4", 5, 0)
        with self.assertRaises(ValueError):
            calculate("9", 1, 2)

    def test_menu_exit(self):
        output = []
        main(input_fn=lambda prompt: "5", output_fn=output.append)
        self.assertIn("Goodbye!", output)


if __name__ == "__main__":
    unittest.main()
