# AI Chatbot for Customer Service

This project implements an AI-powered chatbot designed to enhance customer service interactions. It leverages natural language processing (NLP) techniques to understand user queries and provide relevant responses.

## Technologies Used

### Backend

*   **Flask:** Python web framework for building the API.
*   **SQLite:** Lightweight database for storing chatbot knowledge and interactions.
*   **Gensim:** Library for loading pre-trained word embeddings (Word2Vec).
*   **NLTK:** Natural Language Toolkit for text preprocessing and NLP tasks.
*   **Scikit-learn:** Machine learning library (optional, for future enhancements).

### Frontend

*   **Next.js 14:** React framework for building the user interface.
*   **Tailwind CSS:** Utility-first CSS framework for styling.
*   **TypeScript:** Typed superset of JavaScript for improved code maintainability.

## Setup and Installation

### Backend

**For the backend i included the .venv folder, so you can just run the app.py file and it will work.**

### Frontend

1.  **Navigate to the `frontend` directory:**
    ```bash
    cd frontend
    ```

2.  **Install dependencies:**
    ```bash
    npm install
    ```

## Running the Application

1.  **Start the Flask backend:** (in the `backend` directory)
    ```bash
    flask run
    ```

2.  **Start the Next.js frontend:** (in the `frontend` directory)
    ```bash
    npm run dev
    ```

3.  **Open your browser and visit http://localhost:3000** (or the appropriate port).

## Additional Notes

*   The chatbot's knowledge base is currently stored in the `chatbot.db` file.
*   The chatbot uses word embeddings (Word2Vec) for intent recognition.