import argparse
import json

from bert_score import score


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


def get_target_sentences(qa_list: list) -> list:
    sentences = []
    for qa in qa_list:
        sentences.append(qa["answer"])
    return sentences


def calc_bert_score(cands: list, refs: list) -> tuple:
    Precision, Recall, F1 = score(cands, refs, lang="ja", verbose=True)
    return Precision.numpy().tolist(), Recall.numpy().tolist(), F1.numpy().tolist()


def bert_score(predictions: list, labels: list) -> None:
    cands = get_target_sentences(predictions)
    refs = get_target_sentences(labels)

    P, R, F1 = calc_bert_score(cands, refs)
    for p, r, f1 in zip(P, R, F1):
        print(f"precision: {p}, recall: {r}, f1_score: {f1}")

    print(f"Average precision: {sum(P) / len(P)}")
    print(f"Average recall: {sum(R) / len(R)}")
    print(f"Average f1_score: {sum(F1) / len(F1)}")


def main(args: argparse.Namespace) -> None:
    predictions = load_json(args.prediction_file)
    labels = load_json(args.label_file)

    bert_score(predictions, labels)


if __name__ == "__main__":
    args = get_args()
    main(args)
