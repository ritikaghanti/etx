import openai
from dotenv import load_dotenv
import os

# Load API key from .env
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Test the connection with a prompt
try:
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "What is the weather in Goa?"}
        ]
    )

    print("✅ API Call Successful!")
    print("🔍 Response:")
    print(response.choices[0].message["content"])

except Exception as e:
    print("❌ Something went wrong:")
    print(e)
