# AI-Powered Personal Finance Assistant

A Streamlit-based web application that leverages a multi-agent AI architecture to analyze personal financial transactions. Upload a CSV file containing your transaction data to gain insights, including anomaly detection, monthly spending summaries, and personalized financial advice.

## Features

- **CSV Transaction Ingestion**: Upload and process transaction data from CSV files.
- **Anomaly Detection**: Identifies unusually high-value transactions for review.
- **Monthly Summaries**: Generates detailed breakdowns of monthly spending patterns.
- **Personalized Financial Advice**: Provides tailored recommendations based on spending trends and patterns.

## How It Works

The application uses a multi-agent system to process and analyze financial data:

1. **Ingestion Agent**: Parses and categorizes raw transaction data from uploaded CSV files.
2. **Anomaly Agent**: Flags transactions that are unusually large or suspicious.
3. **Summary Agent**: Aggregates data to produce monthly spending summaries.
4. **Advisor Agent**: Analyzes patterns and generates personalized financial advice.

## Screenshots

1.
![Screenshot 1](https://github.com/shourabhpandey/ai-finance-assistant/blob/main/Screenshot%202025-06-05%20at%2012.59.22.png)

2.
![Screenshot 2](https://github.com/shourabhpandey/ai-finance-assistant/blob/main/Screenshot%202025-06-05%20at%2012.59.44.png)


## Installation

To set up and run the project locally, follow these steps:

```bash
# Clone the repository
git clone https://github.com/yourusername/ai-finance-assistant.git

# Navigate to the project directory
cd ai-finance-assistant

# Install dependencies
pip install -r requirements.txt

# Run the Streamlit app
streamlit run app.py
```

## Folder Structure

```plaintext
ai-finance-assistant/
├── agents/                    # Agent-specific logic
│   ├── ingestion_agent.py     # Handles CSV parsing and categorization
│   ├── anomaly_agent.py       # Detects high-value or unusual transactions
│   ├── summary_agent.py       # Generates monthly spending summaries
│   └── advisor_agent.py       # Provides personalized financial advice
├── orchestrator/              # Workflow orchestration
│   └── langgraph_flow.py      # Manages agent interactions using LangChain
├── app.py                     # Main Streamlit application
├── requirements.txt           # Project dependencies
└── README.md                  # Project documentation
```

## Tech Stack

- **Python**: Core programming language.
- **LangChain**: Framework for orchestrating multi-agent workflows.
- **Pandas**: Data manipulation and analysis.
- **Streamlit**: Web interface for user interaction and visualization.

## Prerequisites

- Python 3.8 or higher
- A valid CSV file with transaction data (ensure it follows the expected format; see [Usage](#usage) for details)

## Usage

1. Run the application using `streamlit run app.py`.
2. Open the provided local URL (e.g., `http://localhost:8501`) in your browser.
3. Upload a CSV file containing transaction data with columns such as `date`, `amount`, `description`, and `category` (optional).
4. View insights, including detected anomalies, monthly summaries, and personalized advice, displayed in the Streamlit interface.

**Sample CSV Format**:
```csv
date,amount,description,category
2025-01-01,50.00,Grocery Store,Food
2025-01-02,2000.00,Car Repair,Transportation
```

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Make your changes and commit (`git commit -m "Add your feature"`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a pull request.

Please ensure your code follows the project's coding standards and includes relevant tests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Author

**Shourabh Pandey**

## Contact

For questions, suggestions, or issues, please open an issue on the [GitHub repository](https://github.com/yourusername/ai-finance-assistant) or contact the author directly.

## Acknowledgments

- Built with [Streamlit](https://streamlit.io/) for an intuitive web interface.
- Powered by [LangChain](https://www.langchain.com/) for agent orchestration.
- Uses [Pandas](https://pandas.pydata.org/) for efficient data processing.

---
Happy budgeting! 💸
