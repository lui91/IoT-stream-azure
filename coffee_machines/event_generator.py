from faker import Faker
from datetime import date
from data_bricks_data import fetch_serial_numbers


class EventGenerator:
    '''
    Creates a simulated event of the registered coffee machines in the databricks data warehouse. 
    '''

    def __init__(self, number_of_events=400) -> None:
        self.generator = Faker()
        self.number_of_events = number_of_events
        self.models = ['low', 'mid', 'high']
        self.event_types = ['Clean', 'Brew']
        self.status = ['True', 'False']
        self.serial_numbers = fetch_serial_numbers()

    def generate_event(self):
        '''
        Creates event data and returns it in dict format.
        '''
        number = self.generator.random.choice(self.serial_numbers)
        model = self.generator.random.choice(self.models)
        event_date = self.generator.date_between(start_date=date(2000, 1, 1))
        event_type = self.generator.random.choice(self.event_types)
        status = self.generator.random.choice(self.status)

        record = {
            "serial_number": number,
            "model": model,
            "event_date": str(event_date),
            "event_type": event_type,
            "status": status
        }
        return record

    def generate_stream(self):
        '''
        Creates a series of events and returns it in a str.
        '''
        stream = ",".join([self.generate_event(self.serial_numbers)
                          for _ in range(self.number_of_events)])
        print(stream)
