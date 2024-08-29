import time
import boto3
import json


with open(file=r"parameters_sqs.json", mode="r", encoding="utf-8") as file:
    parameters = json.load(file)

client = boto3.client("sqs",
                      region_name=parameters["aws_region"],
                      aws_access_key_id=parameters["aws_key_id"],
                      aws_secret_access_key=parameters["aws_secret_key"])
queue_url = parameters["queue_url"]
matricula = input(" Capturar matrícula ")

timestamp = time.time()

response = client.send_message(
    QueueUrl=queue_url,
    MessageBody=json.dumps({
        "matricula": matricula,
        "timestamp": timestamp,
        "subject": "Mensaje de Prueba",
        "receiver": "carlos.mercury92@gmail.com",
        "content": "Hola ya andamos con todo"
    })
)

# print(response)
