import time
import boto3
import json

upv_termination = "@upv.edu.mx"
gmail_termination = "@gmail.com"
course = " Metodología de la programación "


def producer_student_attendance(parameters, parameters_class):

    client = boto3.client("sqs",
                        region_name=parameters["aws_region"],
                        aws_access_key_id=parameters["aws_key_id"],
                        aws_secret_access_key=parameters["aws_secret_key"])
    queue_url = parameters["queue_url"]

    subject = f"{parameters_class["subject"]}: {course}. "
    day_objective = parameters_class["content"]

    while True:

        matricula = input(" Capturar matrícula: ")

        if matricula == "test":
            matricula = "carlos.mercury92"
            email_termination = gmail_termination
        else:
            email_termination = upv_termination

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


def producer_student_homework(parameters, parameters_homework):

    client = boto3.client("sqs",
                        region_name=parameters["aws_region"],
                        aws_access_key_id=parameters["aws_key_id"],
                        aws_secret_access_key=parameters["aws_secret_key"])
    queue_url = parameters["queue_url"]

    subject = f" {parameters_homework["subject"]}: {course}. "
    week_homework = parameters_homework["content"]

    group_id = input(" Capturar id grupo (00, 04, 11, 18): ")
    group = f"groups/IM_20-750{group_id}.json"

    if group_id == "00":
        email_termination = gmail_termination
    else:
        email_termination = upv_termination 

    with open(file=group, mode="r", encoding="utf-8") as file:
        parameters_group = json.load(file)

    for student in parameters_group["students_id"]:
        matricula = str(student)
        timestamp = time.time()

        response = client.send_message(
            QueueUrl=queue_url,
            MessageBody=json.dumps({
                "matricula": matricula,
                "timestamp": timestamp,
                "subject": subject,
                "content": week_homework,
                "receiver": matricula+email_termination,
            })
        )

        if response["ResponseMetadata"]["HTTPStatusCode"] == 200:
            print(f"\tAlumno {matricula}: Tarea enviada correctamente. \t\n")


def producer_student_email_notifications(parameters, parameters_homework):
    
    client = boto3.client("sqs",
                        region_name=parameters["aws_region"],
                        aws_access_key_id=parameters["aws_key_id"],
                        aws_secret_access_key=parameters["aws_secret_key"])
    queue_url = parameters["queue_url"]

    subject = f" {parameters_homework["subject"]}: {course}. "
    week_homework = parameters_homework["content"]

    group_id = input(" Capturar id grupo (00, 04, 11, 18): ")
    group = f"groups/IM_20-750{group_id}.json"    

    if group_id == "00":
        email_termination = gmail_termination
    else:
        email_termination = upv_termination  

    with open(file=group, mode="r", encoding="utf-8") as file:
        parameters_group = json.load(file)

    for student in parameters_group["students_id"]:
        matricula = str(student)
        timestamp = time.time()

        response = client.send_message(
            QueueUrl=queue_url,
            MessageBody=json.dumps({
                "matricula": matricula,
                "timestamp": timestamp,
                "subject": subject,
                "content": week_homework,
                "receiver": matricula+email_termination,
            })
        )

        if response["ResponseMetadata"]["HTTPStatusCode"] == 200:
            print(f"\t Aviso enviado correctamente a {matricula}. \t\n")