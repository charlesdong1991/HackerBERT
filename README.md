# HackerBERT

This is a simple demonstration to combine BERT with elasticsearch to improve
search quality.

![](gh_demo.gif)

All setups are composed using Docker. In order to replicate the project, please
 just follow the steps below:
 
- Download HackerNews public data from Google BigQuery Public Dataset, and save
it locally and set the path to dataset as environment variable:
```
export DATA_PATH=path_to_your_csv
```
 
- Download the BERT pre-trained embeddings. There are many pre-trained embeddings
available, for instance, you could use `wget`:
```
wget https://storage.googleapis.com/bert_models/2018_10_18/cased_L-12_H-768_A-12.zip
```
And then `unzip` the folder, and set the absolute path of the folder as environment
variable `MODEL_PATH`.

```
export MODEL_PATH=path_to_your_pretrained_model
```

- Create search index for elasticsearch, to make elasticsearch work, an index
is needed to find search items, so simply do
```
export SEARCH_INDEX=any_search_index_name
```

- Move into the cloned repo, build and run dockers, there is the `docker-compose` file which composes of 
several dockers:
```
cd HackerBERT
docker-compose build
docker-compose up
```

- Create search indexes:
```
python main.py
```

- Play with it on `http://127.0.0.1:1111`
