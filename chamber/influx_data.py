from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS
import os, json, subprocess
import time

bucket = "iotsmart"

# Establece la conexión con la base de datos de InfluxDB

url = "10.220.85.126"
cmd="curl -s -k " + url
token = "jBVyFx5RWXb4inIbSFWSVO07aPIye1atmtOrINZ9rgsxNnDidZXbnhipDACNVcPzR7ytzYkEuE48l7amhJhqpA=="
client = InfluxDBClient(url = "http://200.122.207.134:8400",token=token,org="smartgrow")
write_api = client.write_api(write_options=SYNCHRONOUS)
query_api = client.query_api()
print(query_api)

def main():
   data_send = 0
   while True:
      result = subprocess.Popen(["curl", url], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
      output, errors = result.communicate()

      if output:
         arr = json.loads(output)
         if  arr['variables']['temperature'] != 0:
            p = Point("my_measurement").tag("location", "chamber_1").field("temperature", arr['variables']['temperature']).tag("sensor_id",1)
            h = Point("my_measurement").tag("location", "chamber_1").field("humidity", arr['variables']['humidity']).tag("sensor_id",1)
            s = Point("my_measurement").tag("location", "chamber_1").field("Co2", arr['variables']['contaminacion']).tag("sensor_id",1)
            write_api.write(bucket=bucket, record=p)
            write_api.write(bucket=bucket, record=h)
            write_api.write(bucket=bucket, record=s)
            data_send+=1
            if data_send%1000==0:
               print(data_send, " datos enviados") 
          
        # with InfluxDBClient.from_config_file("config.toml") as client:
        #    with client.write_api(write_options=SYNCHRONOUS) as writer:
        #       try:
        #          writer.write(bucket=bucket, record=p)
        #          write_api.write(bucket=bucket, record=h)
        #          write_api.write(bucket=bucket, record=s)
        #       except InfluxDBError as e:
        #          print(e)

      else:
         print("esperando el cliente...")



if __name__ == "__main__":
   main()
