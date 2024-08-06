# データセット作成方法

`create_val_dataset.py` を実行し，検証データを作成する．具体的には，Amazon Bedrock FAQs のデータを利用し，検証データを Bedrock Converse API の Document chat と Json mode を利用して，JSON 形式の QA データを作成する．

```bash
python3 create_val_dataset.py
```

# データセットのフォーマット

`preprocess.py` を実行し，データセットを前処理する．具体的には，以下のような，Claude3 Haiku が学習できる形式に変換する．

```
{"system": string, "messages": [{"role": "user", "content": string}, {"role": "assistant", "content": string}]}
{"system": string, "messages": [{"role": "user", "content": string}, {"role": "assistant", "content": string}]}
{"system": string, "messages": [{"role": "user", "content": string}, {"role": "assistant", "content": string}]}
```

## 検証データの場合

```bash
python3 preprocess.py
```

## 訓練データの場合

```bash
bash run_preprocess.sh
```

# データセットの検証（Data Validation）

```bash
python3 data_validation.py
```
