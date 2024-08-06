# Training loss, Validation loss の観察

以下を実行すると，各 loss の推移を png で保存できる．

```bash
python3 observe_loss.py
```

# 評価データセットの作成方法

`dataset/rawdata/training.json`を入力として，以下のプロンプトを利用して，Claude3.5 Sonnet で作成した．

```

与えられた training.json を基に，LLM の fine-tuning の評価を行うための，評価データセットを作成して下さい．具体的には、ドキュメントの内容を利用し、Amazon Bedrock に関する質問文と回答文のペアを JSON 形式で生成します。

<example>
question: What is Amazon Bedrock and its key features?
answer: Amazon Bedrock is a fully managed service that offers a choice of high-performing foundation models along with a broad set of capabilities for building generative AI applications, simplifying development with security, privacy, and responsible AI features.
</example>

質問文は以下の 4 つとして，回答を生成しなさい．

<question>
- What can you do with Amazon Bedrock?
- What is Knowledge Bases for Amazon Bedrock?
- What are Agents for Amazon Bedrock?
- What are Guardrails for Amazon Bedrock?
</question>

<rules>
- 150~200token程度で，英語で回答しなさい．
- JSON形式で回答すること．
- JSONのキーとして，questionとanswerを含むこと．
- 箇条書きは利用しないで下さい．
</rules>

```

# 評価方法

## LLM-as-a-Judge

`eval_llm_as_a_judge.py` を実行することで，モデルの推論結果と[ラベル（想定回答）](https://github.com/ren8k/aws-bedrock-claude3-fine-tuning/blob/main/dataset/eval/label.json)を比較した際の正確性を評価を LLM-as-a-Judge で行うことができる．例えば，fine-tuning を行っていないモデルを評価する場合，以下のコマンドを実行する（fine-tuning を行ったモデルを評価する場合，引数指定は不要）．なお，以下のコマンドは `run_evaluate.sh` に記載されている．

```bash
#!/bin/bash

PREDICTION_FILE="./eval_data/base-model_prediction.json"

python3 eval_llm_as_a_judge.py \
    --prediction-file $PREDICTION_FILE
```

## BERTScore

`eval_bert_score.py` を実行することで，モデルの推論結果と[ラベル（想定回答）](https://github.com/ren8k/aws-bedrock-claude3-fine-tuning/blob/main/dataset/eval/label.json)を比較した際の正確性を評価を BERTScore で行うことができる．利用方法は上記と同様．

# 参考

- [Scoring Evaluator](https://python.langchain.com/v0.1/docs/guides/productionization/evaluation/string/scoring_eval_chain/)
- [langchain.evaluation.loading.load_evaluator](https://api.python.langchain.com/en/latest/evaluation/langchain.evaluation.loading.load_evaluator.html)
- [langchain.evaluation.schema.EvaluatorType](https://api.python.langchain.com/en/latest/evaluation/langchain.evaluation.schema.EvaluatorType.html#langchain.evaluation.schema.EvaluatorType)
- [langchain.evaluation.criteria.eval_chain.Criteria](https://api.python.langchain.com/en/latest/evaluation/langchain.evaluation.criteria.eval_chain.Criteria.html)
- [すごいぞ Langfuse！トークン数計算機能と評価機能を検証](https://qiita.com/moritalous/items/e07448ec0ec5e0132276)
