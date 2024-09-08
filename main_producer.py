import json
import sys
from src.producer import producer_student_attendance, producer_student_homework, producer_student_email_notifications

with open(file=r"parameters_sqs.json", mode="r", encoding="utf-8") as file:
    parameters = json.load(file)

with open(file=r"classes/week_2/class_day_1.json", mode="r", encoding="utf-8") as file:
    parameters_class = json.load(file)

with open(file=r"homeworks/week_2/homework_1.json", mode="r", encoding="utf-8") as file:
    parameters_homework = json.load(file)

with open(file=r"notifications/week_2/notification_1.json", mode="r", encoding="utf-8") as file:
    parameters_notifications = json.load(file)

def run(args):
    if args=="asistencia": 
        print("\t\t---Control de Acceso---\n\t---Metodología de la programación---\n")
        producer_student_attendance(parameters, parameters_class)
    elif args == "tarea":
        print("\t\t---Tarea Semanal---\n\t---Metodología de la programación---\n")
        producer_student_homework(parameters, parameters_homework)
    elif args == "avisos":
        print("\t\t---Envío de avisos---\n\t---Metodología de la programación---\n")
        producer_student_email_notifications(parameters, parameters_notifications)
    else:
        print("Opción inválida")


if __name__ == "__main__":
    args = sys.argv[1]
    run(args)
    