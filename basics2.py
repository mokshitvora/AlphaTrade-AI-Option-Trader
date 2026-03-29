
from groq import Groq
from dotenv import load_dotenv
import os


def ask(system,model,message):
    load_dotenv()
    client = Groq(api_key=os.getenv("GROQ_API_KEY"))
    
    response = client.chat.completions.create(
    model=model,
    messages=[
        {"role": "system", "content": system},
        {"role": "user", "content": message}
    ])
    return response.choices[0].message.content


    
print(ask("You are a helpful assistant", "llama-3.3-70b-versatile", "what is yellow?"))








