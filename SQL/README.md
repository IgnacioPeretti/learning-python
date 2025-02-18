Este ejercicio trabaja con la base de datos Northwind.

Analizamos la rentabilidad de los productos y empleados en términos de ventas.


Lo que trabajamos en el código.

Conexión a la base de datos:

Se establece una conexión a la base de datos northwind.db usando sqlite3.


Obtener los 10 productos más rentables:

Se calcula el revenue (ingresos) de cada producto multiplicando el precio (Price) por la cantidad (Quantity) en la tabla OrderDetails.
Se agrupan los datos por ProductID y se suman los ingresos de cada producto.
Se ordenan de mayor a menor y se seleccionan los 10 más rentables.
Se crea un gráfico de barras con matplotlib para visualizar los productos más rentables.

Obtener los 10 empleados más rentables:

Se cuentan la cantidad de pedidos gestionados por cada empleado (COUNT(*) en la tabla Orders).
Se agrupan por EmployeeID y se ordenan de mayor a menor.
Se crea un gráfico de barras para visualizar los empleados que procesaron más ventas.


Obtener  los 10 empleados que generaron mas ingresos:

Se calcula el total de ingresos generados por cada empleado sumando el producto de Price (de Products) por Quantity (de OrderDetails).
Se unen las tablas Orders, Employees, OrderDetails y Products para obtener el precio de los productos vendidos por cada empleado.
Se agrupan los datos por EmployeeID y se ordenan de mayor a menor según los ingresos generados.
Se genera un gráfico de barras para visualizar los empleados con mayores ingresos.

