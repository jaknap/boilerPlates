import json
import requests

url='API-W/-KEY'
reponse = requests.get(url,  headers={"Content-Type": "application/json"})
dataCt = json.loads(reponse.text)

for data in jsonCategory:
    print(data['fields'])
