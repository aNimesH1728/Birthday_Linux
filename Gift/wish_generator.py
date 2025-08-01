import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI()

def generate_wish(name,traits=""):
    prompt=f"Craft a heartwarming birthday message for someone named {name}, my amazing bestie! 🎉 Reflect on the joy and love we’ve shared, celebrating our achievements this past year. Express my pride, share hopes for {name}'s future, add a touch of humor from our adventures and create a sensory-rich celebration. Keep it concise, yet deeply personal—make it a 200-word celebration that captures the essence of our extraordinary bond."
    if traits:
        prompt+=f"Here are some of her traits, which i want you to touch upon: {traits}"

    response = client.chat.completions.create(model="gpt-4",
    messages=[
        {
            "role":"system",
            "content":"I need you to act as a professional birthday wishes writer who has experience of 8 years in crafting special and customized birthday greetings."
        },
        {
            "role":"user",
            "content":prompt
        }
    ],
    temperature=0.9,
    max_tokens=200
    )

    return response.choices[0].message.content.strip()

