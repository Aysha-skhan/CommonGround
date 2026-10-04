import os
from pathlib import Path

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

# Load configuration from the folder containing this script.
load_dotenv(Path(__file__).parent / ".env")

if not os.getenv("GOOGLE_API_KEY"):
    raise ValueError("Add GOOGLE_API_KEY to your .env file.")

model = ChatGoogleGenerativeAI(
    model=os.getenv("GEMINI_MODEL", "gemini-3.5-flash-lite"),
    vertexai=False,
    timeout=30,
    max_retries=1,
)

response = model.invoke(
    "Explain the difference between a hard constraint and a soft "
    "preference in group decision-making. Use one short example."
)

print(response.text)
print("\nToken usage:", response.usage_metadata)