import json
from src.consumer import consumer_sqs
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)-8s %(message)s', datefmt='%a, %d %b %Y %H:%M:%S', filename='/home/edumediatics/aws-upv-access-control/consumer.log', filemode='w')   


with open(file=r"parameters_sqs.json", mode="r", encoding="utf-8") as file:
    parameters = json.load(file)


def run():
    logging.info("Running")
    consumer_sqs(parameters)


if __name__ == "__main__":
    run()