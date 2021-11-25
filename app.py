from pprint import pprint as pp
from flask import Flask, render_template, request
from weather import query_api
from config import Config

app = Flask(__name__)


@app.route('/')
@app.route('/', methods=['POST'])
def index():
    data = []
    error = None
    if request.method == 'POST':
        city1 = request.form.get('city1')
        city2 = request.form.get('city2')
        city3 = request.form.get('city3')
        for c in (city1, city2, city3):
            resp = query_api(c)
            pp(resp)
            if resp:
                data.append(resp)
        if len(data) != 3:
            error = 'Did not get complete response from Weather API'
    return render_template("weather.html",
                           data=data,
                           error=error)


if __name__ == "__main__":
    app.run(host='127.0.0.5', port=5001, debug=True)
