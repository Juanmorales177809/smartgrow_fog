FROM python:3.8-buster
WORKDIR /chamber
RUN pip install pip install influxdb-client
COPY influx_data.py influx_data.py
CMD ["python", "influx_data.py"]

