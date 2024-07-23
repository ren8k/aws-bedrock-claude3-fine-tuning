# Fine-Tuning

## TODO

- [ ] データセットの調査
- [ ] データセットの作成
- [ ] Fine-Tuning Job の実行
  - model name: claude-3-haiku-ft-model
  - job name: claude-3-haiku-ft-job
- [ ] 評価してみたい
- [ ] 検証結果ブログの執筆

## Survey

- 語尾が「ござる」
  - https://huggingface.co/datasets/bbz662bbz/databricks-dolly-15k-ja-gozaru?row=99
  - https://qiita.com/jovyan/items/c727392d6d6030433f84
- Amazon Bedrock の QA
  - https://aws.amazon.com/jp/blogs/machine-learning/improve-rag-accuracy-with-fine-tuned-embedding-models-on-amazon-sagemaker/
  - https://github.com/aws-samples/fine-tune-embedding-models-on-sagemaker/blob/main/sentence-transformer/multiple-negatives-ranking-loss/training.json
  - でもこれ 85 件しかない。
- NVIDIA のブログ
  - https://resources.nvidia.com/ja-jp-llm-developer-day/how-to-use-peft-on-nemo-framework?ncid=no-ncid

## Memo

微調整のパフォーマンスを最適化するには、データセットのサイズよりもトレーニング データの品質の方が重要です。モデルを微調整してパフォーマンスを評価するには、小規模ながらも高品質のトレーニング データセット (50 ～ 100 行のデータから始めるのが妥当です) から始めることをお勧めします。評価結果に基づいて、トレーニング データを反復して改良することができます。一般に、高品質のトレーニング データのサイズが大きくなるにつれて、微調整されたモデルからより優れたパフォーマンスが得られることが期待できます。ただし、データの品質に重点を置くことが重要です。大規模でも品質の低いデータセットでは、微調整されたモデルのパフォーマンスが期待どおりに向上しない可能性があるためです。

## Map

- まずは、85-15 件で split して、学習させてみるか。
  - 15 件分の validation dataset は、自作するか、、
  - tool use の利用

## References

- https://github.com/aws-samples/aws-ml-jp/pull/66
- https://aws.amazon.com/jp/blogs/news/cost-efficiency-of-api-and-oss-generative-ai/
- https://www.perplexity.ai/search/llmnofine-tuningwoxing-uji-nil-LXDILLZ.Q4ukZ9pY66Tnpg
- https://www.perplexity.ai/search/llmwofine-tuningsurukotote-jin-h8DcckwlSg6e_1ZoY.2SVA

### qiita

- https://qiita.com/revsystem/items/303487a39eea5924187c
- https://qiita.com/ren8k/items/3d5f66df251703b8407e
- https://qiita.com/kazuneet/items/9b0dc3c37cc33f7b61d6
- https://qiita.com/moritalous/items/ff2763bcd9408a1b395a
