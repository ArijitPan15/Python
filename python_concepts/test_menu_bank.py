import unittest
from menu_bank import main


class BankMenuTests(unittest.TestCase):
    def test_session(self):
        answers = iter(["1", "100", "2", "25", "3", "5"])
        output = []
        main(input_fn=lambda _: next(answers), output_fn=output.append)
        self.assertIn("Balance: 75", output)
        self.assertEqual(output[-1], "Goodbye!")

    def test_invalid_choice(self):
        answers = iter(["bad", "5"])
        output = []
        main(input_fn=lambda _: next(answers), output_fn=output.append)
        self.assertIn("Invalid choice", output)


if __name__ == "__main__":
    unittest.main()
