import os
from dotenv import load_dotenv
import google.genai as genai
import requests
import json

load_dotenv()  # used to get API key

def call_gemini(content: str):
    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=content,
        # config=genai.types.GenerateContentConfig(
        #     temperature=0.2,
        #     top_p=0.9,
        #     max_output_tokens=600,
        # ),
    )

    return response.text


def call_openrouter(content: str):
    response = requests.post(
    url="https://openrouter.ai/api/v1/chat/completions",
    headers={
        "Authorization": f"Bearer {os.getenv('OPENROUTER_API_KEY')}",
        "Content-Type": "application/json",
    },
    data=json.dumps({
        "model": "tngtech/deepseek-r1t2-chimera:free",
        "messages": [
        {
            "role": "user",
            "content": f"{content}"
        }
        ]
    })
    )

    return response.json()["choices"][0]["message"]["content"]


if __name__ == "__main__":
    print(os.getenv("OPENROUTER_API_KEY"))

    context = f"""
    You are an experienced options trader and risk analyst.

    Given the following option legs, analyse the overall strategy as a single trade.

    For your response:
    - Start with a 1-2 sentence plain-English summary of the trade
    - Identify the strategy name if applicable (e.g. spread, straddle, condor)
    - Describe the **maximum upside** and **maximum downside**
    - Explain how the trade makes money and how it loses money
    - Highlight key risks (e.g. directional risk, volatility risk, assignment risk)
    - Mention any important assumptions you are making
    - Be succinct, logical, and clear
    - Return the response as markdown

    Option legs:
    Long call at strike price 100 with a premium of 10
    Short call at a strike price 150 with a premium of 5
    """.strip()

    print(call_openrouter(context))





