FROM python:3

RUN pip install azure-cli
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN az login
COPY data_bricks_data.py data_bricks_data.py
COPY event_generator.py event_generator.py
COPY coffee_data_streaming.py coffee_data_streaming.py
CMD [ "python", "coffee_data_streaming.py"]