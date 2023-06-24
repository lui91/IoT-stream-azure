from databricks import sql
import os

DATABRICKS_SERVER_HOSTNAME = os.getenv('ENV_SERVER_HOSTNAME')
DATABRICKS_HTTP_PATH = os.getenv('ENV_HTTP_PATH')
DATABRICKS_TOKEN = os.getenv('ENV_TOKEN')


def fetch_serial_numbers():
    with sql.connect(server_hostname=DATABRICKS_SERVER_HOSTNAME,
                     http_path=DATABRICKS_HTTP_PATH,
                     access_token=DATABRICKS_TOKEN) as connection:
        with connection.cursor() as cursor:

            cursor.execute(
                "SELECT machine_serial_number FROM coffee_shop.users")
            result = cursor.fetchall()

            serial_numbers = [row[0] for row in result]
            return serial_numbers
