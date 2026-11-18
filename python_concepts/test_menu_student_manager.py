import unittest
from menu_student_manager import StudentManager, main


class StudentTests(unittest.TestCase):
    def test_crud(self):
        manager = StudentManager()
        manager.add(2, "Mira", 89)
        manager.add(1, "Ravi", 75)
        self.assertEqual([s.roll for s in manager.list_all()], [1, 2])
        manager.update(1, "Ravi K", 90)
        self.assertEqual(manager.students[1].marks, 90)
        manager.delete(2)
        self.assertEqual(len(manager.students), 1)

    def test_validation(self):
        manager = StudentManager()
        with self.assertRaises(ValueError):
            manager.add(1, "", 30)
        with self.assertRaises(ValueError):
            manager.add(1, "A", 101)
        manager.add(1, "A", 50)
        with self.assertRaises(ValueError):
            manager.add(1, "B", 60)
        with self.assertRaises(KeyError):
            manager.delete(5)

    def test_menu_exit(self):
        main(input_fn=lambda _: "5", output_fn=lambda _: None)


if __name__ == "__main__":
    unittest.main()
