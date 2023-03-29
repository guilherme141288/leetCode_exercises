import json
import sqlite3

conn = sqlite3.connect('rosterdb.sqlite')
cur = conn.cursor()

cur.executescript('''
    SELECT d.Name AS 'Department', e.Name AS 'Employee', e.Salary
    FROM Employee e
    INNER JOIN Department d ON e.DepartmentId = d.Id
    WHERE e.Salary = (
        SELECT MAX(Salary)
        FROM Employee
        WHERE DepartmentId = d.Id)
''')

conn.commit()
