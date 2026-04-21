from langchain_groq import ChatGroq
from langchain.agents import create_react_agent, AgentExecutor
from langchain import hub

from langchain_tavily import TavilySearch
from dotenv import load_dotenv
import os

load_dotenv()  # removed duplicate

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY")
)

search = TavilySearch(max_results=3, tavily_api_key=os.getenv("TAVILY_API_KEY"))


prompt = hub.pull("hwchase17/react")
tools = [search]
agent = create_react_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

from market_data import get_market_data
import json

data = get_market_data()

result = agent_executor.invoke({
    "input": f"""You are an expert Nifty 50 options trading advisor.
Here is the current market data: {json.dumps(data)}

Search for the latest Nifty 50 news and any relevant market events.
Then suggest the best options strategy with rationale, risk and potential profit."""
})

print(result["output"])