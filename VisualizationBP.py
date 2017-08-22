import requests
import json
import pandas as pd
from altair import Chart

xAxisValue=[]
yAxisValue=[]


def main():
    url='API-W/-KEY'
    reponse = requests.get(url,  headers={"Content-Type": "application/json"})
    dataCt = json.loads(reponse.text)

    for data in jsonCategory:
        xAxisValue.append(data['fieldXaxis'])
        yAxisValue.append(data['fieldYaxis'])

    visualize(xAxisValue, yAxisValue)

def visualize( xAxis, yAxis ):
    data = pd.DataFrame({'xLabel': xAxis,
                         'yLabel': yAxis})
    chart=Chart(data).mark_point().encode(
        x='xLabel',
        y='yLabel'
    ).configure_cell(width=940, height=240)
    return chart.serve()


if __name__ == '__main__':
    main()