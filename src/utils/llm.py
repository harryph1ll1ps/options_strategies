import os
from dotenv import load_dotenv
import google.genai as genai

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


# if __name__ == "__main__":
#     print(call_gemini("what is hello world?"))