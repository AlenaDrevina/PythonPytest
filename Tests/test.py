import pyodbc
import pytest
import pymssql

'''
try:
    connection = pyodbc.connect('DRIVER={SQL Server};Server=EPBYMINW0EE0\\SQLEXPRESS03;Database=TRN;username= testuser;password=password12345')
    print("There is connection to DB")
except Exception as ex:
    print(ex)  '''

connection = pymssql.connect(
    host='172.22.144.1',
    user='testuser',
    password='password12345',
    database='TRN'
)

def test01():
    """
    AUTO-001: [Jobs] completeness
    Find out if table jobs is not empty
    result: pass
    """
    cursor = connection.cursor()
    cursor.execute("Select count(*) from hr.jobs")
    rows = cursor.fetchall()
    if len(list(rows)) > 0:
        print(f'Table jobs is not empty')
    return 1



def test02():
    """
    AUTO-002: [Jobs] completeness
    Find out if the quantity of expecting result is the same as in query
    result: pass
    """
    cursor = connection.cursor()
    cursor.execute("Select count(*) from hr.jobs")
    rows = cursor.fetchall()[0][0]
    if rows == 19:
        print(f'The property of completeness is fulfilled')
    return 1

def test03():
    """
    AUTO-003: [Employees] uniqueness
    Find out if duplicate rows exist
    result: pass
    """
    cursor = connection.cursor()
    cursor.execute("select employee_id, job_id, manager_id, department_id, count(*) from hr.employees group by employee_id, job_id, manager_id, department_id having count(*)>1")
    rows = cursor.fetchall()
    if len(list(rows)) == 0:
        print(f'There are no duplicates')
    return 1

def test04():
    """
    AUTO-004: [Employees] validity
    Be sure that average salary of employees - 8060
    result: pass
    """
    cursor = connection.cursor()
    cursor.execute("SELECT sum(salary)/count(*) as average_salary FROM hr.employees")
    rows = cursor.fetchall()[0][0]
    if rows == 8060:
        print(f'The average salary is as in expected result')
    return 1


def test05():
    """
    AUTO-005: [Employees] validity
    Find min_salary of all employees
    result: pass
    """
    cursor = connection.cursor()
    cursor.execute("select min(salary) as min_salary from hr.employees;")
    rows = cursor.fetchall()[0][0]
    if rows == 2500:
        print(f'Min salary is 2500(')
    return 1

def test06():
    """
    AUTO-006: [Locations] accuracy
    Check that Toronto is the city in Canada
    result: pass
    """
    cursor = connection.cursor()
    cursor.execute("select city from hr.locations where country_id='CA';")
    rows = cursor.fetchall()[0][0]
    if rows == 'Toronto':
        print(f'Toronto is the city in Canada')
    return 1

def test07():
    """
    AUTO-007: [Locations] additional verification
    Check that the quantity of postal_code's length of 5 symbols is 4
    result: pass
    """
    cursor = connection.cursor()
    cursor.execute("select count(*) from hr.locations where len(postal_code)<6;")
    rows = cursor.fetchall()[0][0]
    if rows == 4:
        print(f'The quantity of postal_code length of 5 symbols is 4')
    return 1

def test08():
    """
    AUTO-008: [Dependents] additional verification
    Check that don't exist rows of column 'first_name' which is equal to rows from
    column 'last_name'
    result: pass
    """
    cursor = connection.cursor()
    cursor.execute("SELECT count(*) FROM hr.dependents WHERE first_name=last_name;")
    rows = cursor.fetchall()[0][0]
    if rows == 0:
        print(f'Do not exist rows of first_name which is equal to rows from last_name')
    return 1

def test09():
    """
    AUTO-009: [Dependents] additional verification
    Find out the quantity where length of first_name and last_name is equal
    result: pass
    """
    cursor = connection.cursor()
    cursor.execute("SELECT count(*) FROM hr.dependents WHERE len(first_name)=len(last_name);")
    rows = cursor.fetchall()[0][0]
    if rows == 3:
        print(f'The length of first_name and last_name is equal')
    return 1