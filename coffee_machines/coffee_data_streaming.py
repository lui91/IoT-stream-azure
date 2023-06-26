from event_generator import EventGenerator
import asyncio
import json
from azure.eventhub import EventData
from azure.eventhub.aio import EventHubProducerClient
from azure.identity.aio import DefaultAzureCredential
import os


class coffee_machine:
    def __init__(self, batch_size=10, n_events=200) -> None:
        self.event_generator = EventGenerator()
        self.batch_size = batch_size
        self.n_events = n_events
        self.credential = DefaultAzureCredential()
        self.producer = EventHubProducerClient(
            fully_qualified_namespace=os.getenv('EVENT_HUB_NAMESPACE'),
            eventhub_name=os.getenv('EVENT_HUB_NAME'),
            credential=self.credential,
        )

    async def send_data(self):
        async with self.producer:
            event_data_batch = await self.producer.create_batch()
            for _ in range(self.batch_size):
                event = self.event_generator.generate_event()
                event_data_batch.add(EventData(json.dumps(event)))

            await self.producer.send_batch(event_data_batch)
            print("Batch sent successfully")

    async def stream(self):
        for _ in range(self.n_events):
            await self.send_data()
        await self.credential.close()
        print("Data streamed")


c = coffee_machine()
asyncio.run(c.stream())
