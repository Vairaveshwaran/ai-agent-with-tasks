import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_community.tools import DuckDuckGoSearchRun
from langchain.agents import initialize_agent, AgentType

# ✅ Load API key from .env
load_dotenv()


# ✅ Make sure your new API key is set in environment variables
# Option 1 (secure): setx OPENAI_API_KEY "your_new_api_key_here"
# Option 2 (temporary): uncomment line below
# os.environ["OPENAI_API_KEY"] = "your_new_api_key_here"

def run_agent(query: str):
    # 1. Load the OpenAI LLM (ChatGPT model)
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

    # 2. Add tools (DuckDuckGo for web search, you can add math/calculator if needed)
    tools = [DuckDuckGoSearchRun()]

    # 3. Create an Agent with tools
    agent = initialize_agent(
        tools,
        llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True
    )

    # 4. Run the agent
    response = agent.invoke({"input": query})
    return response["output"]

if __name__ == "__main__":
    while True:
        query = input("Enter your query (or 'exit'): ")
        if query.lower() == "exit":
            break
        try:
            answer = run_agent(query)
            print(f"\n🤖 Answer: {answer}\n")
        except Exception as e:
            print(f"⚠️ Error: {e}")
