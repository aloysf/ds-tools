import os.path

# This will produce the path to the test data on any OS and machine,
# if run inside unit_tests.py

# Strictly needed
TEST_DATA_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", 'tests', 'test_data')
)