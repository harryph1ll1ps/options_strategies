import os
import requests
import json
import streamlit as st

def call_openrouter(content: str):

    key = st.secrets.get("OPENROUTER_API_KEY") or os.getenv("OPENROUTER_API_KEY")

    if not key:
        raise RuntimeError("API Key Not Found")

    response = requests.post(
    url="https://openrouter.ai/api/v1/chat/completions",
    headers={
        "Authorization": f"Bearer {key}",
        "Content-Type": "application/json",
    },
    data=json.dumps({
        "model": "xiaomi/mimo-v2-flash:free",
        "messages": [
        {
            "role": "user",
            "content": f"{content}"
        }
        ]
    }),
    timeout=20
    )

    if response.status_code != 200:
        raise RuntimeError(f"OpenRouter error {response.status_code}: {response.text}")
    
    try:
        data = response.json()
    except ValueError:
        raise RuntimeError("Invalid JSON response from OpenRouter")

    return data["choices"][0]["message"]["content"]




#import google.genai as genai
# def call_gemini(content: str):
#     client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

#     response = client.models.generate_content(
#         model="gemini-3-flash-preview",
#         contents=content,
#         # config=genai.types.GenerateContentConfig(
#         #     temperature=0.2,
#         #     top_p=0.9,
#         #     max_output_tokens=600,
#         # ),
#     )

#     return response.text





if __name__ == "__main__":
    print(os.getenv("OPENROUTER_API_KEY"))

    context = f"""
    You are a professional options trader and risk analyst.
    Analyse the following option legs as a single, unified strategy, not as individual trades.

    Output requirements:
    Write in a professional but accessible tone, suitable for an informed retail or institutional trader
    Be concise, high-level, and conceptual rather than numerically precise
    Do not over-focus on exact strike prices or premiums; use them only to infer structure and payoff
    Avoid unnecessary jargon or edge-case details
    Structure your response exactly as follows (markdown, bold section headers):

    Strategy Name:
    Identify the commonly accepted strategy name (e.g. vertical spread, straddle, condor). If none clearly applies, write 'N/A'.

    Overview:
    One plain-English sentence explaining what the trade is trying to achieve and the market view it expresses.

    Economics:
    Explain how the trade makes money and how it loses money in general terms, including payoff shape and where gains or losses are capped.

    Risks:
    Describe the primary risks (e.g. directional risk, time decay, capped upside, volatility changes), focusing on what could go wrong.

    Assumptions:
    State the key assumptions required for the trade thesis to hold (e.g. price movement, volatility behaviour, liquidity, early exercise considerations).

    Option legs:
    List the option legs exactly as provided, without reinterpretation.

    Here are the option legs to analyse:

    Option legs:
    Long call at strike price 100 with a premium of 10
    Short call at a strike price 150 with a premium of 5
    """.strip()

    print(call_openrouter(context))





