import pyodbc
import pytest

connection = pyodbc.connect('DRIVER={SQL Server};Server=EPBYMINW0EE0\\SQLEXPRESS03;Database=TRN;username= testuser;password=password12345')
print("There is connection to DB")
