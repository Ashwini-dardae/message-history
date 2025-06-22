
💬 Memory-Based Chatbot using LangChain + Groq
This project implements a smart chatbot that remembers your past messages (like ChatGPT) using LangChain's message history, powered by Groq's Llama3 LLM. It mimics human-like multi-turn conversations with memory — tracking names, context, and previous answers.

✅ Key Features
🧠 Message Memory: Remembers what you told it earlier (your name, role, etc.)

💬 Multi-turn chat: Have continuous, intelligent conversations

🤖 Uses LangChain with Groq’s blazing-fast LLMs

⚙️ Custom prompt templates and memory trimming logic


🎯 Use Case
You: Hi, my name is Krish.
Bot: Nice to meet you, Krish! What do you do?

You: I’m a Chief AI Engineer.
Bot: That’s impressive! What kind of AI projects are you working on?

You: What’s my name?
Bot: Your name is Krish.

📁 Folder Structure
.
├── app.py                         # Streamlit frontend to chat
├── langchain_chat.py              # LangChain logic, memory, prompts
├── requirements.txt
├── .env                           # API key
└── README.md

🔮 Future Enhancements
Persistent memory using Redis or FAISS

User authentication for multiple chat sessions

Export chat as PDF or email
