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



**Strategy Name:**
Bull Call Spread (Vertical Call Spread)

**Summary:**
A defined-risk bullish trade that benefits from a moderate rise in the underlying price while capping both gains and losses.

**Economics:**
The trade profits as the underlying rises above the lower strike, with gains limited once it exceeds the higher strike. The maximum loss is the net premium paid, occurring if the underlying finishes below the lower strike.

**Risks:**
If the underlying fails to rise sufficiently, the position can lose part or all of the premium. Upside is capped, and time decay hurts returns if the price remains flat.

**Assumptions:**
Assumes minimal early-exercise risk, adequate market liquidity, and relatively stable implied volatility.




You are a professional options trader and risk analyst.

Analyse the following option legs as a single, unified strategy, not as individual trades.

Output requirements:

Write in a professional but accessible tone, suitable for an informed retail or institutional trader

Be concise, high-level, and conceptual rather than numerically precise

Do not over-focus on exact strike prices or premiums; use them only to infer structure and payoff

Avoid unnecessary jargon or edge-case details

Structure your response exactly as follows (markdown, bold section headers):

Strategy Name:
Identify the commonly accepted strategy name (e.g. vertical spread, straddle, condor). If none clearly applies, write “N/A”.

Summary:
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
{trade_context}



