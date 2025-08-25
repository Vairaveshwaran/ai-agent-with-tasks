🤖 AI Agent with Tasks

An intelligent AI Agent built using LangChain + OpenAI API + PostgreSQL + Docker, capable of:

Accepting user queries

Generating smart responses using GPT models

Saving query–response pairs in a PostgreSQL database

(Future extension) Optionally sending results as PDF/Word via email

✨ Features

🧠 AI-powered agent – Uses GPT via LangChain to answer queries.

🗄️ Database logging – Every query and response is stored in PostgreSQL.

🐳 Dockerized database – Easy setup with a single Docker command.

🔑 Environment variables – API keys and secrets are kept safe in .env.

📄 Future-ready – Can be extended to email results or add more tools.

⚙️ Project Flow

User enters a query

LangChain Agent (GPT model) generates an intelligent response

Response is shown to the user

Query + response is saved in PostgreSQL for history tracking

(Optional future) Send the output as PDF/Word via email

🛠️ Setup
1️⃣ Clone the repository
git clone https://github.com/yourusername/ai_agent_with_tasks.git
cd ai_agent_with_tasks

2️⃣ Create & activate virtual environment
python -m venv venv
venv\Scripts\activate   # On Windows
source venv/bin/activate  # On Mac/Linux

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Start PostgreSQL via Docker
docker run --name ai_agent_db -e POSTGRES_USER=agent_user -e POSTGRES_PASSWORD=agent_pass -e POSTGRES_DB=agent_db -p 5432:5432 -d postgres

5️⃣ Set up environment variables

Create a .env file:

OPENAI_API_KEY=your_api_key_here
DATABASE_URL=postgresql://agent_user:agent_pass@localhost:5432/agent_db


(Commit .env.example instead of real .env)

6️⃣ Run the agent
python agent.py

📂 Repository Structure
ai_agent_with_tasks/
│-- agent.py            # Main agent logic
│-- requirements.txt    # Python dependencies
│-- .env.example        # Example env file
│-- README.md           # Project documentation
│-- .gitignore          # Ignore venv, env, cache files

🔮 Future Improvements

Add AutoEmail feature (send results as PDF/Word to user’s email).

Integrate web search tools for real-time answers.

Build a simple web UI (Flask/Streamlit).
