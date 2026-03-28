from groq import Groq
from dotenv import load_dotenv
import os
import json

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

MY_BACKGROUND = """
Name: Mokshit
Degree: B.Tech Electronics & Instrumentation Engineering, Minor in CSE
CGPA: 8.0
Skills: Python, ML, Deep Learning, Federated Learning research
Projects: Working on academic ML papers
Looking for: AI Engineer internship
Location: Ahmedabad
"""

def research_company(company_name):
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": """You are a company research assistant.
Respond with valid JSON only. No markdown, no backticks, no extra text.
Format:
{
  "company_name": "",
  "what_they_do": "",
  "tech_stack": [],
  "ai_use_cases": []
}"""
            },
            {"role": "user", "content": f"Research this company: {company_name}"}
        ]
    )
    return json.loads(response.choices[0].message.content)


def generate_email(company_data):
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": f"""You are an expert at writing cold internship emails.
Rules:
- Max 3 short paragraphs
- Sound human, not robotic
- Reference something specific about the company
- End with a clear call to action
- Never use generic lines like "I am writing to express my interest"

Candidate background:
{MY_BACKGROUND}"""
            },
            {
                "role": "user",
                "content": f"""Write a cold email for an AI Engineer internship at {company_data['company_name']}.
What they do: {company_data['what_they_do']}
Tech stack: {', '.join(company_data['tech_stack'])}
AI use cases: {', '.join(company_data['ai_use_cases'])}"""
            }
        ]
    )
    return response.choices[0].message.content


def run_pipeline(company_name):
    print(f"\n🔍 Researching {company_name}...")
    company = research_company(company_name)
    
    print(f"✅ Found: {company['what_they_do'][:60]}...")
    
    print(f"✍️  Drafting email...")
    email = generate_email(company)
    
    print(f"\n{'='*50}")
    print(f"📧 EMAIL FOR {company_name.upper()}")
    print(f"{'='*50}")
    print(email)
    print(f"{'='*50}\n")
    
    return {"company": company, "email": email}


# Run it on 3 companies
companies = ["Juspay", "Zepto", "Darwinbox"]

for company in companies:
    run_pipeline(company)