from langchain_tavily import TavilySearch
from dotenv import load_dotenv
import os

load_dotenv()  # removed duplicate

search = TavilySearch(max_results=5)  # instantiate before calling .run()

result = search.run("Nifty 50 latest news today")
print(result)