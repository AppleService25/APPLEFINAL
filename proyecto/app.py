from flask import Flask, request, jsonify
import gspread
from oauth2client.service_account import ServiceAccountCredentials

app = Flask(__name__)

# Configurar acceso a Google Sheets
scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive"
]
credentials = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
client = gspread.authorize(credentials)

# Abrir la hoja de cálculo
spreadsheet_name = "Registro de Usuarios"
worksheet_name = "Hoja1"
try:
    sheet = client.open(spreadsheet_name).worksheet(worksheet_name)
except gspread.SpreadsheetNotFound:
    sheet = client.create(spreadsheet_name).get_worksheet(0)
    sheet.update([["Correo", "Contraseña"]])

@app.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    correo = data.get("correo")
    contrasena = data.get("contrasena")

    if not correo or not contrasena:
        return jsonify({"error": "Correo y contraseña son obligatorios."}), 400

    # Guardar en la hoja de cálculo
    sheet.append_row([correo, contrasena])

    return jsonify({"message": "Usuario registrado exitosamente."}), 201

if __name__ == "__main__":
    app.run(debug=True)
