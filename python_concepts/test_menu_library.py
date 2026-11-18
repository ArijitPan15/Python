import unittest
from menu_library import main


class LibraryMenuTests(unittest.TestCase):
    def test_lending_cycle(self):
        answers = iter(["1", "123", "Python", "Ada", "2", "123", "3", "123", "4", "5"])
        output = []
        main(input_fn=lambda _: next(answers), output_fn=output.append)
        self.assertIn("Book added", output)
        self.assertIn("Borrowed: Python", output)
        self.assertIn("Book returned", output)
        self.assertIn("123: Python by Ada", output)


if __name__ == "__main__":
    unittest.main()
