import argparse
import json

from langchain.evaluation import Criteria, EvaluatorType, load_evaluator
from langchain_aws import ChatBedrock


def get_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--prediction-file",
        type=str,
        default="../../dataset/eval/fine-tuning-model_prediction.json",
    )
    parser.add_argument(
        "--label-file",
        type=str,
        default="../../dataset/eval/label.json",
    )
    return parser.parse_args()


def load_json(file_path: str) -> list:
    with open(file_path, "r") as f:
        return json.load(f)


def main(args: argparse.Namespace) -> None:
    predictions = load_json(args.prediction_file)
    labels = load_json(args.label_file)

    model = ChatBedrock(
        model_id="anthropic.claude-3-5-sonnet-20240620-v1:0",
        region_name="us-east-1",
        model_kwargs={
            "temperature": 0.0,
        },
    )

    evaluator = load_evaluator(
        evaluator=EvaluatorType.LABELED_SCORE_STRING,
        criteria=Criteria.CORRECTNESS,
        llm=model,
    )

    scores = []
    for prediction, label in zip(predictions, labels):
        # print(f"Prediction: {prediction}, Label: {label}")
        eval_result = evaluator.evaluate_strings(
            prediction=prediction["answer"],
            reference=label["answer"],
            input=label["question"],
        )
        print(eval_result)
        print(eval_result["score"])
        scores.append(eval_result["score"])

    score_average = sum(scores) / len(scores)
    print(f"Average score: {score_average}")


if __name__ == "__main__":
    args = get_args()
    main(args)
