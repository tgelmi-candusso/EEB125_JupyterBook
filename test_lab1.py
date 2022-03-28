from notebook_helper import importer
import Lab_1
import numpy as np
import pytest

@pytest.fixture(scope='module', autouse=True)
def load_code():
    importer.run_cells(Lab_1)

def test_five():
    assert Lab_1.five == 5
