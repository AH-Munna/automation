import requests
import os
from dotenv import load_dotenv
import json
import sys
from time import sleep
import re

load_dotenv()

# Retrieve your Groq API key from an environment variable
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("Please set the GROQ_API_KEY environment variable")

url = "https://api.groq.com/openai/v1/chat/completions"

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}

def groq_title_divider(prompt):
    print("\033[32mpreparing title...\033[0m")
    sleep(0.5)
    payload = {
        # "model": "deepseek-r1-distill-llama-70b",
        "model": "llama-3.3-70b-specdec",
        "messages": [
            {
                "role": "user",
                "content": f'{PromptExtension["title_divider"]}\n\ngiven text: {prompt}'
            }
        ]
    }

    # Send the POST request to the API
    response = requests.post(url, headers=headers, json=payload)


    if response.status_code == 200:
        print("\033[32mgetting title divide...\033[0m")
        content: str = response.json()["choices"][0]["message"]["content"]
        sleep(1)
        print("title_divide:", content)
        sleep(1)
        print("\033[32mprocessing titles...\033[0m")

        # titles = re.split(r"\n|'|\"", content.split("</think>")[1].strip()) # for thinking models
        titles = re.split(r"\n|'|\"", content.strip())
        returnable_data = []
        for title in titles:
            title = title.strip()
            if title:
                returnable_data.append(title)
        sleep(0.5)
        if len(returnable_data) != 2:
            print(returnable_data)
            print("\033[31mTitle division failed. trying again.\033[0m")
            return groq_title_divider(prompt)
        print("\033[32mdivided titles: \033[0m",returnable_data)
        return returnable_data
    else:
        print(response.text)
        sys.exit(f"Request failed with status code {response.status_code}")

def groq_prompt_gen(prompt: list[str]):
    sleep(0.5)
    print("Title Prepared.")
    sleep(0.5)
    print("\033[32mGenerating prompt...\033[0m")
    sleep(0.5)
    payload = {
        # "model": "deepseek-r1-distill-llama-70b",
        "model": "llama-3.3-70b-specdec",
        "messages": [
            {
                "role": "user",
                "content": f'{PromptExtension["prompt_creator"]}\n\n"{prompt[0]}" "{prompt[1]}"'
            }
        ]
    }

    # Send the POST request to the API
    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 200:
        print("\033[32mgetting image prompt response...\033[0m")
        content: str = response.json()["choices"][0]["message"]["content"]
        sleep(1)
        print("image_prompt_data:", content)
        sleep(1)
        
        # image_prompt: str = content.split("</think>")[1].replace("\n", "").strip() # for thinking models
        image_prompt: str = content.replace("\n", "").strip()
        print("image_prompt: \033[32m", image_prompt, "\033[0m")
        return image_prompt
    else:
        print(response.text)
        sys.exit(f"Request failed with status code {response.status_code}")

PromptExtension = {
    "title_divider": "<instructions>only give the answer without any explanation.\n# I will give a text\n# divide it in two parts, in a appropriate meaningful way. do not rearragnge. remove ':', if exists. (e.g. 'spread the love with these 10 sayings', can be: 'SPREAD THE LOVE' 'WITH THESE 10 SAYINGS'. 'Share the Love! 90 Uplifting IWD Sayings, Quotes & Messages for 2025', can be: 'SHARE THE LOVE!' '90 UPLIFTING IWD SAYINGS, QUOTES & MESSAGES FOR 2025'. '105 Hilarious & Heartfelt Retirement Quotes for Every Occasion', can be: '105 HILARIOUS & HEARTFELT RETIREMENT QUOTES' 'FOR EVERY OCCASION')\n# answer's every letter will be uppercase</instructions>",
    "prompt_creator": "<instructions>please create a short image generation prompt using below instructions:\n\nthe image prompt contains two different texts and a related background description.\n3 short lines.\nfor first two lines, give some appropriate design/decoration/color for those texts.\nfor background, please don't describe any specific, and keep the part very short, so there are room for varieties.\njust write the prompt without explaining or describing in your final answer.\n\n(example: 'GOODBYE FEBRUARY, HELLO MARCH!' 'EMBRACE NEW BEGINNINGS', output: designed text 'GOODBYE FEBRUARY, HELLO MARCH!' written in icy blue and warm orange with melting snowflake and blooming flower accents. Elegant cursive smaller text 'EMBRACE NEW BEGINNINGS' in soft pastel tones with subtle sparkles. March themed background.)\n(example: 'REFRESH YOUR SPIRIT' 'WITH 120 UPLIFTING SPRING QUOTES', output: decorated written text 'REFRESH YOUR SPIRIT'. smaller text 'WITH 120 UPLIFTING SPRING QUOTES'. Spring colorful flower garden.)</instructions>"
    }