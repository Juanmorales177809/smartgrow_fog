import os, json
import time


url = "10.220.85.126"
cmd="curl -s -k " + url

def generate(data):
    result = os.popen(cmd).read()
    arr = json.loads(result)
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

if __name__ == "__main__":
    main()