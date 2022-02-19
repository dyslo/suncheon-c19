from flask import Flask, request, abort
import requests, json
from datetime import datetime, timedelta

app = Flask(__name__)

@app.route("/c19_suncheon", methods=['GET'])
def c19_suncheon():
    if(request.method == "GET"):
        stdt = request.args.get('stdt')
        eddt = request.args.get('eddt')
        #(datetime.today() - timedelta(1)).strftime("%Y-%m-%d")
        response = requests.post("https://www.suncheon.go.kr/kr/main/disease/road_page.do", data = {'mode':'chart', 'chartStDt': stdt, 'chartEdDt': eddt})
        data = json.loads(response.content)
        return data

app.run(host="0.0.0.0", port="5000", debug=True)