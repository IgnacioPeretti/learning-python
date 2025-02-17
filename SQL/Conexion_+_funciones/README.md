Este repositorio contiene un script en Python que demuestra cómo trabajar con bases de datos SQLite, 
ejecutar consultas SQL y definir funciones personalizadas en SQLite utilizando create_function.

Utilizamos la base de datos nortwind (https://gist.github.com/jmalarcon/e98d20735d17b3160766c041060d1902)

Este ejercicio es útil para aprender sobre la integración de SQLite con Python y cómo extender SQL con funciones personalizadas.

Caracteristicas:

Conexión a SQLite: Uso de sqlite3.connect() con with para manejar la conexión automáticamente.

Funciones definidas por el usuario (UDFs): Se registra una función square(n), que devuelve el cuadrado de un número, para ser utilizada dentro de las consultas SQL.

Consultas SQL con Python: Se ejecuta una consulta para seleccionar productos de la tabla Products donde el precio es mayor a 0, aplicando la función square(Price).

Uso de Pandas: Se convierte el resultado de la consulta en un DataFrame de Pandas para facilitar su manipulación y análisis.