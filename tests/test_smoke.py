import importlib
import pathlib
import sys
import unittest


sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "src"))


class TestSmoke(unittest.TestCase):
    def test_main_exists(self):
        mod = importlib.import_module("workflow_weaver.cli")
        self.assertTrue(hasattr(mod, "main"))


if __name__ == "__main__":
    unittest.main()
