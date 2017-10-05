# Description
This project contains:
* [Addressline converter utility](https://github.com/alderven/addressline/blob/master/addressline.py)
* [Test cases](https://github.com/alderven/addressline/blob/master/test_Addressline.py)
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

# Test Cases description and run result

№  | Test scenario | Result
-- | ----------------------- | ---------- |
1  | Convert "Winterallee 3" | [Passed](https://rawgit.com/alderven/addressline/master/allure-report/index.html#behaviors/8e0b0249ce25345e94bf58b5320969c6/7b9059918dae87e9/) |
2  | Convert "Musterstrasse 45" | [Passed](https://rawgit.com/alderven/addressline/master/allure-report/index.html#behaviors/8e0b0249ce25345e94bf58b5320969c6/616efa3ad9e3f564/) |
3  | Convert "Blaufeldweg 123B" | [Passed](https://rawgit.com/alderven/addressline/master/allure-report/index.html#behaviors/8e0b0249ce25345e94bf58b5320969c6/10630e181b2bd81/) |
4  | Convert "Am Bächle 23" | [Passed](https://rawgit.com/alderven/addressline/master/allure-report/index.html#behaviors/8e0b0249ce25345e94bf58b5320969c6/af9f88d694a64969/) |
5  | Convert "Auf der Vogelwiese 23 b" | [Passed](https://rawgit.com/alderven/addressline/master/allure-report/index.html#behaviors/8e0b0249ce25345e94bf58b5320969c6/3939eebf0edacc/) |
6  | Convert "4, rue de la revolution" | [Passed](https://rawgit.com/alderven/addressline/master/allure-report/index.html#behaviors/8e0b0249ce25345e94bf58b5320969c6/2c0fc1011db2224d/) |
7  | Convert "200 Broadway Av" | [Passed](https://rawgit.com/alderven/addressline/master/allure-report/index.html#behaviors/8e0b0249ce25345e94bf58b5320969c6/838a0ac58e10e217/) |
8  | Convert "Calle Aduana, 29" | [Passed](https://rawgit.com/alderven/addressline/master/allure-report/index.html#behaviors/8e0b0249ce25345e94bf58b5320969c6/809a10372a4b4a8a/) |
9  | Convert "Calle 39 No 1540" | [Passed](https://rawgit.com/alderven/addressline/master/allure-report/index.html#behaviors/8e0b0249ce25345e94bf58b5320969c6/bcaaa7a866a04aa2/) |
