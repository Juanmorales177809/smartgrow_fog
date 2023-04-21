import os, json
import time
import re, subprocess



url = "10.220.85.148"
cmd="curl -s -k " + url
longitud_de_onda = ['410','435','460','485','510','535','560','585','610','645','680','705','730','760','810','860','900','940']
def regularizar(arr):
    patron = r'\d+\.\d+'
    lista1 = re.findall(patron,arr['variables']['ABC'])
    lista2 = re.findall(patron,arr['variables']['DEF'])
    lista3 = re.findall(patron,arr['variables']['GHR'])
    lista4 = re.findall(patron,arr['variables']['ISJ'])
    lista5 = re.findall(patron,arr['variables']['TUV'])
    lista6 = re.findall(patron,arr['variables']['WKL'])
    return lista1+lista2+lista3+lista4+lista5+lista6

def generate(data):
    output = 0
    while not output:
        result = subprocess.Popen(["curl", url], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, errors = result.communicate() 
        print("esperando datos...")
    
    arr = json.loads(output)
    data["410 [nm]"] = regularizar(arr)[0] ; data["435 [nm]"] = regularizar(arr)[1]
    data["460 [nm]"] = regularizar(arr)[2] ; data["485 [nm]"] = regularizar(arr)[3]
    data["510 [nm]"] = regularizar(arr)[4] ; data["535 [nm]"] = regularizar(arr)[5]
    data["560 [nm]"] = regularizar(arr)[6] ; data["585 [nm]"] = regularizar(arr)[7]
    data["610 [nm]"] = regularizar(arr)[8] ; data["645 [nm]"] = regularizar(arr)[9]
    data["680 [nm]"] = regularizar(arr)[10] ; data["705 [nm]"] = regularizar(arr)[11]
    data["730 [nm]"] = regularizar(arr)[12] ; data["760 [nm]"] = regularizar(arr)[13]
    data["810 [nm]"] = regularizar(arr)[14] ; data["860 [nm]"] = regularizar(arr)[15]
    data["900 [nm]"] = regularizar(arr)[16] ; data["940 [nm]"] = regularizar(arr)[17]
    data['timestamp'] = time.time()
    

def main():
    data = {
        "device_id": 'AS7265X',
        "location": "chamber_1",
        "sensor_type": "spectrophotometer",
        "410 [nm]": 0, "435 [nm]": 0, "460 [nm]": 0, "485 [nm]": 0,
        "510 [nm]": 0, "535 [nm]": 0, "560 [nm]": 0, "585 [nm]": 0,
        "610 [nm]": 0, "645 [nm]": 0, "680 [nm]": 0, "705 [nm]": 0,
        "730 [nm]": 0, "760 [nm]": 0, "810 [nm]": 0, "860 [nm]": 0,
        "900 [nm]": 0, "940 [nm]": 0,
        "timestamp": time.time()
    }
    
    while True:
        generate(data)
        with open('output_as7265x.json','a') as output_file:
            output_file.write(f'{json.dumps(data)}\n')
        time.sleep(0.5)


if __name__ == "__main__":
    main()