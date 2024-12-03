from flask import Flask, jsonify, request

app = Flask(__name__)

# Simulación de archivo JSON (puedes cargarlo desde un archivo si lo prefieres)
questions = {
    "questions": [
        {
            "id": 1,
            "category": "Autoconocimiento",
            "text": "Solicito información a los demás acerca de mis fortalezas y debilidades como base para mi mejora personal.",
            "scale": [1, 2, 3, 4, 5, 6]
        },
        {
            "id": 2,
            "category": "Autoconocimiento",
            "text": "Para mejorar, estoy dispuesto a revelar aspectos personales a los demás (esto es, compartir mis creencias y sentimientos).",
            "scale": [1, 2, 3, 4, 5, 6]
        }
        # Agregar más preguntas aquí
    ]
}

# Ruta para obtener las preguntas
@app.route('/questions', methods=['GET'])
def get_questions():
    return jsonify(questions)

# Ruta para recibir las respuestas
@app.route('/answers', methods=['POST'])
def save_answers():
    answers = request.json  # Las respuestas enviadas por el cliente
    print("Respuestas recibidas:", answers)
    # Aquí puedes guardarlas en una base de datos o archivo
    return jsonify({"message": "Respuestas recibidas correctamente"}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)
