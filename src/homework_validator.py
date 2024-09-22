import os
import shutil
import openpyxl
import json
from src.homework import Homework


groups = ["75004", "75011", "75018"]


def move_file_to():

    downloads_path = "c:\\Users\\carlo\\Downloads"
    path_to_move = "c:\\Users\\carlo\\OneDrive\\upv_clases\\Metodologia_de_la_programacion"
    files_in_dir = os.listdir(downloads_path)


    for file_in_dir in files_in_dir:

        if groups[0] in file_in_dir:
            shutil.move(downloads_path+"\\"+file_in_dir, path_to_move+f"\\Grupo-IM-20-{groups[0]}\\Tareas")

        if groups[1] in file_in_dir:
            shutil.move(downloads_path+"\\"+file_in_dir, path_to_move+f"\\Grupo-IM-20-{groups[1]}\\Tareas")

        if groups[2] in file_in_dir:
            shutil.move(downloads_path+"\\"+file_in_dir, path_to_move+f"\\Grupo-IM-20-{groups[2]}\\Tareas")
        

def create_excel():

    path_homeworks = "c:\\Users\\carlo\\OneDrive\\upv_clases\\Metodologia_de_la_programacion"
    tareas = {"Tarea1": 'Algoritmo Cotidiano', "Tarea2": 'Algoritmo Industrial', "Tarea3": 'Algoritmos de clase'}

    for group in groups:

        group_file = f"groups/IM_20-{group}.json"
        
        with open(file=group_file, mode="r", encoding="utf-8") as file:
            parameters_group = json.load(file)

        students = parameters_group['students_id']
        tareas_grupo = Homework(students, tareas)
        files_in_dir = os.listdir(path_homeworks + f"\\Grupo-IM-20-{group}\\Tareas")

        idex_hw1_ = 2
        idex_hw2_ = 2
        idex_hw3_ = 2

        for file in files_in_dir:

            params = file.strip().split('-')

            if 'tarea' in params[0].lower():
                continue

            current_student = params[2]
            name = params[1]

            if ('algoritmo1' or 'cotidiano' or 'cotidian' or 'coti') in file.lower():
                tareas_grupo.set_value("Tarea1", idex_hw1_, current_student, name, 'Entregado')
                tareas_grupo.set_student("Tarea1", current_student)
                idex_hw1_+=1

            if ('algoritmo2' or 'industrial' or 'indus' or 'industr') in file.lower():
                tareas_grupo.set_value('Tarea2', idex_hw2_, current_student, name, 'Entregado')
                tareas_grupo.set_student('Tarea2', current_student)
                idex_hw2_+=1                

            if 'algoritmos3' in file.lower():
                tareas_grupo.set_value('Tarea3', idex_hw3_, current_student, name, 'Entregado')
                tareas_grupo.set_student('Tarea3', current_student)
                idex_hw3_+=1

        all_students = set({str(x) for x in students})

        for key, _ in tareas_grupo.students_by_tarea.items():
            students_homework = set(tareas_grupo.students_by_tarea[key])
            students_with_no_homework = list(all_students.difference(students_homework))
            tareas_grupo.students_by_tarea[key] = students_with_no_homework
            print(f" Grupo: {group}, Tarea: {key},  Entregaron: {len(students_homework)}, No entregaron: {len(students_with_no_homework)}" )
            # student_with_homework_sorted = [int(x) for x in list(students_homework)]
            # print(sorted(student_with_homework_sorted), students_with_no_homework)
            print(students_with_no_homework)
        
        # print(tareas_grupo.students_by_tarea)

        tareas_grupo.save_excel("c:\\Users\\carlo\\OneDrive\\upv_clases\\Metodologia_de_la_programacion"+f"\\Grupo-IM-20-{group}\\Tareas\\Tarea.xlsx")





"""

https://j2logo.com/python/crear-archivo-excel-en-python-con-openpyxl/

https://www.datacamp.com/es/tutorial/python-excel-tutorial

Salida 1 - Documento de Excel 

Nombre - Matricula - Tarea 1 - Tarea 2 - Porcentaje de Tareas cumplidas - Puntuación Tareas


Salida 2 - Documento de Excel 

Nombre - Matricula - Proyecto 1 - Proyecto 2 - Porcentaje de Proyecto - Puntuación Proyecto


"""