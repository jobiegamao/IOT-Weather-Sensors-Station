from flask import Flask, render_template, request
import threading
from search import getAverageGraph
from weatherWarnings import warningMessages
from generate import generate_graphs

app = Flask(__name__)


@app.route('/')
def home():

    date1 = request.args.get('date1', default=0)
    date2 = request.args.get('date2', default=0)

    if date1 == 0:
        warn = warningMessages()
        return render_template("index.html", warn=warn)

    getAverageGraph(date1, date2)

    return render_template("search.html", start=date1, end=date2)


def generate_graphs_thread():
    while True:
        generate_graphs()


if __name__ == '__main__':
    generate_thread = threading.Thread(target=generate_graphs_thread)
    generate_thread.start()

    app.run(debug=True, port=8000)
