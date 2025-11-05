# 🤖 AI Agent Lab — LangChain & LangGraph Playground

An interactive **Streamlit web app** that lets you explore and compare two cutting-edge AI agent frameworks — **LangChain** and **LangGraph** — side by side.  
It integrates **Tavily Search API** for real-time web information retrieval and showcases agent reasoning, tool use, and orchestration.

---

## 🚀 Features

✅ **Dual Agents UI** — Chat side-by-side with:
- **LangChain Agent** (uses Tavily Search for live research)
- **LangGraph Agent** (demonstrates graph-based tool orchestration)

✅ **Tavily Real Web Search** — fetch current results from the internet  
✅ **Math Reasoning Tools** — LangGraph agent supports addition/multiplication  
✅ **Session Chat Memory** — keeps chat history within the session  
✅ **Modern UI** — built with Streamlit, responsive and elegant  
✅ **Ready for Cloud Deployment** — easily deploy to Streamlit Cloud or Hugging Face Spaces

---

## 🧩 Tech Stack

| Component | Description |
|------------|--------------|
| **Python 3.10+** | Core language |
| **Streamlit** | Frontend web framework |
| **LangChain** | LLM framework for building tool-using agents |
| **LangGraph** | Graph-based orchestration for multi-step/stateful agents |
| **Tavily Search API** | Real-time search integration |
| **OpenAI / Claude / Local LLMs** | Backend language models (configurable) |

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/<your-username>/ai-agent-lab.git
cd ai-agent-lab
Create a virtual environment and install dependencies:

bash
Copy code
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate
pip install --upgrade pip
pip install -r requirements.txt
If you don’t have a requirements.txt, use:

bash
Copy code
pip install streamlit langchain langchain-openai langgraph langchain-tavily
🔑 Environment Variables
Before running, set your API keys:

bash
Copy code
export OPENAI_API_KEY="sk-your-openai-key"
export TAVILY_API_KEY="tvly-your-tavily-key"
Get a free Tavily key here: https://app.tavily.com

🧠 Usage
Run the app:

bash
Copy code
streamlit run app.py
Then open in your browser:
👉 http://localhost:8501

🖥️ User Interface
Section	Description
🧠 LangChain Agent	Uses Tavily Search to answer current-world questions. Great for research, fact-checking, and summarization.
📘 LangGraph Agent	Graph-based math agent performing reasoning and tool calls (e.g., add/multiply).
💬 Session History	Displays previous interactions in neatly formatted response boxes.

⚙️ Configuration
Change the model in the sidebar (default: openai:gpt-4o-mini)

Adjust temperature for creativity control

API keys can be managed as environment variables or .env file (optional)

🧰 Project Structure
bash
Copy code
ai-agent-lab/
├── app.py                # Streamlit frontend + backend logic
├── README.md             # Project documentation
├── requirements.txt      # Python dependencies
└── assets/ (optional)    # Images, logos, etc.
☁️ Deployment
Streamlit Cloud
Push this repo to GitHub

Go to https://streamlit.io/cloud

Deploy your repo

Under “Advanced Settings” → add environment variables:

OPENAI_API_KEY

TAVILY_API_KEY

Hugging Face Spaces
Create a new Streamlit Space

Upload app.py and requirements.txt

Add the same API keys as secrets under Settings

🧩 Future Enhancements
🔹 Add streaming responses (real-time token output)
🔹 Include long-term memory via LangChain Memory modules
🔹 Add code interpreter & geospatial reasoning tools
🔹 Enable local LLMs (Ollama, LM Studio, etc.)

👨‍💻 Author
Brian Otieno
Geospatial Engineer | Full-Stack Developer | AI & Data Enthusiast
🌍 Passionate about integrating geospatial intelligence with modern AI systems.
🔗 Connect: LinkedIn | GitHub

🪪 License
This project is released under the MIT License.
Feel free to modify, enhance, and distribute with attribution.

📚 References
LangChain Docs

LangGraph Docs

Tavily API

Streamlit