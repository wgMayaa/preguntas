from flask import Flask, request
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)

@app.route("/")
def inicio():
    return '''
    <h2>Contéstame esto 💛</h2>
    <form method="POST" action="/enviar">
        Nombre: <input name="nombre"><br><br>
        Comida favorita: <input name="comida"><br><br>
        <button type="submit">Enviar</button>
    </form>
    '''

@app.route("/enviar", methods=["POST"])
def enviar():
    nombre = request.form["nombre"]
    comida = request.form["comida"]

    mensaje = f"{nombre} dijo que su comida favorita es {comida}"

    # Aquí pones tu correo
    remitente = "tucorreo@gmail.com"
    contraseña = "TU_CONTRASEÑA_DE_APLICACION"
    destinatario = "tucorreo@gmail.com"

    msg = MIMEText(mensaje)
    msg["Subject"] = "Nueva respuesta"
    msg["From"] = remitente
    msg["To"] = destinatario

    servidor = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    servidor.login(remitente, contraseña)
    servidor.send_message(msg)
    servidor.quit()

    return "Gracias por responder 💛"

if __name__ == "__main__":
    app.run()
