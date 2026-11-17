import csv
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


class Test(unittest.TestCase):
    def test_sample_booking(self):
        with tempfile.TemporaryDirectory() as directory:
            result = subprocess.run(
                [sys.executable, str(Path(__file__).with_name("main.py"))],
                cwd=directory,
                capture_output=True,
                text=True,
                check=True,
            )
            with (Path(directory) / "bookings.csv").open(newline="", encoding="utf-8") as file:
                rows = list(csv.DictReader(file))
        self.assertIn("Booking BK-204 confirmed for EUR 366.00", result.stdout)
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0]["reference"], "BK-204")
        self.assertEqual(rows[0]["total"], "366")


if __name__ == "__main__":
    unittest.main()
