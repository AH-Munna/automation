# from openai import OpenAI
# import dotenv
# import os
# dotenv.load_dotenv()
# API_KEY = os.getenv("GOOGLE_AI_STUDIO_KEY")
# print(API_KEY)

# client = OpenAI(
#     api_key=API_KEY,
#     base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
# )

# response = client.chat.completions.create(
#     model="gemini-2.5-flash",
#     messages=[
#         {"role": "system", "content": "You are a helpful assistant."},
#         {
#             "role": "user",
#             "content": "Explain to me how AI works"
#         }
#     ]
# )

# print(response.choices[0].message)

from pyautogui import click

from helper.find_image import find_image
from helper.get_path import get_resource_path
from helper.pyscreensize import screenHeight, screenWidth

click(find_image(get_resource_path('images/tabs/pinterest_chrome.png'), 0.8))

click(screenWidth-110, 220, duration=1)