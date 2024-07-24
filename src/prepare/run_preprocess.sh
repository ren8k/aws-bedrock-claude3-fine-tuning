#!/bin/bash

INPUT="../../dataset/rawdata/training.json"
OUTPUT="../../dataset/preprocessed/claude3_ft_training.jsonl"
PROMPT_KEY="sentence1"
COMPLETION_KEY="sentence2"

python3 preprocess.py \
    --input-file $INPUT \
    --output-file $OUTPUT \
    --prompt-key $PROMPT_KEY \
    --completion-key $COMPLETION_KEY
