import csv
import os
from project import add_transaction, view_summary_by_category

def test_add_transaction(monkeypatch):
    inputs = iter(["2024-12-01", "Food", "Lunch", "-12.5"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Remove the file if it exists for testing
    if os.path.exists("transactions.csv"):
        os.remove("transactions.csv")

    add_transaction()

    with open("transactions.csv", "r") as file:
        reader = csv.reader(file)
        rows = list(reader)

    assert len(rows) == 1
    assert rows[0] == ["2024-12-01", "Food", "Lunch", "-12.5"]

def test_view_summary_by_category(monkeypatch, capsys):
    inputs = iter(["2024-12-01", "Food", "Lunch", "-12.5", "2024-12-02", "Food", "Dinner", "-20.0"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Reset the CSV
    with open("transactions.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["2024-12-01", "Food", "Lunch", "-12.5"])
        writer.writerow(["2024-12-02", "Food", "Dinner", "-20.0"])

    view_summary_by_category()
    captured = capsys.readouterr()

    assert "Food       |     -32.50" in captured.out
