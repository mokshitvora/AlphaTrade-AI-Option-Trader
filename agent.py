from langchain_tavily import TavilySearch
from dotenv import load_dotenv
import os
load_dotenv()
load_dotenv()

result = search.run("Nifty 50 latest news today")
print(result)