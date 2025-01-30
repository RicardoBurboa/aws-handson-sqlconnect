import pymysql

# Función
def lambda_handler(event, context):
    try:
        endpoint = event["endpoint"]
        username = event["username"]
        password = event["password"]
        database_name = event["database_name"]
        query = event["query"]

        # Conectarse
        connection = pymysql.connect(
            host=endpoint,
            user=username,
            password=password,
            database=database_name
        )

        cursor = connection.cursor()
        cursor.execute(query)

        rows = cursor.fetchall()

        for row in rows:
            print("{0} | {1} | {2}".format(row[0], row[1], row[2]))

        return {
            "statusCode": 200,
            "body": rows
        }
    except:
        return {
            "statusCode": 500,
            "body": f"Error en la conexión a la base de datos: {str(e)}"
        }
