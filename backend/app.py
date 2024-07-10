import sqlite3
from flask import Flask, g, request, jsonify
from nlp import preprocess_text, predict_intent
from models.chatbot_model import ChatbotModel
from flask_login import LoginManager
from flask_cors import CORS

app = Flask(__name__)
app.config.from_object('config.Config')
CORS(app)

login_manager = LoginManager()
login_manager.init_app(app)

# Function to get a database connection
def get_db_connection():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(app.config['DATABASE'])
    return db

@app.route('/api/chat', methods=['GET'])
def get_bot_response():
    user_input = request.args.get('msg')
    if user_input is None:
        return jsonify({"error": "Missing 'msg' parameter"}), 400

    processed_input = preprocess_text(user_input)
    intent = predict_intent(processed_input)

    if intent is None:
        return jsonify({"response": "I'm sorry, I didn't understand that. Could you please rephrase?"})

    chatbot_model = ChatbotModel(get_db_connection())
    response = chatbot_model.generate_response(intent)
    chatbot_model.log_interaction(user_input, intent['tag'], response)

    return jsonify({'response': response})

# Function to close the database connection
@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

if __name__ == '__main__':
    app.run(debug=True)