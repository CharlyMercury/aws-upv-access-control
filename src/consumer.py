import json
import boto3
from src.send_email import SendEmail
import logging

logger = logging.getLogger("main_consumer")
logger.setLevel(logging.INFO)


def consumer_sqs(parameters):

    client = boto3.client("sqs",
                        region_name=parameters["aws_region"],
                        aws_access_key_id=parameters["aws_key_id"],
                        aws_secret_access_key=parameters["aws_secret_key"])
    queue_url = parameters["queue_url"]

    send_email_instance = SendEmail()

    while True:

        response = client.receive_message(
            QueueUrl=queue_url,
            MaxNumberOfMessages=10,
            VisibilityTimeout=60,
            WaitTimeSeconds=20,
        )

        if "Messages" not in response:
            logger.info('------------------------')
            logger.info("La cola ESTÁ vacía")
            logger.info('------------------------')
        else:
            for message in response["Messages"]:
                message_body = json.loads(message['Body'])
                logger.info('------------------------')
                logger.info(message_body)
                logger.info('------------------------')
                send_email_instance.create_email(message_body)

                response_delete = client.delete_message(
                    QueueUrl=queue_url,
                    ReceiptHandle=message["ReceiptHandle"]
                )
