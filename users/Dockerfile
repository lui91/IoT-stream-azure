FROM python:3

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY user_generation.py user_generation.py
COPY insert_rows.py insert_rows.py
CMD [ "python", "insert_rows.py" ]