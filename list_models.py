import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
print("🔑 API Key found:", bool(api_key))

try:
    genai.configure(api_key=api_key)
    models = genai.list_models()
    if not models:
        print("⚠️ No models returned.")
    for m in models:
        print(f"🧠 {m.name} | supports: {m.supported_generation_methods}")
except Exception as e:
    print("❌ Error listing models:", e)
