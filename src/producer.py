import time
import boto3
import json


def producer_sqs(parameters):

    client = boto3.client("sqs",
                        region_name=parameters["aws_region"],
                        aws_access_key_id=parameters["aws_key_id"],
                        aws_secret_access_key=parameters["aws_secret_key"])
    queue_url = parameters["queue_url"]

    course = " Metodología de la programación "
    subject = f" Asistencia al curso: {course}. "
    day_objective = """
    <h4> Objetivos del Día:</h4>
    <ul> 
        <li>Definir qué es un algoritmo.</li>
        <li>Identificar ejemplos de algoritmos en la vida diaria.</li>
    </ul>
    """
    email_termination = "@gmail.com"

    while True:

        matricula = input(" Capturar matrícula ")

        if matricula == '1030034':
            break

        timestamp = time.time()

        response = client.send_message(
            QueueUrl=queue_url,
            MessageBody=json.dumps({
                "matricula": matricula,
                "timestamp": timestamp,
                "subject": subject,
                "content": day_objective,
                "receiver": matricula+email_termination,
            })
        )

        if response["ResponseMetadata"]["HTTPStatusCode"] == 200:
            print(f"\tAlumno {matricula} capturado correctamente\t\n")

