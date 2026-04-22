# AlphaTrade: AI-Powered Nifty 50 Options Strategy Analyzer

AlphaTrade is a Python project that combines live Indian market data, web news search, and LLM reasoning to generate Nifty 50 options strategy suggestions.

It includes multiple ways to use the system:
- A **Streamlit web app** for interactive analysis
- A **FastAPI endpoint** for API-style access
- **CLI scripts** for direct experimentation
- A basic **RAG demo** for question-answering over PDFs

## Features

- Fetches live market context from NSE (`NIFTY 50`, `INDIA VIX`, yearly high/low)
- Pulls recent market/news context using Tavily search
- Uses Groq-hosted LLMs (Llama 3.3 70B) for strategy generation
- Displays AI output in a clean Streamlit dashboard
- Exposes an `/analyze` API route via FastAPI
- Includes a PDF Q&A (RAG) workflow with Chroma + HuggingFace embeddings

## Project Structure

```text
.
├── streamlit_app.py        # Main UI app (recommended entrypoint)
├── market_data.py          # Live market data fetch from NSE
├── analyzer.py             # Direct Groq strategy analyzer
├── main.py                 # FastAPI app exposing /analyze
├── agent.py                # LangChain ReAct-style agent with Tavily tool
├── rag_agent.py            # RAG over PDF example
├── langchain_analyzer.py   # LangChain LLM setup (in progress)
└── requirements.txt        # Python dependencies
```

## Tech Stack

- **Python**
- **Streamlit**
- **FastAPI**
- **LangChain**
- **Groq API**
- **Tavily Search API**
- **NSE data endpoint + nsepython**
- **Chroma + HuggingFace embeddings** (RAG demo)

## Prerequisites

- Python 3.10+ (3.11 recommended)
- A Groq API key
- A Tavily API key

## Setup

1. Clone the repository:

```bash
git clone <your-repo-url>
cd ai-automation-week
```

2. Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the project root:

```bash
GROQ_API_KEY=your_groq_api_key
TAVILY_API_KEY=your_tavily_api_key
```

## Run the App

### Streamlit (recommended)

```bash
streamlit run streamlit_app.py
```

Then open the local URL shown in the terminal and click **Analyze Market Now**.

### FastAPI

```bash
uvicorn main:app --reload
```

API endpoint:
- `GET /analyze`

### CLI scripts

```bash
python analyzer.py
python agent.py
python rag_agent.py
```

> Note: `rag_agent.py` expects a local `resume.pdf` file by default. Change the file path in the script as needed.

## Example Workflow

1. Fetch latest Nifty 50 + VIX data
2. Retrieve current news context
3. Send market + news context to the LLM
4. Return a structured strategy recommendation:
   - Strategy
   - Rationale
   - Risk
   - Potential Profit
   - Strike Prices

## Environment Variables

| Variable | Required | Purpose |
| --- | --- | --- |
| `GROQ_API_KEY` | Yes | Access to Groq LLM endpoints |
| `TAVILY_API_KEY` | Yes (for news search) | Access to Tavily search tool |

## Important Disclaimer

This project is for educational and research use only.
It is **not financial advice**. Options trading involves substantial risk. Always do your own research and consult a qualified financial advisor.

## Roadmap Ideas

- Add strategy backtesting module
- Add historical indicators (SMA/EMA/RSI/MACD)
- Add Pydantic schemas for strongly structured LLM outputs
- Add retry/rate-limit handling for external APIs
- Add tests and CI workflows
- Add Docker support for one-command deployment

## Contributing

Contributions are welcome. If you want to improve data quality, prompts, risk controls, or UI/UX, feel free to open an issue or PR.

## License

Add your preferred license (for example, MIT) in a `LICENSE` file.

