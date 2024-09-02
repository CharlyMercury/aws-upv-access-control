import json
from src.producer import producer_sqs

with open(file=r"parameters_sqs.json", mode="r", encoding="utf-8") as file:
    parameters = json.load(file)


def run():
    print("\t\t---Control de Acceso---\n\t---Metodología de la programación---\n")
    producer_sqs(parameters)


if __name__ == "__main__":
    run()