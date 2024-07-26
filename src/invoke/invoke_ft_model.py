import json

import boto3

model_id = "<import model arn>"

system_prompt = "You are a high-performance QA assistant that responds to questions concisely, accurately, and appropriately."
prompt = "hogehoge"

client = boto3.client(service_name="bedrock-runtime", region_name="us-west-2")

response = client.invoke_model(
    body=json.dumps(
        {
            "anthropic_version": "bedrock-2023-05-31",
            "max_tokens": 2048,
            "messages": [{"role": "user", "content": f"{prompt}"}],
            "temperature": 0.1,
            "top_p": 0.9,
            "system": f"{system_prompt}",
        }
    ),
    modelId=model_id,
)
output = response.get("body").read().decode("utf-8")
response_body = json.loads(output)
response_text = response_body["outputs"][0]["text"]
print(response_text)
