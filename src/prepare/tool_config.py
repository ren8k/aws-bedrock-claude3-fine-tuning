class ToolConfig:
    tool_name = "QA_dataset_generator"
    no_of_dataset = 32

    description = f"""
    与えられるドキュメントに基づいて、LLMのFine-Tuning用のValidationデータセットを作成します。
    具体的には、ドキュメントの内容を利用し、Amazon Bedrockに関する質問文と回答文のペアを生成します。

    <example>
    question: What is Amazon Bedrock and its key features?
    answer: Amazon Bedrock is a fully managed service that offers a choice of high-performing foundation models along with a broad set of capabilities for building generative AI applications, simplifying development with security, privacy, and responsible AI features.
    </example>

    <rules>
    - 必ず{no_of_dataset}個の質問文と回答文のペアを生成すること。
    - 英語で回答すること。
    - JSON形式で回答すること。
    - Amazon Bedrockについて、多様な質問と回答を作成すること。
    </rules>
    """

    tool_definition = {
        "toolSpec": {
            "name": tool_name,
            "description": description,
            "inputSchema": {
                "json": {
                    "type": "object",
                    "properties": {
                        "dataset": {
                            "description": f"Validationデータ用の質問文と回答文のセット。必ず{no_of_dataset}個生成すること。",
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
                        },
                    },
                    "required": ["dataset"],
                }
            },
        }
    }
