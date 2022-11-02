# Environment setup

### Automation Testing Framework
Framework to run data-related tests on Database MS SQL SERVER.
Tests are based on pytest framework.There are basic SQL-based tests.

## Name and description of project
Project pythonPytest contains determined automated test cases
of 4 tables - Jobs,Employees,Locations and Dependents that have specific tag-name to link to Jira issues.

## Test cases creation and management
Tests should be atomic, independent, reasonable and self-described.

## Create virtual environment for tests execution
```bash
pip install -r requirements.txt
```

## Deploy and configure Data Quality solution
Follow [instructions](../README.md)

## Project location
The project can be found in repository:

git clone: https://git.epam.com/alena_drevina/pythonPytest.git

## Run tests
```bash
python Tests/test.py
pytest -v -s Tests/ --html=report.html
pytest tests/ --html-report=./report --title='PYTEST REPORT'
```

# Report portal 
There are HTML outputs of test that are run. It's going to tell it to copy it into an object store, 
just it's accessible to everybody to monitoring about the quality of the database.
All the results after execution following commands can be found in root of the project with names: 
report.html and pytest_html_report.html with all received information.