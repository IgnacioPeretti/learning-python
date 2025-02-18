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


Posible mejora: Para calcular realmente la rentabilidad de los empleados, se podría modificar la consulta para que en lugar de contar órdenes (COUNT(*)), se sumen los ingresos generados por cada empleado.