from databricks import sql

DATABRICKS_SERVER_HOSTNAME="adb-1469634309361132.12.azuredatabricks.net"
DATABRICKS_HTTP_PATH="sql/protocolv1/o/1469634309361132/0613-164813-shitp1hi"
DATABRICKS_TOKEN="dapi16465a3b0f07b03c13bc04a925d1940f-3"

with sql.connect(server_hostname=DATABRICKS_SERVER_HOSTNAME,
                 http_path=DATABRICKS_HTTP_PATH,
                 access_token=DATABRICKS_TOKEN) as connection:
    with connection.cursor() as cursor:
        # cursor.execute("INSERT INTO `coffee_shop`.`users` VALUES 'Luis Ramirez', 117, '05/05/1991', 2, 'lm@coffee.com'")
        cursor.execute("INSERT INTO coffee_shop.users VALUES ('Luis Ramirez', 117, 2, 'lm@coffee.com')")
        print("Record stored")