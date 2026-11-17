import csv
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


class Test(unittest.TestCase):
    def test_sample_registrations(self):
        with tempfile.TemporaryDirectory() as directory:
            result = subprocess.run(
                [sys.executable, str(Path(__file__).with_name("main.py"))],
                cwd=directory,
                capture_output=True,
                text=True,
                check=True,
            )
            with (Path(directory) / "registrations.csv").open(newline="", encoding="utf-8") as file:
                rows = list(csv.DictReader(file))
        self.assertIn("Quote for Alan Turing: EUR 135.89", result.stdout)
        self.assertIn("Quote for Margaret Hamilton: EUR 201.80", result.stdout)
        self.assertIn("'revenue': 337.69", result.stdout)
        self.assertIn("'quotes_logged': 4", result.stdout)
        self.assertEqual([row["total"] for row in rows], ["135.89", "201.8"])


if __name__ == "__main__":
    unittest.main()
