import os
import shutil
import openpyxl
import json


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

    try: 
        wb = openpyxl.Workbook()
        wb.create_sheet('Tarea 1')
        wb.create_sheet('Tarea 2')
        
        try:
            Sheet1 = wb['Sheet']
            wb.remove(Sheet1)
        except Exception as err:
            print('Not Sheet in document', err)

        sheet_1 = wb['Tarea 1']             
        sheet_2 = wb['Tarea 2']             

        sheet_1.cell(row = 1, column = 1).value = 'Matricula'
        sheet_1.cell(row = 1, column = 2).value = 'Nombre'
        sheet_1.cell(row = 1, column = 3).value = 'Algoritmo Cotidiano'

        sheet_2.cell(row = 1, column = 1).value = 'Matricula'
        sheet_2.cell(row = 1, column = 2).value = 'Nombre'
        sheet_2.cell(row = 1, column = 3).value = 'Algoritmo Industrial'

    except Exception as err:
        print(err)


    for group in groups:

        files_in_dir = os.listdir(path_homeworks + f"\\Grupo-IM-20-{group}\\Tareas")
        idex_hw1_ = 2
        idex_hw2_ = 2
        exit_flag = 0

        group_file = f"groups/IM_20-{group}.json"
        
        with open(file=group_file, mode="r", encoding="utf-8") as file:
            parameters_group = json.load(file)

        students = parameters_group['students_id']

        for file in files_in_dir:

            params = file.strip().split('-')
            # print(params[2], exit_flag)
            current_student = params[2]

            if ('algoritmo1' or 'cotidiano' or 'cotidian' or 'coti') in file.lower():
                sheet_1.cell(row = idex_hw1_, column = 1).value = current_student
                sheet_1.cell(row = idex_hw1_, column = 2).value = params[1]
                sheet_1.cell(row = idex_hw1_, column = 3).value = 'Entregado'
                idex_hw1_+=1
                exit_flag+=1

                if int(current_student) not in students:        
                    print(f"student {params[1]} - {current_student} not in {group}", exit_flag)

            elif ('algoritmo2' or 'industrial' or 'indus' or 'industr') in file.lower():
                sheet_2.cell(row = idex_hw2_, column = 1).value = current_student
                sheet_2.cell(row = idex_hw2_, column = 2).value = params[1]
                sheet_2.cell(row = idex_hw2_, column = 3).value = 'Entregado'
                idex_hw2_+=1                
                exit_flag+=1

                if int(current_student) not in students:        
                    print(f"student {params[1]} - {current_student} not in {group}", exit_flag)

            if exit_flag == 2:
                try:            
                    students.remove(int(current_student))
                    exit_flag = 0
                except Exception as err:
                    print("Error", err)


        print('No entregaron', students)

        wb.save(path_homeworks + f"\\Grupo-IM-20-{group}\\Tareas\\Tarea.xlsx")





"""

https://j2logo.com/python/crear-archivo-excel-en-python-con-openpyxl/

https://www.datacamp.com/es/tutorial/python-excel-tutorial

Salida 1 - Documento de Excel 

Nombre - Matricula - Tarea 1 - Tarea 2 - Porcentaje de Tareas cumplidas - Puntuación Tareas


Salida 2 - Documento de Excel 

Nombre - Matricula - Proyecto 1 - Proyecto 2 - Porcentaje de Proyecto - Puntuación Proyecto


"""