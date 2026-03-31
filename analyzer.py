
from market_data import get_market_data 
from groq import Groq
from dotenv import load_dotenv
import json
import os
load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def analyze(data):
    
    messages = [
{ "role" : "system" , "content" :"you are a trading advisor , master in options who will suggest great option startegies which gaurantee pprofit based on user data"},
{"role":"user","content": json.dumps(data)}
]
    
    response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=messages
)
    return response.choices[0].message.content


data = get_market_data()
print(analyze(data))


