#!/bin/bash

PREDICTION_FILE="../../dataset/eval/base-model_prediction.json"

python3 eval_llm_as_a_judge.py \
    --prediction-file $PREDICTION_FILE
