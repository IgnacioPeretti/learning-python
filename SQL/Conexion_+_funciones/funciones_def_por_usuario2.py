import sqlite3
import pandas as pd

square = lambda n : n*n

with sqlite3.connect(r"C:\SQLite3\databases\northwind.db") as conn:         # Con el with la conexión se cierra automaticamente

    conn.create_function("square",1,square)
    cursor = conn.cursor()
    cursor.execute("SELECT *, square(Price) FROM Products WHERE Price > 0")
    results = cursor.fetchall()

    results_df = pd.DataFrame(results)

print(results_df)


