import os

from flask import Flask, render_template, jsonify, request
from elasticsearch import Elasticsearch
from bert_serving.client import BertClient

SEARCH_INDEX = os.environ["SEARCH_INDEX"]
TEMPLATE = "hackernews.html"
BERT_CLIENT_IP = "bertserving"
SEARCH_SIZE = 10

app = Flask(__name__)


@app.route("/")
def index():
    return render_template(TEMPLATE)


@app.route("/search")
def find_similar_news():
    bc = BertClient(ip=BERT_CLIENT_IP, output_fmt="list", check_version=False)
    es = Elasticsearch("elasticsearch:9200")

    query = request.args.get("q")
    query_vector = bc.encode([query])[0]

    script_query = {
        "script_score": {
            "query": {"match_all": {}},
            "script": {
                "source": "cosineSimilarity(params.query_vector, doc['text_vector']) + 1.0",
                "params": {"query_vector": query_vector}
            }
        }
    }

    response = es.search(
        index=SEARCH_INDEX,
        body={
            "size": SEARCH_SIZE,
            "query": script_query,
            "_source": {"includes": ["title", "text", "url"]}
        }
    )
    return jsonify(response)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=1111)
