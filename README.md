# AI-ChatBot
This project is an AI-powered chatbot built using Streamlit for the user interface and the Mistral API for generating intelligent responses. The chatbot allows users to have interactive conversations, save chat history, and load previous conversations.

# AI Chatbot with Streamlit and Mistral API
This project is an AI-powered chatbot built using Streamlit for the user interface and the Mistral API for generating intelligent responses. The chatbot allows users to have interactive conversations, save chat history, and load previous conversations. It is designed to be user-friendly and can be used for various applications, such as answering FAQs, providing career guidance, or general-purpose conversational AI.

# Features
Interactive Chat Interface: Users can type questions and receive responses in real-time.

Prebuilt Questions: Quick access to common questions for faster interactions.

Conversation History: Save and load previous conversations for seamless continuity.

Database Integration: Chat history is stored in a MySQL database for persistence.

Mistral API Integration: Leverages the Mistral API for generating intelligent and context-aware responses.

Responsive UI: Built with Streamlit, providing a clean and intuitive user interface.

# Technologies Used
Streamlit: For building the web-based user interface.

Mistral API: For generating AI-powered responses.

MySQL: For storing and retrieving chat history.

Python: Backend logic and integration.

JSON: For serializing and deserializing chat history.

# How It Works
Users interact with the chatbot through the Streamlit UI.

User queries are sent to the Mistral API, which generates responses.

Conversations are saved to a MySQL database for future reference.

Users can load previous conversations and continue chatting.

# Installation
Clone the repository:
bash
git clone https://github.com/your-username/your-repo-name.git

Install dependencies:
pip install -r requirements.txt

Set up the MySQL database and update the DB_CONFIG in config.py.

Run the Streamlit app:
streamlit run chat_ui.py


# Usage
Open the app in your browser.

Type your question or select a prebuilt question.

View the chatbot's response and continue the conversation.

Save and load conversations using the sidebar.

Future Enhancements
Add support for multiple users with authentication.

Integrate additional AI models for diverse use cases.

Improve the UI with themes and customization options.

Add analytics to track user interactions.

Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.
