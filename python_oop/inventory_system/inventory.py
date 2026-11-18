"""Typed inventory domain model demonstrating OOP, validation, and persistence."""
from __future__ import annotations

import csv
from dataclasses import dataclass
from decimal import Decimal, InvalidOperation
from pathlib import Path


@dataclass(frozen=True)
class Product:
    sku: str
    name: str
    unit_price: Decimal
    quantity: int

    def __post_init__(self) -> None:
        if not self.sku.strip() or not self.name.strip():
            raise ValueError("SKU and name are required")
        if not self.unit_price.is_finite() or self.unit_price < 0:
            raise ValueError("Unit price must be finite and nonnegative")
        if isinstance(self.quantity, bool) or not isinstance(self.quantity, int) or self.quantity < 0:
            raise ValueError("Quantity must be a nonnegative integer")

    @property
    def stock_value(self) -> Decimal:
        return self.unit_price * self.quantity


class Inventory:
    """Manage products by unique SKU without exposing mutable internal state."""

    def __init__(self, products: list[Product] | None = None) -> None:
        self._items: dict[str, Product] = {}
        for product in products or []:
            self.add(product)

    def add(self, product: Product) -> None:
        if product.sku in self._items:
            raise ValueError(f"Duplicate SKU: {product.sku}")
        self._items[product.sku] = product

    def get(self, sku: str) -> Product:
        return self._items[sku]

    def adjust_stock(self, sku: str, delta: int) -> Product:
        if isinstance(delta, bool) or not isinstance(delta, int):
            raise TypeError("Stock adjustment must be an integer")
        current = self.get(sku)
        next_quantity = current.quantity + delta
        if next_quantity < 0:
            raise ValueError("Insufficient stock")
        updated = Product(current.sku, current.name, current.unit_price, next_quantity)
        self._items[sku] = updated
        return updated

    def total_value(self) -> Decimal:
        return sum((p.stock_value for p in self._items.values()), Decimal("0"))

    def products(self) -> tuple[Product, ...]:
        return tuple(sorted(self._items.values(), key=lambda item: item.sku))

    def save_csv(self, path: str | Path) -> None:
        with Path(path).open("w", encoding="utf-8", newline="") as handle:
            writer = csv.writer(handle)
            writer.writerow(("sku", "name", "unit_price", "quantity"))
            for item in self.products():
                writer.writerow((item.sku, item.name, str(item.unit_price), item.quantity))

    @classmethod
    def from_csv(cls, path: str | Path) -> Inventory:
        with Path(path).open("r", encoding="utf-8-sig", newline="") as handle:
            reader = csv.DictReader(handle)
            if reader.fieldnames != ["sku", "name", "unit_price", "quantity"]:
                raise ValueError("CSV header must be sku,name,unit_price,quantity")
            inventory = cls()
            for line_number, row in enumerate(reader, start=2):
                if None in row or any(value is None for value in row.values()):
                    raise ValueError(f"Malformed CSV row {line_number}")
                try:
                    price = Decimal(row["unit_price"])
                    quantity = int(row["quantity"])
                except (InvalidOperation, ValueError) as exc:
                    raise ValueError(f"Invalid price or quantity on row {line_number}") from exc
                inventory.add(Product(row["sku"], row["name"], price, quantity))
            return inventory


if __name__ == "__main__":
    inventory = Inventory([Product("BOOK-1", "Python Handbook", Decimal("249.50"), 3)])
    inventory.adjust_stock("BOOK-1", -1)
    print(f"Remaining inventory value: {inventory.total_value()}")
