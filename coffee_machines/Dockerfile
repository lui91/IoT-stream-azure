FROM python:3

RUN pip install azure-cli
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN az login
COPY data_bricks_data.py data_bricks_data.py
COPY stream_data_generation.py stream_data_generation.py
CMD [ "python", "stream_data_generation.py"]