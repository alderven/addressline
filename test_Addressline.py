import os
import pytest
import csv
from addressline import addressline

test_data_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'testData.txt')


def get_test_data():
    result = []
    with open(test_data_file, 'r') as f:
        data = csv.reader(f, delimiter=';')
        for row in data:
            result.append([row[0], row[1], row[2]])
    return result


@pytest.allure.feature('Addressline')
@pytest.allure.story('Test Addressline')
@pytest.allure.severity(pytest.allure.severity_level.BLOCKER)
@pytest.mark.parametrize('test_data', get_test_data())
def test_addressline(test_data):
    input_str = test_data[0]
    expected_result = [test_data[1], test_data[2]]
    actual_result = addressline(input_str)
    msg = 'Input string: "{}". Expected result: {}. Actual result: {}'.format(input_str, expected_result, actual_result)
    with pytest.allure.step(msg):
        assert expected_result == actual_result, msg
