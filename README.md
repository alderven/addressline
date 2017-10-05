# Description
This project contains:
* [Addressline converter utility](https://github.com/alderven/addressline/blob/master/addressline.py)
* [Test case](https://github.com/alderven/addressline/blob/master/test_Addressline.py)
* [Allure Test Report](https://rawgit.com/alderven/addressline/master/allure-report/index.html)

# How to install

1. Download and unzip this project: https://github.com/alderven/addressline/archive/master.zip
1. Install Python 3.6 or higher: https://www.python.org/downloads/
1. Install Allure Framework: https://docs.qameta.io/allure/latest/
1. Install following Python libs:
   * pytest: https://docs.pytest.org/en/latest/getting-started.html
   * pytest-allure-adaptor: https://pypi.python.org/pypi/pytest-allure-adaptor

# How to run Addressline utility
Execute following line in CMD in the project folder:
```
python addressline.py -a "string to convert"
```

# How to run tests
Execute following line in CMD in the project folder:
```
python -m pytest --alluredir /full/path/to/report/folder
```

# How to generate Allure report
Execute following line in CMD in the project folder:
```
allure serve /full/path/to/report/folder
```
