import random

class ChatbotModel:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def generate_response(self, intent):
        """Generates a response based on intent."""
        if intent is None:
            return "I'm sorry, I didn't understand that."

        # gettng response from database
        cursor = self.db_connection.cursor()
        cursor.execute("SELECT response FROM knowledge_base WHERE intent = ?", (intent['tag'],))
        response = cursor.fetchone()
        self.db_connection.commit()
        if response:
            return response[0]
        else:
            return "I don't have a response for that yet."

    def log_interaction(self, user_input, intent, chatbot_response):
        """Logs the user interaction in the database."""
        cursor = self.db_connection.cursor()
        cursor.execute("INSERT INTO user_interactions (user_input, intent, chatbot_response) VALUES (?, ?, ?)",
                       (user_input, intent, chatbot_response))
        self.db_connection.commit()
