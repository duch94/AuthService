FROM tiangolo/uwsgi-nginx-flask:python3.7

COPY ./app/requirements.txt /app/requirements.txt
RUN pip3 install -r /app/requirements.txt

COPY ./app /app
