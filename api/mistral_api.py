import requests
import random
from config import MISTRAL_API_KEY, MISTRAL_API_URL

def get_mistral_response(messages):
    headers = {"Authorization": f"Bearer {MISTRAL_API_KEY}"}
    data = {"model": "mistral-tiny", "messages": messages}

    try:
        response = requests.post(MISTRAL_API_URL, headers=headers, json=data)
        if response.status_code == 200:
            raw_response = response.json().get("choices", [{}])[0].get("message", {}).get("content", "Error: No response received.")
            prompts = [
                "Sure, here's what I found:",
                "That's a great question!",
                "Let me break it down for you:",
                "Here's an insightful take on that:",
                "Let's explore this together:",
                "Certainly!",
                "Absolutely, here’s what I can tell you:"
            ]
            return f"{random.choice(prompts)}\n{raw_response}"
        else:
            return "I couldn't fetch a response at the moment. Please try again later."
    except requests.exceptions.RequestException:
        return "Error: Unable to connect to the AI service."