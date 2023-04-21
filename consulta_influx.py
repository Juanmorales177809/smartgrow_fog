from influxdb_client import InfluxDBClient

host = "http://172.16.20.104:8086"
host1 = "http://200.122.207.134:8400"
token = "jBVyFx5RWXb4inIbSFWSVO07aPIye1atmtOrINZ9rgsxNnDidZXbnhipDACNVcPzR7ytzYkEuE48l7amhJhqpA=="
client = InfluxDBClient(url =host,token=token,org="smartgrow")
bucket = "iotsmart"
org = "smartgrow"
query_api = client.query_api()
query = 'from(bucket:"iotsmart")\
|> range(start: -24h)\
|> filter(fn:(r) => r._measurement == "my_measurement")\
|> filter(fn:(r) => r.location == "chamber_1")\
|> filter(fn:(r) => r._field == "temperature")\
|> aggregateWindow(every: 24h, fn: max, createEmpty: false,)\
  |> yield(name:"max")'
result = query_api.query(org=org, query=query)
results = []
for table in result:
    for record in table.records:
        results.append((record.get_field(), record.get_value()))

print(results)