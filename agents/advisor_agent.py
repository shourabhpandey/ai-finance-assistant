from langchain_community.llms import Ollama
from langchain.prompts import PromptTemplate

def run_advice(transactions):
    llm = Ollama(model="mistral")

    template = """
    You are a financial advisor. Analyze the following list of transactions and provide:
    1. Spending habits
    2. Saving suggestions
    3. Any risky or unusual patterns

    Transactions:
    {transactions}
    """

    prompt = PromptTemplate.from_template(template)
    formatted_prompt = prompt.format(transactions=transactions)

    response = llm.invoke(formatted_prompt)
    cleaned = response.replace("\n", "\n\n").replace("  ", " ").strip()
    return cleaned
