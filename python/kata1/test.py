import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


class Test(unittest.TestCase):
    def test_sample_receipt(self):
        with tempfile.TemporaryDirectory() as directory:
            result = subprocess.run(
                [sys.executable, str(Path(__file__).with_name("main.py"))],
                cwd=directory,
                capture_output=True,
                text=True,
                check=True,
            )
        self.assertIn("Member discount applied", result.stdout)
        self.assertIn("Discount: EUR 2.40", result.stdout)
        self.assertIn("Total: EUR 21.60", result.stdout)


if __name__ == "__main__":
    unittest.main()
