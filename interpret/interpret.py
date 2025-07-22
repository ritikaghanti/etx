import openai
import os
import json

openai.api_key = os.getenv("OPENAI_API_KEY")

def interpret_text(text):
    print(f"[INFO] Sending to GPT: {text}")
    prompt = f"""
You are an intent detection engine. Given the following user input, extract the intent and any relevant entities (like locations, dates, times, etc). 
Only respond with valid JSON. Do not add any explanation or extra text. Respond only in a valid JSON object like:
{{"intent": "get_weather", "location": "Goa"}}

If you can't find an intent, return:
{{"intent": "unknown"}}

User input: "{text}"
"""

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Use "gpt-4" only if your key has access
            messages=[{"role": "user", "content": prompt}]
        )
        raw_output = response["choices"][0]["message"]["content"]
        print(f"[DEBUG] Raw GPT output:\n{raw_output}")

        # Parse JSON safely
        try:
            parsed = json.loads(raw_output)
            return parsed
        except json.JSONDecodeError:
            return {"intent": "unknown", "error": "Invalid JSON"}

    except Exception as e:
        print(f"[ERROR] OpenAI API call failed: {e}")
        return {"intent": "unknown", "error": str(e)}
