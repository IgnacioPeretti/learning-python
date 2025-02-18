"""""
Ejercicio de rentabilidad
"""""

import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

conn = sqlite3.connect(r"C:\SQLite3\databases\northwind.db")



# Obteniendo los 10 productos mas rentables

query = """
    SELECT  ProductName, SUM(Price * Quantity) as Revenue
    FROM OrderDetails od 
    JOIN Products p ON p.ProductID = od.ProductID
    GROUP BY od.ProductID
    ORDER BY Revenue DESC
    LIMIT 10
"""

top_products = pd.read_sql_query(query,conn)

print(top_products)

top_products.plot(x="ProductName", y="Revenue", kind="bar", figsize=(10,5), legend=False)

plt.title("10 productos mas rentables")
plt.xlabel("Productos")
plt.ylabel("Revenue")
plt.xticks(rotation = 90)
plt.show()

# Obteniendo los 10 empleados mas rentables


query = """
    SELECT FirstName || " " || LastName as Employee, COUNT(*) as Total
    FROM Orders o
    JOIN Employees e
    ON e.EmployeeID = o.EmployeeID  
    GROUP BY o.EmployeeID
    ORDER BY Total DESC
"""

top_employees = pd.read_sql_query(query, conn)
top_employees.plot(x="Employee", y="Total", kind="bar",figsize=(10,5), legend=False)

plt.title("10 empleados mas rentables")
plt.xlabel("Empleados")
plt.ylabel("Total Vendido")
plt.xticks(rotation = 90)
plt.show()


# Obteniendo los 10 empleados que generaron más ingresos

query = """
    SELECT FirstName || " " || LastName as Employee, 
           SUM(p.Price * od.Quantity) as TotalRevenue
    FROM Orders o
    JOIN Employees e ON e.EmployeeID = o.EmployeeID  
    JOIN OrderDetails od ON o.OrderID = od.OrderID
    JOIN Products p ON od.ProductID = p.ProductID
    GROUP BY o.EmployeeID
    ORDER BY TotalRevenue DESC
    LIMIT 10;
"""

top_employees_revenue = pd.read_sql_query(query, conn)  # Cambio de variable para evitar sobrescribir

top_employees_revenue.plot(x="Employee", y="TotalRevenue", kind="bar", figsize=(10,5), legend=False)

plt.title("10 empleados que generaron más ingresos")
plt.xlabel("Empleados")
plt.ylabel("Ingresos Totales")
plt.xticks(rotation=90)
plt.show()
