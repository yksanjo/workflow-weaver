import importlib


def test_main_exists():
    mod = importlib.import_module("workflow_weaver.cli")
    assert hasattr(mod, "main")
