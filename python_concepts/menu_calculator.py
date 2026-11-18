"""Interactive menu-driven calculator with injectable input and output."""
from decimal import Decimal, InvalidOperation


def calculate(choice, first, second):
    try:
        a, b = Decimal(str(first)), Decimal(str(second))
    except (InvalidOperation, ValueError):
        raise ValueError("invalid number") from None
    if not a.is_finite() or not b.is_finite():
        raise ValueError("numbers must be finite")
    operations = {
        "1": lambda: a + b,
        "2": lambda: a - b,
        "3": lambda: a * b,
        "4": lambda: a / b,
    }
    if choice not in operations:
        raise ValueError("invalid choice")
    if choice == "4" and b == 0:
        raise ZeroDivisionError("cannot divide by zero")
    return operations[choice]()


def main(input_fn=input, output_fn=print):
    while True:
        output_fn("1. Add  2. Subtract  3. Multiply  4. Divide  5. Exit")
        choice = input_fn("Choose: ").strip()
        if choice == "5":
            output_fn("Goodbye!")
            return
        if choice not in {"1", "2", "3", "4"}:
            output_fn("Invalid menu choice")
            continue
        first = input_fn("First number: ")
        second = input_fn("Second number: ")
        try:
            output_fn(str(calculate(choice, first, second)))
        except (ValueError, ZeroDivisionError) as exc:
            output_fn(str(exc))


if __name__ == "__main__":
    main()
