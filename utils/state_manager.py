import json

def save_settings(settings, file_path="settings.json"):
    with open(file_path, "w") as file:
        json.dump(settings, file)

def load_settings(file_path="settings.json"):
    try:
        with open(file_path, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return None
