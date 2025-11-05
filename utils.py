from openai import OpenAI
from PyPDF2 import PdfReader
import re, os

# Create client compatible with OpenRouter
def init_openai_client(api_key, api_base):
    global client
    client = OpenAI(
        api_key=api_key,
        base_url=api_base.rstrip("/")  # works for OpenRouter
    )

def parse_pdf(uploaded_file):
    reader = PdfReader(uploaded_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text

def call_chat_completion(messages, model="gpt-4o-mini", temperature=0.2, max_tokens=512):
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature,
        max_tokens=max_tokens
    )
    return {
        "text": response.choices[0].message.content,
        "raw": response
    }

def safe_filename(prefix="session"):
    import time
    return re.sub(r"[^a-zA-Z0-9_-]", "_", f"{prefix}_{int(time.time())}")
