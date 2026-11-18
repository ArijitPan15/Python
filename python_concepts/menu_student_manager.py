"""Menu-driven student records, stored in memory."""
from dataclasses import dataclass


@dataclass
class Student:
    roll: int
    name: str
    marks: float


class StudentManager:
    def __init__(self):
        self.students = {}

    def add(self, roll, name, marks):
        roll, marks = int(roll), float(marks)
        if roll <= 0 or roll in self.students:
            raise ValueError("roll must be positive and unique")
        if not name.strip() or not 0 <= marks <= 100:
            raise ValueError("invalid name or marks")
        self.students[roll] = Student(roll, name.strip(), marks)

    def update(self, roll, name, marks):
        roll, marks = int(roll), float(marks)
        if roll not in self.students:
            raise KeyError(roll)
        if not name.strip() or not 0 <= marks <= 100:
            raise ValueError("invalid name or marks")
        self.students[roll] = Student(roll, name.strip(), marks)

    def delete(self, roll):
        return self.students.pop(int(roll))

    def list_all(self):
        return [self.students[roll] for roll in sorted(self.students)]


def main(input_fn=input, output_fn=print):
    manager = StudentManager()
    while True:
        output_fn("1.Add 2.List 3.Update 4.Delete 5.Exit")
        choice = input_fn("Choice: ").strip()
        if choice == "5":
            return
        try:
            if choice in ("1", "3"):
                roll = input_fn("Roll: ")
                name = input_fn("Name: ")
                marks = input_fn("Marks: ")
                if choice == "1":
                    manager.add(roll, name, marks)
                else:
                    manager.update(roll, name, marks)
                output_fn("Saved")
            elif choice == "2":
                for student in manager.list_all():
                    output_fn(f"{student.roll}: {student.name} ({student.marks:g})")
            elif choice == "4":
                manager.delete(input_fn("Roll: "))
                output_fn("Deleted")
            else:
                output_fn("Invalid choice")
        except (ValueError, KeyError) as exc:
            output_fn(f"Error: {exc}")


if __name__ == "__main__":
    main()
