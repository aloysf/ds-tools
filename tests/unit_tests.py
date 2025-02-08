import os.path
import sys
import pandas as pd

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

# This will produce the path to the test data on any OS and machine,
# if run inside unit_tests.py

# Strictly needed
TEST_DATA_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", 'tests', 'test_data')
)

from ds_tools.data import generate_data
from ds_tools.analysis import analyse_data
from ds_tools.plotting import plot_analysis

raw_data = generate_data()
fit_results = analyse_data(raw_data=raw_data)

def test_raw_data():
    ref_data = pd.read_parquet(os.path.join(TEST_DATA_DIR, 'raw_data.parquet'))
    try:
        pd.testing.assert_frame_equal(raw_data, ref_data)
    except AssertionError:
        assert False

def test_analyse_data():
    ref_data = pd.read_parquet(os.path.join(TEST_DATA_DIR, 'fit_results.parquet'))
    try:
        pd.testing.assert_frame_equal(fit_results, ref_data)
    except AssertionError:
        assert False

def test_full_analysis():
    try:
        raw_data = generate_data()
        fit_results = analyse_data(raw_data=raw_data)
        plot_analysis(raw_data, fit_results)
    except Exception:
        assert False