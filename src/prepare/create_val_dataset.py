import argparse
import json
from pprint import pprint

import boto3
from botocore.config import Config
from tool_config import ToolConfig


def get_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--region",
        type=str,
        default="us-west-2",
    )
    parser.add_argument(
        "--model-id",
        type=str,
        default="anthropic.claude-3-opus-20240229-v1:0",
    )
    parser.add_argument(
        "--order",
        type=str,
        default="LLM の Fine Tuning 用のデータセットを作成しなさい。",
    )
    parser.add_argument(
        "--input-doc-path",
        type=str,
        default="./amazon_bedrock_user_docs.pdf",
    )
    parser.add_argument(
        "--output-path",
        type=str,
        default="../../dataset/rawdata/validation.json",
    )

    return parser.parse_args()


def document_chat(region: str, model_id: str, prompt: str, doc_bytes: bytes) -> dict:
    retry_config = Config(
        region_name=region,
        connect_timeout=300,
        read_timeout=300,
        retries={
            "max_attempts": 10,
            "mode": "standard",
        },
    )
    client = boto3.client("bedrock-runtime", config=retry_config, region_name=region)
    messages = [
        {
            "role": "user",
            "content": [
                {
                    "document": {
                        "name": "Document",
                        "format": "pdf",
                        "source": {"bytes": doc_bytes},
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
        inferenceConfig={
            "maxTokens": 3000,
        },
        toolConfig={
            "tools": [ToolConfig.tool_definition],
            "toolChoice": {
                "tool": {
                    "name": ToolConfig.tool_name,
                },
            },
        },
    )
    pprint(response)
    return response


def extract_tool_use_args(content: list) -> dict:
    for item in content:
        if "toolUse" in item:
            return item["toolUse"]["input"]
    raise ValueError("toolUse not found in response content")


def main(args: argparse.Namespace) -> None:
    prompt = f"""
    <text>
    {args.order}
    </text>

    {ToolConfig.tool_name} ツールのみを利用すること。
    """
    print(prompt)

    with open(args.input_doc_path, "rb") as f:
        doc_bytes = f.read()

    # call converse API
    response: dict = document_chat(args.region, args.model_id, prompt, doc_bytes)
    response_content: list = response["output"]["message"]["content"]

    # extract json
    tool_use_args = extract_tool_use_args(response_content)

    # write to file
    with open(args.output_path, "w") as f:
        json.dump(tool_use_args["dataset"], f, indent=2, ensure_ascii=False)


if __name__ == "__main__":
    args = get_args()
    main(args)
