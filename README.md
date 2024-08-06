# Bedrock Claude3 Fine-Tuning

本リポジトリは，Amazon Bedrock 上で Claude3 Haiku を Fine-Tuning する際に利用したコードを公開しています．主に，データセット作成，前処理，モデルの評価のためのコードが含まれています．

> [!NOTE]
> Claude3 Haiku を Fine-Tuning し，モデルを評価した際の解説記事を Qiita に投稿しております．
> 是非そちらもご覧下さい！
> <br>[Amazon Bedrock で Claude3 Haiku を Fine-Tuning し，評価する](https://qiita.com/ren8k/items/XXXXXXXXXXXXXXXXXXXX)

## ディレクトリ構成

データセット・コードの説明などは，各ディレクトリ内の README.md を参照されたい．

```
├── dataset               : データセット格納ディレクトリ
│   ├── eval              : 評価データセット格納ディレクトリ
│   ├── preprocessed      : 前処理済みデータセット格納ディレクトリ
│   └── rawdata           : rawデータ格納ディレクトリ
├── requirements.txt
├── result: fine-tuning   : 結果格納ディレクトリ
│   ├── eval              : 評価結果格納ディレクトリ
│   │   ├── bert-score
│   │   └── llm-as-a-judge
│   └── fine-tuning       : Fine-Tuning 結果格納ディレクトリ
└── src                   : コード格納ディレクトリ
    ├── eval              : 評価コード格納ディレクトリ
    ├── inference         : 推論コード格納ディレクトリ
    └── prepare           : データセット作成, 前処理コード格納ディレクトリ
```
