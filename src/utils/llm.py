from google import genai
from src.components.summary import build_context

trade_context = build_context()

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=f"Summarise the following trade for me. Highlight the main upside and downside. What are the key concerns? Does this trade have a name? {trade_context}",
)

print(response.text)