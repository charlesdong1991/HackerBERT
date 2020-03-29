def reconstruct_dataframe(df):
    """Reconstruct dataframe row by row and convert to list of dictionaries
    """
    docs = []
    for row in df.itertuples():
        doc = {
            "title": row.title,
            "text": row.text,
            "url": row.url
        }
        docs.append(doc)
    return docs


def create_document(doc, embedding, index_name):
    """Format document"""
    return {
        "_op_type": "index",
        "_index": index_name,
        "text": doc["text"],
        "title": doc["title"],
        "url": doc["url"],
        "text_vector": embedding
    }


def bulk_predict(bc, docs, batch_size=16):
    """Make bulk prediction"""
    for i in range(0, len(docs), batch_size):
        batch_docs = docs[i: i+batch_size]
        embeddings = bc.encode([doc["text"] for doc in batch_docs])
        for embedding in embeddings:
            yield embedding
