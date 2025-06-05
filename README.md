# AI-Powered Personal Finance Assistant

An intelligent Streamlit web app that analyzes personal financial transactions using multi-agent AI architecture. Upload your CSV, and receive insights including anomaly detection, monthly summaries, and personalized financial advice.

## Features

- CSV-based transaction ingestion
- High-value anomaly detection
- Monthly spending summaries
- AI-generated personalized advice

## How It Works

1. **Ingestion Agent**: Parses and categorizes raw transaction data.
2. **Anomaly Agent**: Flags unusually large transactions.
3. **Summary Agent**: Computes monthly spending summaries.
4. **Advisor Agent**: Generates advice based on patterns.

## Installation

```bash
git clone https://github.com/yourusername/ai-finance-assistant.git
cd ai-finance-assistant
pip install -r requirements.txt
streamlit run app.py```


## Folder Structure
ai-finance-assistant/
│
├── agents/
│   ├── ingestion_agent.py
│   ├── anomaly_agent.py
│   ├── summary_agent.py
│   └── advisor_agent.py
│
├── orchestrator/
│   └── langgraph_flow.py
│
├── app.py
├── requirements.txt
└── README.md

##Tech Stack
1.Python
2.Langchain
3.Pandas
4.Streamlit

Author
Shourabh Pandey

