import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


class Test(unittest.TestCase):
    def test_sample_exports(self):
        with tempfile.TemporaryDirectory() as directory:
            result = subprocess.run(
                [sys.executable, str(Path(__file__).with_name("main.py"))],
                cwd=directory,
                capture_output=True,
                text=True,
                check=True,
            )
        for expected in (
            "Exported Weekly sales as CSV",
            "Keyboard,3,135.0",
            "Mouse,5,90.0",
            "Exported Weekly sales as JSON",
            '"product": "Keyboard"',
            '"revenue": 90.0',
        ):
            self.assertIn(expected, result.stdout)


if __name__ == "__main__":
    unittest.main()
