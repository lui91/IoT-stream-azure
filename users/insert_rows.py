from databricks import sql
from user_generation import UserGenerator
import os

DATABRICKS_SERVER_HOSTNAME = os.getenv('ENV_SERVER_HOSTNAME')
DATABRICKS_HTTP_PATH = os.getenv('ENV_HTTP_PATH')
DATABRICKS_TOKEN = os.getenv('ENV_TOKEN')

user_generator = UserGenerator(total_users=50)
rows = user_generator.generate_data()

with sql.connect(server_hostname=DATABRICKS_SERVER_HOSTNAME,
                 http_path=DATABRICKS_HTTP_PATH,
                 access_token=DATABRICKS_TOKEN) as connection:
    with connection.cursor() as cursor:
        cursor.execute(
            f"INSERT INTO coffee_shop.users(name, machine_serial_number, birthdate, loyalty_points, email) VALUES {rows}")
        print("Record stored")
