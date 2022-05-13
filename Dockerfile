FROM python:3.8
ADD ./tarea /code
WORKDIR /code
RUN pip install -r requirements.txt
CMD python app.py