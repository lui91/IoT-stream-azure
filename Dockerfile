FROM python:3

RUN pip install azure-cli
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN az login
COPY comms_test.py comms_test.py
CMD [ "python", "comms_test.py" ]