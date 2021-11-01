# Web Automation Skeleton Python

## Installation
##### Use the package manager pip to install project dependency

    $ cd to the directory where requirements.txt is located
    $ run: pip3 install -r requirements.txt


## Configure project
#### Edit Test>testconf>runconfiguration for configure Test suite
    $ system configuration
        e.g. select headless mode, select os
    $ project configuration
        e.g. portal selection , admin selection


## Run Project

    $ cd to the "Test" directory
    $ run: python3 testconf/runtest.py

## Run individual testcase

 ##### run test using unittest

    $ cd to the "Test" directory
    $ python3 -m unittest TestCase.TC_file_name (without '.py')
    
##### run test with allure report

    $ cd to the "Test" directory
    $ python -m pytest -s TestCase/TC_file_name.py --alluredir=ReportAllure &&  allure serve ReportAllure/
