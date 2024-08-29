import json
from src.consumer import consumer_sqs

with open(file=r"parameters_sqs.json", mode="r", encoding="utf-8") as file:
    parameters = json.load(file)


def run():
    print("Running")
    consumer_sqs(parameters)


if __name__ == "__main__":
    run()