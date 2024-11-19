from flask import Flask
from flask import render_template, request

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/Ejercicio1.html', methods=['GET', 'POST'])
def ejercicio1():
    res = None
    if request.method == "POST":
        try:
            Nota1 = float(request.form.get('Nota1', 0))
            Nota2 = float(request.form.get('Nota2', 0))
            Nota3 = float(request.form.get('Nota3', 0))
            Asistencia = float(request.form.get('Asistencia', 0))

            if not (10 <= Nota1 <= 70 and 10 <= Nota2 <= 70 and 10 <= Nota3 <= 70 and 0 <= Asistencia <= 100):
                res = "Información inválida, Notas deben estar entre 10 y 70 y asistencia entre 0 y 100. "
            elif not (0 <= Asistencia <= 100):
                res = "La asistencia está entre el rango de 0 a 100"
            else:
                prom = (Nota1 + Nota2 + Nota3) / 3

                if prom >= 40 and Asistencia >= 75:
                    res = f"Promedio: {prom:.2f}. Estado: Aprobado."
                else:
                    res = f"Promedio: {prom:.2f}. Estado: Reprobado."
        except ValueError:
            res = "Error: Por favor, ingrese valores válidos."


    return render_template('Ejercicio1.html', res=res)

@app.route('/Ejercicio2.html', methods=["GET", "POST"])
def ejercicio2():
    res = None
    if request.method == "POST":
        try:
            nombre1 = request.form.get("nombre1", "").strip()
            nombre2 = request.form.get("nombre2", "").strip()
            nombre3 = request.form.get("nombre3", "").strip()

            if not nombre1 or not nombre2 or not nombre3:
                res = "Los nombres deben estar completos"

            elif len(set([nombre1, nombre2, nombre3])) < 3:
                res = "Nombre ya registrado, deben ser diferentes."

            else:
                nombres = [nombre1, nombre2, nombre3]
                nombre_largo = max(nombres, key=len)
                long = len(nombre_largo)

                res = f"El nombre más largo es '{nombre_largo}' con {long} caracteres."
        except Exception as e:
            res = f"Error: {e}"

    return render_template('Ejercicio2.html', res=res)

if __name__ == '__main__':
    app.run()
