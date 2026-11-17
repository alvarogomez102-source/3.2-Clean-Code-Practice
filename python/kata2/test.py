import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


class Test(unittest.TestCase):
    def test_sample_quote(self):
        with tempfile.TemporaryDirectory() as directory:
            result = subprocess.run(
                [sys.executable, str(Path(__file__).with_name("main.py"))],
                cwd=directory,
                capture_output=True,
                text=True,
                check=True,
            )
        for expected in (
            "Subtotal: EUR 55.00",
            "Shipping: EUR 0.00",
            "Total: EUR 55.00",
            "Free shipping unlocked",
        ):
            self.assertIn(expected, result.stdout)


if __name__ == "__main__":
    unittest.main()
