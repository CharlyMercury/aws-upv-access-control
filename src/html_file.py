import datetime


def crear_html(matricula, timestamp, subject, receiver, content):

    today_day = datetime.datetime.fromtimestamp(float(timestamp)).strftime('%Y-%m-%d %H:%M:%S')

    trigger_basein_subject = subject.lower()
    
    if "asistencia" in trigger_basein_subject:
        body_title = " Bienvenido a la clase: Metodología de la programación. "
        first_greeting = f" Gracias por asistir a tu clase del día de hoy: {today_day} "
        background_color_title = "#138808"
        background_letters_color_title = "#000000"
    elif "tarea" in trigger_basein_subject:
        body_title = " Tarea Semanal: Metodología de la programación. "
        first_greeting = f" Me da gusto saludarte el día de hoy: {today_day}. A continuación te muestro las especificaciones para las tareas de la semana. "
        background_color_title = "#0073e6"
        background_letters_color_title = "#ffffff"
    elif "aviso" in trigger_basein_subject:
        body_title = " Aviso importante: Metodología de la programación. "
        first_greeting = f" Me da gusto saludarte el día de hoy: {today_day}."
        background_color_title = "#E4D00A"
        background_letters_color_title = "#ffffff"

    html_content = f"""<!DOCTYPE html>
    <html lang="es">
    <head>
      <meta charset="UTF-8">
      <meta http-equiv="X-UA-Compatible">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title> {subject} </title>  
      </head>
      <body
        style="
          margin: 0;
          padding: 0;
          background-color: #f4f4f4;
          font-family: Arial, sans-serif;
          color: #333333;
        "
      >
        <table
          border="0"
          cellpadding="0"
          cellspacing="0"
          width="100%"
          style="max-width: 600px; margin: 0 auto; background-color: #ffffff"
        >
          <tr>
            <td align="center" bgcolor={background_color_title} style="padding: 20px; color: {background_letters_color_title}; font-size: 24px" >
             {body_title}
            </td>
          </tr>
          <tr>
            <td
              style="
                padding: 20px;
                line-height: 1.5;
                color: #333333;
              "
            >
              <h3> Estimado/a: {matricula}, </h3>
              <h4> {first_greeting} </h4>
              {content}

              <h5 style="margin: 0px; padding: 0px; color: #333333;"> Saludos cordiales. </h5>
              <h5 style="margin: 0px; padding: 0px; color: #333333;"><strong> MC. Carlos Antonio Tovar García </strong></h5>
              <h5 style="margin: 0px; padding: 0px; color: #333333;">Profesor de Metodología de la Programación</h5>
              <h5 style="margin: 0px; padding: 0px; color: #333333;">Ingeniería Mecatrónica</h5>
              <h5 style="margin: 0px; padding: 0px; color: #333333;">Universidad Politécnica de Victoria</h5>
              <h5 style="margin: 0px; padding: 0px; color: #333333;">Email: <a href="mailto:ctovarg@upv.edu.mx">ctovarg@upv.edu.mx</a></h4>

              <h6>
                Si no perteneces a la clase: Metodología de la Programación 
                de la Universidad Politécnica de Victoria, ignora este correo electrónico.
              </h6>

            </td>
          </tr>
          <tr>
            <td
              align="center"
              bgcolor="#f4f4f4"
              style="
                padding: 20px;
                font-size: 12px;
                color: #666666;
                text-align: center;
              "
            >
            <p> &copy; 2024. Todos los derechos reservados.</p>
            <p> Carlos Antonio Tovar García </p>
            </td>
          </tr>
        </table>
      </body>
    </html>
   """
    # Guardar el contenido HTML en un archivo
    with open("html_body.html", "w", encoding="utf-8") as file:
        file.write(html_content)

    print("Archivo HTML creado con éxito.")
