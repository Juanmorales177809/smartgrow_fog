import os, json
import time
import csv


url = "10.220.85.126"
cmd="curl -s -k " + url

def generate(data):
    result = os.popen(cmd).read()
    arr = json.loads(result)
    data['timestamp'] = time.time()
    data['temperature'] = arr['variables']['temperature']
    data['humidity'] = arr['variables']['humidity']
    data['contaminacion'] = arr['variables']['contaminacion']
def main():
    data = {
        "temperature": 0,
        "humidity":0,
        "contaminacion":0,
        "timestamp": time.time()
    }
    while True:
        generate(data)
        with open('output_sensor.csv',mode='w') as archivo_csv:
            writer = csv.writer(archivo_csv)
            columns = list(data.keys())
            writer.writerow(columns)
            for row in data.values():
                print(row)
                writer.writerow(str(row))
        time.sleep(1)  
if __name__ == "__main__":
    main()
