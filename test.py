from openai import OpenAI
import dotenv
import os
dotenv.load_dotenv()
API_KEY = os.getenv("GOOGLE_AI_STUDIO_KEY")
print(API_KEY)

client = OpenAI(
    api_key=API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": "Explain to me how AI works"
        }
    ]
)

print(response.choices[0].message)