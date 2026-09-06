"""Make the handler modules under src/ importable by the tests."""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))
