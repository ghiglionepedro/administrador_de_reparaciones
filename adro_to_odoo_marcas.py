tablamarcas = "marcas"
tablaproductos ="productos"

query = " SELECT " + tablamarcas + ".Id, " + tablamarcas + ".Nombre ," + tablaproductos + ".Nombre AS nombre_producto"
query += " FROM " + tablamarcas;
query += " INNER JOIN " + tablaproductos + " ON " + tablaproductos + ".Id = " + tablamarcas + ".Id_producto"
query += " WHERE "+ tablamarcas +  ".Activo = 1"

print (query)