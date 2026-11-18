# Python OOP: Inventory and CSV Persistence

An educational object-oriented programming project using only Python's standard library.

- **Encapsulation:** `Inventory` manages its internal SKU-to-product dictionary.
- **Data classes:** immutable `Product` values with validation.
- **Business logic:** add products, change inventory, prevent negative stock.
- **Precision:** `decimal.Decimal` for accurate base-10 prices.
- **Persistence:** import/export CSV with a defined schema and validation.
- **Tests:** unit coverage for stock adjustments, invalid inputs, and round trips.

Run the example:

```bash
python inventory.py
```

Run the tests from this folder:

```bash
python -m unittest discover -s . -p 'test_*.py' -v
```

This is a single-user, in-memory teaching example rather than a transactional warehouse backend.
