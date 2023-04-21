from influxdb_client import InfluxDBClient, Point, WriteOptions
from influxdb_client.client.write_api import SYNCHRONOUS
import os, json, subprocess
import time
from dateutil import parser

bucket = "iotsmart"

# Establece la conexión con la base de datos de InfluxDB
url = "10.220.85.126"
cmd="curl -s -k " + url

def generate(data):
    output = 0
    while not output:
        result = subprocess.Popen(["curl", url], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, errors = result.communicate() 
        print("esperando datos...")     
    arr = json.loads(output)
    data['timestamp'] = time.time()
    data['temperature'] = arr['variables']['temperature']
    
def main():
    data = {
        "device_id": '1',
        "client_id": "001SMART",
        "sensor_type": "Temperature",
        "temperature": 0,
        "timestamp": time.time()
    }
    while True:
        generate(data)
        with open('/tmp/output_sensor.json','a') as output_file:
            output_file.write(f'{json.dumps(data)}\n')
        time.sleep(0.5)

token = "jBVyFx5RWXb4inIbSFWSVO07aPIye1atmtOrINZ9rgsxNnDidZXbnhipDACNVcPzR7ytzYkEuE48l7amhJhqpA=="
client = InfluxDBClient(url = "http://200.122.207.134:8400",token=token,org="smartgrow")

write_api = client.write_api(write_options=SYNCHRONOUS)
query_api = client.query_api()
print(query_api)

# def main():
#     error = 0
#     while True:
#         try:
#             result = os.popen(cmd).read()
#             arr = json.loads(result)
#             p = Point("my_measurement").tag("location", "chamber_1").field("temperature", arr['variables']['temperature']).tag("sensor_id", 1)
#             write_api.write(bucket=bucket, record=p)
#             h = Point("my_measurement").tag("location", "chamber_1").field("humidity", arr['variables']['humidity']).tag("sensor_id", 1)
#             write_api.write(bucket=bucket, record=h)
#             s = Point("my_measurement").tag("location", "chamber_1").field("Co2", arr['variables']['contaminacion']).tag("sensor_id", 1)
#             write_api.write(bucket=bucket, record=s)
#         except:
#             print(error)

def main():
    while True:
        result = subprocess.Popen(["curl", url], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, errors = result.communicate()

        if output:
            arr = json.loads(output)
            p = Point("my_measurement").tag("location", "chamber_1").field("temperature", arr['variables']['temperature']).tag("sensor_id",1)
            h = Point("my_measurement").tag("location", "chamber_1").field("humidity", arr['variables']['humidity']).tag("sensor_id",1)
            s = Point("my_measurement").tag("location", "chamber_1").field("Co2", arr['variables']['contaminacion']).tag("sensor_id",1)

            with InfluxDBClient.from_config_file("config.toml") as client:
                with client.write_api(write_options=SYNCHRONOUS) as writer:
                    try:
                        writer.write(bucket=bucket, record=p)
                        write_api.write(bucket=bucket, record=h)
                        write_api.write(bucket=bucket, record=s)
                    except:
                        print("Error")

#         else:
#             print("esperando el cliente...")
if __name__ == "__main__":
    main()

# ## using Table structure
# tables = query_api.query('from(bucket:"my-bucket") |> range(start: -10m)')

# for table in tables:
#     print(table)
#     for row in table.records:
#         print (row.values)


# ## using csv library
# csv_result = query_api.query_csv('from(bucket:"smartdata") |> range(start: -10m)')
# val_count = 0
# for row in csv_result:
#     for cell in row:
#         val_count += 1


