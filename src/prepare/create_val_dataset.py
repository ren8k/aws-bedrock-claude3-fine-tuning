description = """
与えられるドキュメントに基づいて、LLMのFine-Tuning用のValidationデータセットを作成します。
具体的には、ドキュメントの内容を利用し、Amazon Bedrockに関する質問文と回答文のペアを生成します。

<example>
question: What is Amazon Bedrock and its key features?
answer: Amazon Bedrock is a fully managed service that offers a choice of high-performing foundation models along with a broad set of capabilities for building generative AI applications, simplifying development with security, privacy, and responsible AI features.
</example>

<rules>
- 必ず15個の質問文と回答文のペアを生成すること。
- 英語で回答すること。
- Amazon Bedrockについて、多様な質問と回答を作成すること。
</rules>
"""
tool_name = "QA_dataset_generator"

tool_definition = {
    "toolSpec": {
        "name": tool_name,
        "description": description,
        "inputSchema": {
            "json": {
                "type": "object",
                "properties": {
                    "dataset": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "question": {
                                    "type": "string",
                                    "description": "Validationデータ用の質問文。",
                                },
                                "answer": {
                                    "type": "string",
                                    "description": "Validationデータ用の回答文。",
                                },
                            },
                            "required": ["question", "answer"],
                        },
                        "description": "Validationデータ用の質問文と回答文のセット。必ず15個生成すること。",
                    },
                },
                "required": ["dataset"],
            }
        },
    }
}

import json
from pprint import pprint

import boto3

client = boto3.client("bedrock-runtime", region_name="us-west-2")
model_id = "anthropic.claude-3-opus-20240229-v1:0"

input_document = "./amazon_bedrock_user_docs.pdf"
input_text = "LLM の Fine Tuning 用のデータセットを作成しなさい。"
prompt = f"""
<text>
{input_text}
</text>

{tool_name} ツールのみを利用すること。
"""
print(prompt)

with open(input_document, "rb") as f:
    document_bytes = f.read()

messages = [
    {
        "role": "user",
        "content": [
            {
                "document": {
                    "name": "Document",
                    "format": "pdf",
                    "source": {"bytes": document_bytes},
                }
            },
            {"text": prompt},
        ],
    }
]

# Send the message to the model
response = client.converse(
    modelId=model_id,
    messages=messages,
    toolConfig={
        "tools": [tool_definition],
        "toolChoice": {
            "tool": {
                "name": tool_name,
            },
        },
    },
)
pprint(response)


def extract_tool_use_args(content):
    for item in content:
        if "toolUse" in item:
            return item["toolUse"]["input"]
    return None


response_content = response["output"]["message"]["content"]

# json部を抽出
tool_use_args = extract_tool_use_args(response_content)
print(json.dumps(tool_use_args, indent=2, ensure_ascii=False))

# ファイルに書き出し
with open("../../dataset/rawdata/validation.json", "w") as f:
    json.dump(tool_use_args["dataset"], f, indent=4, ensure_ascii=False)
