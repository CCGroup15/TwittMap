from flask import Flask, render_template, request
import config
import json

application = Flask(__name__)

@application.route('/')
def say_hello():
    def index():
        coords = []
        return render_template("index.html", coords=json.dumps(coords))
    return render_template('index.html')

@application.route('/result', methods = ['GET'])
def result():
    if request.method == 'GET':
        category = request.args.getlist("category")
        # print(category)
        coords = []
        for keyword in category:
            es_data = config.es.search(index=config.AWS_ES_INDEX, body={"query": {"match": {"text": keyword}}}, size=600)
            for data in es_data['hits']['hits']:
                if len(data['_source']['coordinates']) > 0:
                    geo_data = data['_source']['coordinates']['location'].split(',')
                    lat = float(geo_data[0])
                    lng = float(geo_data[1])
                    coords.append([lat, lng])
        print(coords)
        return render_template("render.html", coords=json.dumps(coords))

if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = True
    application.run()
