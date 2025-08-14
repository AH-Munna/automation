import requests
import json
import dotenv
import os

dotenv.load_dotenv()

response = requests.get(
  url="https://openrouter.ai/api/v1/auth/key",
  headers={
    "Authorization": f"Bearer {os.getenv('openrouter_ahm3')}"
  }
)

print(json.dumps(response.json(), indent=2))