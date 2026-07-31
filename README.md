# 🤖 LangGraph ChatBot

An AI-powered chatbot built using **LangGraph**, **LangChain**, **Streamlit**, and **Google Gemini/OpenAI**. The chatbot provides an interactive conversational interface with a modular backend powered by LangGraph workflows.

## 🚀 Features

- 💬 Interactive chat interface with Streamlit
- 🧠 LangGraph-based agent workflow
- 🔗 LangChain integration
- 🤖 Supports LLMs (Google Gemini/OpenAI)
- ⚡ Fast and responsive UI
- 🔒 Environment variable support using `.env`
- 📦 Modular project structure

## 🛠️ Tech Stack

- Python 3.14+
- LangGraph
- LangChain
- Streamlit
- Google Gemini / OpenAI
- python-dotenv

## 📂 Project Structure

```
ChatBot/
│── Backend.py
│── Frontend.py
│── requirements.txt
│── .env
│── README.md
```

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/Rolexx001/ChatBot.git
cd ChatBot
```

### 2. Create a virtual environment

```bash
python3 -m venv myenv
source myenv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Create a `.env` file

```env
GOOGLE_API_KEY=your_api_key_here
```

or

```env
OPENAI_API_KEY=your_api_key_here
```

## ▶️ Run the Application

Start the backend (if applicable):

```bash
python Backend.py
```

Run the Streamlit frontend:

```bash
streamlit run Frontend.py
```

## 📸 Demo

_Add screenshots or GIFs here._

## 🔮 Future Improvements

- Conversation Memory
- RAG (Retrieval-Augmented Generation)
- Multiple LLM Support
- Chat History
- Authentication
- Docker Deployment

## 🤝 Contributing

Contributions are welcome! Feel free to fork this repository and submit a pull request.

## 📜 License

This project is licensed under the MIT License.

---

⭐ If you found this project useful, don't forget to star the repository!
