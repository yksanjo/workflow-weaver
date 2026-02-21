import importlib
import unittest


class TestSmoke(unittest.TestCase):
    def test_main_exists(self):
        mod = importlib.import_module("workflow_weaver.cli")
        self.assertTrue(hasattr(mod, "main"))


if __name__ == "__main__":
    unittest.main()
