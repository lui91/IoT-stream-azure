from faker import Faker


class UserGenerator:
    def __init__(self, total_users=50) -> None:
        self.total_users = total_users
        self.generator = Faker()

    def generate_record(self):
        name = self.generator.name()
        serial_number = self.generator.unique.random_int()
        birth = self.generator.date()
        points = self.generator.random.randint(a=1, b=1000)
        email = self.generator.random.choice(
            name.split(' ')).lower() + "@somemail.com"
        return f"('{name}', {serial_number}, DATE'{birth}', {points} ,'{email}')"

    def generate_data(self):
        '''
        Generate sample clients data
        name, machine_serial_number, birthdate, loyalty_points, email 
        '''
        records = [self.generate_record() for _ in range(self.total_users)]
        insert_values = ",".join([record for record in records])
        return insert_values
