#!/bin/sh
bert-serving-start -num_worker=1 -model_dir /model -cpu -max_batch_size 16
