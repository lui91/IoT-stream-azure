import asyncio
import json
from azure.eventhub import EventData
from azure.eventhub.aio import EventHubProducerClient
from azure.identity.aio import DefaultAzureCredential

EVENT_HUB_FULLY_QUALIFIED_NAMESPACE = "coffe-events.servicebus.windows.net"
EVENT_HUB_NAME = "coffee-stream"

credential = DefaultAzureCredential()


async def run():
    # Create a producer client to send messages to the event hub.
    # Specify a credential that has correct role assigned to access
    # event hubs namespace and the event hub name.
    producer = EventHubProducerClient(
        fully_qualified_namespace=EVENT_HUB_FULLY_QUALIFIED_NAMESPACE,
        eventhub_name=EVENT_HUB_NAME,
        credential=credential,
    )
    async with producer:
        # Create a batch.
        event_data_batch = await producer.create_batch()

        data_first = {
            "serial_number": "3",
            "model": "top",
            "event_date": "12062023",
            "event_type": {
                "Clean": "Success"
            }
        }
        data_second = {
            "serial_number": "4",
            "model": "low",
            "event_date": "12062023",
            "event_type": {
                "Brew": "Success"
            }
        }

        # Add events to the batch.
        event_data_batch.add(EventData(json.dumps(data_first)))
        event_data_batch.add(EventData(json.dumps(data_second)))

        # Send the batch of events to the event hub.
        await producer.send_batch(event_data_batch)

        # Close credential when no longer needed.
        await credential.close()

        print("Data sent successfully")

asyncio.run(run())
