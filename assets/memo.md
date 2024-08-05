# Fine-Tuning

## TODO

- [x] データセットの調査
- [x] データセットの作成
- [x] Fine-Tuning Job の実行
  - model name: claude-3-haiku-ft-model
  - job name: claude-3-haiku-ft-job
  - role: claude-3-haiku-ft-role
- [x] 評価してみたい
- [ ] 検証結果ブログの執筆
  - [x] create_val_dataset.py のリファクタリング

## Survey (fine-tuning の検証)

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

## Strategy

- まずは、85-15 件で split して、学習させてみるか。

  - 15 件分の validation dataset は、自作するか、、
  - tool use の利用

- 普通に 1 時間の試行で 2 万円かかるので、慎重に行いたい。
- 想定シナリオとしては以下。
  - きちんと FT できている
  - FT の効果が見られない。
- 上記の効果を見極められる評価用データセットを作成しないといけない。

### プロビジョンスループットの参考

No commitment で 50 分で検証を行うこと！

- https://qiita.com/minorun365/items/4c5f69e120898179347d
- https://dev.classmethod.jp/articles/bedrock-pt-min-unit/

## References

- https://github.com/aws-samples/aws-ml-jp/pull/66
- https://aws.amazon.com/jp/blogs/news/cost-efficiency-of-api-and-oss-generative-ai/
- https://www.perplexity.ai/search/llmnofine-tuningwoxing-uji-nil-LXDILLZ.Q4ukZ9pY66Tnpg
- https://www.perplexity.ai/search/llmwofine-tuningsurukotote-jin-h8DcckwlSg6e_1ZoY.2SVA

### PFN の LLM の LoRA のブログ

- https://tech.preferred.jp/ja/blog/llm-fine-tuning-for-domain-knowledge/

> ここで、本来ドメイン知識は医療や法律といった特定のドメインに関する知識のことですが、実験設定を考慮し、事前学習データに含まれていないであろう日本語における知識を指すこととします。

- その他
  - https://www.ariseanalytics.com/activities/report/20240419-2/

### AWS Blog(Claude3 fine-tuning)

- [whats-news](https://aws.amazon.com/jp/about-aws/whats-new/2024/07/fine-tuning-anthropics-claude-3-haiku-bedrock-preview/)
- [Fine-tune Anthropic’s Claude 3 Haiku in Amazon Bedrock to boost model accuracy and quality](https://aws.amazon.com/jp/blogs/machine-learning/fine-tune-anthropics-claude-3-haiku-in-amazon-bedrock-to-boost-model-accuracy-and-quality/)
- [モデルのカスタマイズがサポートされている地域とモデル](https://docs.aws.amazon.com/bedrock/latest/userguide/custom-model-supported.html)
- https://aws.amazon.com/jp/blogs/machine-learning/few-shot-prompt-engineering-and-fine-tuning-for-llms-in-amazon-bedrock/

### 評価の部分

- https://qiita.com/moritalous/items/e07448ec0ec5e0132276

### qiita

- https://qiita.com/revsystem/items/303487a39eea5924187c
- https://qiita.com/moritalous/items/8d8e6b91c7289692644a
- https://qiita.com/moritalous/items/ff2763bcd9408a1b395a
- https://qiita.com/ren8k/items/3d5f66df251703b8407e
- https://qiita.com/kazuneet/items/9b0dc3c37cc33f7b61d6

### ft のメリット

- 最小限のコンテキストのみで良いので，コストが低い
- 低レイテンシー

- PT は 10 分程度で利用可能になった。
- 2epoch だけだど全く学習できてない模様
  - 10epoch, early stopping で試してみた
  - これで駄目なら、データセット不足かも。
  - もう少しデータセットを増やしてみるか、英語で聞いて比較してみるか。
  - うまくいきそうだけどね。
