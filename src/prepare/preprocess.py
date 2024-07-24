import argparse
import json


def get_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--system-prompt",
        type=str,
        default="You are a high-performance QA assistant that responds to questions concisely, accurately, and appropriately.",
    )
    parser.add_argument(
        "--input-file",
        type=str,
        default="../../dataset/rawdata/validation.json",
    )
    parser.add_argument(
        "--output-file",
        type=str,
        default="../../dataset/preprocessed/claude3_ft_validation.jsonl",
    )
    parser.add_argument("--prompt-key", type=str, default="question")
    parser.add_argument("--completion-key", type=str, default="answer")

    return parser.parse_args()


def preprocess(args: argparse.Namespace) -> None:
    """
    Preprocess the input JSON file to the format that can be used for claude3's fine-tuning.
    Input JSON file should have the structure of a list of dictionaries.
    Below is an example of the input JSON file.
    [
        {
            "question": "What is the capital of France?",
            "answer": "Paris"
        },
        ...
    ]
    """
    with open(args.input_file, "r") as f_in, open(args.output_file, "w") as f_out:
        input_json = json.load(f_in)
        for data in input_json:
            prompt = data[args.prompt_key]
            completion = data[args.completion_key]

            new_data = {}
            new_data["system"] = args.system_prompt
            new_data["messages"] = [
                {"role": "user", "content": prompt},
                {"role": "assistant", "content": completion},
            ]

            f_out.write(json.dumps(new_data) + "\n")


def main(args: argparse.Namespace) -> None:
    preprocess(args)
    print("Conversion completed!")


if __name__ == "__main__":
    args = get_args()
    main(args)
