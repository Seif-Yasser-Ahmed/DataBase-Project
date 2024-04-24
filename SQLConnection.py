############################################################
# Will be movved to ui_function.py
############################################################
import pyodbc

try:
    connection = pyodbc.connect('DRIVER={SQL Server};' +
                                'Server=LAPTOP-019RIHG4;' +
                                'Database=Team-5;' +
                                'Trusted_Connection=True;')
    print("Connection Established")

    # Set autocommit to True (optional)
    connection.autocommit = True
    # cursor = connection.cursor()
    sql_stmt = '''INSERT INTO Employee (EmployeeSalary, UserID)
SELECT 50000.00, 2
WHERE NOT EXISTS (
    SELECT 1
    FROM Trainee
    WHERE Trainee.UserID = 2
)AND NOT EXISTS (
    SELECT 1
    FROM Trainer
    WHERE Trainer.UserID = 3
);'''
    connection.execute(sql_stmt)

except pyodbc.Error as e:
    print("Connection Failed:", e)
