# TODO решите задачу

import json

INPUT_FILENAME = "input.json"


def task() -> float:
    with open(INPUT_FILENAME) as file_json:
        data = json.load(file_json)
    sum_ = sum([item["score"] * item["weight"] for item in data])
    return round(sum_, 3)


print(task())
