#!/bin/bash

PREDICTION_FILE="../../dataset/eval/base-model_prediction.json"

python3 evaluate.py \
    --prediction-file $PREDICTION_FILE
