import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class CodeMentorAgent:
    def __init__(self):
        self.api_key = os.getenv("GROQ_API_KEY")
        if not self.api_key:
            raise ValueError("Missing GROQ_API_KEY environment variable")

        self.base_url = "https://api.groq.com/openai/v1/chat/completions"
        self.model = "llama-3.3-70b-versatile"  # Updated to a supported model

    def run(self, query: str) -> str:
        """Send user query to Groq API and return AI response."""
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        payload = {
            "model": self.model,
            "messages": [
                {"role": "system", "content": "You are an AI Code Mentor. Help debug, explain, and optimize code clearly."},
                {"role": "user", "content": query}
            ],
            "temperature": 0.7
        }

        response = requests.post(self.base_url, headers=headers, json=payload)
        data = response.json()
        print("DEBUG RESPONSE:", data)  # For debugging

        try:
            if "choices" in data and len(data["choices"]) > 0:
                choice = data["choices"][0]
                if "message" in choice and "content" in choice["message"]:
                    return choice["message"]["content"]
                if "text" in choice:
                    return choice["text"]
                if "delta" in choice and "content" in choice["delta"]:
                    return choice["delta"]["content"]

            return "⚠️ Could not parse Groq response. Check DEBUG RESPONSE in terminal."
        except Exception as e:
            return f"⚠️ Error parsing response: {str(e)}"
