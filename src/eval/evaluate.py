# https://python.langchain.com/v0.1/docs/guides/productionization/evaluation/string/scoring_eval_chain/

from langchain.evaluation import load_evaluator
from langchain_aws import ChatBedrock

accuracy_criteria = {
    "accuracy": """
Score 1: The answer is completely unrelated to the reference.
Score 3: The answer has minor relevance but does not align with the reference.
Score 5: The answer has moderate relevance but contains inaccuracies.
Score 7: The answer aligns with the reference but has minor errors or omissions.
Score 10: The answer is completely accurate and aligns perfectly with the reference."""
}

input = "What can you do with Amazon Bedrock?"

prediction = """Amazon Bedrock is a fully managed service that provides a quick, effective, and secure path to building generative AI applications powered by foundation models from Amazon, Anthropic, Stability AI, Cohere, and other integrated providers. It simplifies the creation and deployment of cutting-edge customized models and foundational models for a wide range of natural language processing (NLP), text-to-image, and speech-to-text use cases, all while focusing on security, data privacy, and responsible AI."""


label = """Amazon Bedrock is a versatile platform that enables developers to harness the power of generative AI for a wide range of applications. With Bedrock, you can access high-performance foundation models from leading providers and customize them for specific use cases. The platform supports various tasks such as content creation, image generation, personalized recommendations, text summarization, and code generation. Bedrock also offers tools for responsible AI development, including model evaluation and content filtering. Its serverless architecture and integration with other AWS services make it easy to build, deploy, and scale generative AI applications securely. Whether you're working on natural language processing, creative projects, or industry-specific solutions, Amazon Bedrock provides the infrastructure and capabilities to bring your generative AI ideas to life."""


model = ChatBedrock(
    model_id="anthropic.claude-3-5-sonnet-20240620-v1:0",
    region_name="us-east-1",
    model_kwargs={
        "temperature": 0.0,
    },
)

evaluator = load_evaluator(
    "labeled_score_string",
    criteria=accuracy_criteria,
    llm=model,
)

# Correct
eval_result = evaluator.evaluate_strings(
    prediction=prediction,
    reference=label,
    input=input,
)
print(eval_result)
