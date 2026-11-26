import tempfile
import unittest
from decimal import Decimal
from pathlib import Path

from inventory import Inventory, Product


class InventoryTests(unittest.TestCase):
    def setUp(self):
        self.inventory = Inventory([Product("A", "Notebook", Decimal("25.50"), 4)])

    def test_stock_value(self):
        self.assertEqual(self.inventory.get("A").stock_value, Decimal("102.00"))

    def test_adjust_stock(self):
        item = self.inventory.adjust_stock("A", -2)
        self.assertEqual(item.quantity, 2)
        self.assertEqual(self.inventory.total_value(), Decimal("51.00"))

    def test_insufficient_stock_keeps_original(self):
        with self.assertRaises(ValueError):
            self.inventory.adjust_stock("A", -5)
        self.assertEqual(self.inventory.get("A").quantity, 4)

    def test_duplicate_sku(self):
        with self.assertRaises(ValueError):
            self.inventory.add(Product("A", "Other", Decimal("1"), 1))

    def test_invalid_price_and_quantity(self):
        with self.assertRaises(ValueError):
            Product("X", "Bad", Decimal("-1"), 0)
        with self.assertRaises(ValueError):
            Product("X", "Bad", Decimal("NaN"), 0)
        with self.assertRaises(ValueError):
            Product("X", "Bad", Decimal("1"), -1)

    def test_csv_round_trip(self):
        with tempfile.TemporaryDirectory() as directory:
            file = Path(directory) / "inventory.csv"
            self.inventory.save_csv(file)
            restored = Inventory.from_csv(file)
        self.assertEqual(restored.products(), self.inventory.products())

    def test_bad_csv_header(self):
        with tempfile.TemporaryDirectory() as directory:
            file = Path(directory) / "bad.csv"
            file.write_text("wrong,header\na,b\n", encoding="utf-8")
            with self.assertRaises(ValueError):
                Inventory.from_csv(file)

    def test_unknown_sku(self):
        with self.assertRaises(KeyError):
            self.inventory.get("missing")


if __name__ == "__main__":
    unittest.main()
