#!/bin/bash

PREDICTION_FILE="./eval_data/base-model_prediction.json"

python3 evaluate.py \
    --prediction-file $PREDICTION_FILE
