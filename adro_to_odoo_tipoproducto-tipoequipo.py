tablaproductos ="productos"

query = " SELECT " + tablaproductos + ".Id, " + tablaproductos + ".Nombre "
query += " FROM " + tablaproductos
query += " WHERE Activo = 1"

print (query)