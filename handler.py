import pymysql

# Configuración de la conexión
endpoint = "database-1.cbgyowye8kbi.us-east-1.rds.amazonaws.com"
username = "admin"
password = "administrator"
database_name = "mi_base_de_datos"
query = "SELECT * FROM clientes"

# Conectarse
connection = pymysql.connect(
    host=endpoint,
    user=username,
    password=password,
    database=database_name
)

# Función
def lambda_handler(event, context):
    cursor = connection.cursor()
    cursor.execute(query)

    rows = cursor.fetchall()

    for row in rows:
        print("{0} | {1} | {2}".format(row[0], row[1], row[2]))
