import openai
import os
from dotenv import load_dotenv

# Load environment variables from .env (if present)
load_dotenv()

# Correct way – read from env, fall back to a clear error if missing
openai.api_key = os.getenv("OPENAI_API_KEY")
if not openai.api_key:
    raise ValueError(
        "OPENAI_API_KEY not found. "
        "Copy .env.example to .env and add your real key."
    )

# Rwanda seasonal crop guide
seasonal_crops = {
    "long_rainy": ["Maize", "Beans", "Banana", "Sweet Potato"],
    "short_rainy": ["Irish Potato", "Maize", "Tomato", "Onion"],
    "dry": ["Cassava", "Sorghum", "Groundnuts"]
}

# Function to get response from OpenAI
def get_response(user_input: str) -> str:
    # Add seasonal advice
    if "season" in user_input.lower():
        if "long" in user_input.lower():
            crops = seasonal_crops["long_rainy"]
        elif "short" in user_input.lower():
            crops = seasonal_crops["short_rainy"]
        elif "dry" in user_input.lower():
            crops = seasonal_crops["dry"]
        else:
            crops = ["Maize", "Beans", "Banana"]
        user_input += f" Recommended crops for this season in Rwanda: {', '.join(crops)}."

    conversation = [
        {"role": "system", "content": (
            "You are AgriBot, an AI assistant for Rwanda farmers. "
            "Give practical, friendly, and accurate crop advice, "
            "including seasonal recommendations and weather tips."
        )},
        {"role": "user", "content": user_input}
    ]

    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=conversation
    )
    return response.choices[0].message.content.strip()
