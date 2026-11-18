"""Interactive bank account menu using the BankAccount class."""
from oop_bank import BankAccount


def main(input_fn=input, output_fn=print):
    account = BankAccount("Customer")
    while True:
        output_fn("1.Deposit 2.Withdraw 3.Balance 4.History 5.Exit")
        choice = input_fn("Choice: ").strip()
        try:
            if choice == "1":
                output_fn(f"Balance: {account.deposit(input_fn('Amount: '))}")
            elif choice == "2":
                output_fn(f"Balance: {account.withdraw(input_fn('Amount: '))}")
            elif choice == "3":
                output_fn(f"Balance: {account.balance}")
            elif choice == "4":
                for kind, amount in account.transactions:
                    output_fn(f"{kind}: {amount}")
            elif choice == "5":
                output_fn("Goodbye!")
                return
            else:
                output_fn("Invalid choice")
        except ValueError as exc:
            output_fn(f"Error: {exc}")


if __name__ == "__main__":
    main()
