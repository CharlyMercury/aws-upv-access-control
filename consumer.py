import json
import boto3
from send_email import SendEmail


with open(file=r"parameters_sqs.json", mode="r", encoding="utf-8") as file:
    parameters = json.load(file)

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
        print("La cola ESTÁ vacía")
    else:
        for message in response["Messages"]:
            message_body = json.loads(message['Body'])
            # print(message_body)
            send_email_instance.create_email(message_body)

            response_delete = client.delete_message(
                QueueUrl=queue_url,
                ReceiptHandle=message["ReceiptHandle"]
            )
