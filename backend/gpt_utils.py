from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Initialize OpenAI client with API key
client = OpenAI(api_key=os.getenv("OPEN_API_KEY"))

def analyze_meeting(transcript):
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an expert meeting assistant."},
            {"role": "user", "content": f"""
Here is a meeting transcript:
{transcript}

Summarize the key points, list action items, decisions made, 
and generate a follow-up email.
"""}
        ]
    )
    return response.choices[0].message.content
