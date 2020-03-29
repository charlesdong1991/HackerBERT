import os

import pandas as pd
from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk
from bert_serving.client import BertClient

from utils import reconstruct_dataframe, create_document, bulk_predict

SEARCH_INDEX = os.environ["SEARCH_INDEX"]
INDEX_SETUP = "index_setup.json"
DATA_PATH = os.environ['DATA_PATH']


def main():
    df_hackernews = pd.read_csv(DATA_PATH)
    es = Elasticsearch()
    bc = BertClient(check_version=False, output_fmt="list", check_length=False)

    # delete old search index if there is, and create new search index
    es.indices.delete(index=SEARCH_INDEX, ignore=[404])
    with open(INDEX_SETUP) as f:
        source = f.read().strip()
        es.indices.create(index=SEARCH_INDEX, body=source)

    # reconstruct dataset to be able to bulk predict
    docs = reconstruct_dataframe(df_hackernews)

    documents = []
    for doc, embedding in zip(docs, bulk_predict(bc, docs)):
        document = create_document(doc, embedding, SEARCH_INDEX)
        documents.append(document)

    bulk(es, documents)


if __name__ == "__main__":
    main()
