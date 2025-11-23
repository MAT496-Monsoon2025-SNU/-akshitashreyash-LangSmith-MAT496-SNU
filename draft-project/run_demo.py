# run_demo.py - Perplexity demo script
from dotenv import load_dotenv
import os
import requests
import sys

load_dotenv()
api_key = os.getenv("PERPLEXITY_API_KEY")
if not api_key:
    raise Exception("PERPLEXITY_API_KEY not found in .env")

url = "https://api.perplexity.ai/chat/completions"
payload = {
    "model": "sonar",
    "messages": [
        {"role":"system","content":"You are a helpful assistant."},
        {"role":"user","content":"Test reply: say Hello."}
    ],
    "max_tokens": 20
}
headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}

try:
    r = requests.post(url, headers=headers, json=payload, timeout=30)
    r.raise_for_status()
except requests.exceptions.RequestException as e:
    print("Request failed:", e)
    sys.exit(1)

try:
    reply = r.json()["choices"][0]["message"]["content"].strip()
except Exception as e:
    print("Failed to parse response:", e)
    print("Raw response:", r.text)
    sys.exit(1)

print(reply)
