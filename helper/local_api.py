import requests

def find_text_on_screen(text: str):
    """
    Finds the coordinates of a given text on the screen by calling a local API.

    Args:
        text: The text to find on the screen.

    Returns:
        A JSON object with the coordinates of the text, or None if an error occurs.
    """
    return # FIXME: wip
    url = "http://localhost:8004/find_text"
    payload = {"text": text}

    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error calling the screen API: {e}")
        return None
