import streamlit as st
from market_data import get_market_data
from langchain_groq import ChatGroq
from langchain_tavily import TavilySearch
from dotenv import load_dotenv
import os
import json

# ------------------ SETUP ------------------
load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY")
)

search = TavilySearch(
    max_results=3,
    tavily_api_key=os.getenv("TAVILY_API_KEY")
)

st.set_page_config(page_title="AlphaTrade", page_icon="📈", layout="wide")

st.title("📈 AlphaTrade — AI Options Strategy Analyzer")
st.markdown("### Real-time Nifty 50 options strategy powered by AI")

# ------------------ HELPER FUNCTIONS ------------------

def safe_float(value, default=0.0):
    """Safely convert to float"""
    try:
        return float(value)
    except (ValueError, TypeError):
        return default

def format_currency(value):
    return f"₹{safe_float(value):,.2f}"

def format_percent(value):
    return f"{safe_float(value):.2f}%"

# ------------------ MAIN BUTTON ------------------

if st.button("🔍 Analyze Market Now", use_container_width=True):

    # -------- FETCH DATA --------
    with st.spinner("📡 Fetching live market data..."):
        data = get_market_data()

    # -------- VALIDATION --------
    if not data:
        st.error("❌ Failed to fetch market data.")
        st.stop()

    # -------- DISPLAY DATA --------
    st.subheader("📊 Live Market Data")

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Nifty 50",
        format_currency(data.get('current_price')),
        format_percent(data.get('percentage_change'))
    )

    col2.metric(
        "India VIX",
        f"{safe_float(data.get('vix_level')):.2f}"
    )

    col3.metric(
        "52W High",
        format_currency(data.get('fiftytwo_week_high'))
    )

    # -------- NEWS --------
    with st.spinner("📰 Fetching latest market news..."):
        try:
            news_result = search.invoke("Nifty 50 latest news India today")
            news_text = " ".join(
                [r["content"] for r in news_result.get("results", [])]
            )
        except Exception as e:
            news_text = "No news available."
            st.warning("⚠️ Failed to fetch news.")

    # -------- AI ANALYSIS --------
    with st.spinner("🤖 Generating AI trading strategy..."):

        prompt = f"""
You are a professional options trader specializing in Indian markets.

Market Data:
{json.dumps(data, indent=2)}

Latest News:
{news_text}

Analyze and suggest a high-probability options strategy.

Respond STRICTLY in this format:

Strategy:
Rationale:
Risk:
Potential Profit:
Strike Prices:
"""

        try:
            response = llm.invoke(prompt)
            output = response.content
        except Exception as e:
            output = "❌ Failed to generate strategy."

    # -------- OUTPUT --------
    st.subheader("🎯 Recommended Strategy")

    st.markdown(f"""