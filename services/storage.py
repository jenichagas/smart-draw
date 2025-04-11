import os, json, random

HISTORY_FILE = "data/history.json"
PARTICIPANT_FILE ="data/participants.json"

PARTICIPANT_FILE = "data/participants.json"
HISTORY_FILE = "data/history.json"


def load_participants():
    if not os.path.exists(PARTICIPANT_FILE):
        return []

    try:
        with open(PARTICIPANT_FILE, "r") as f:
            data = json.load(f)
            return data if isinstance(data, list) else []
    except json.JSONDecodeError:
        return []


def save_participants(data):
    os.makedirs(os.path.dirname(PARTICIPANT_FILE), exist_ok=True)
    with open(PARTICIPANT_FILE, "w") as f:
        json.dump(data, f, indent=2)


def add_to_history(entry):
    history = []
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r") as f:
            content = f.read().strip()
            if content:
                try:
                    history = json.loads(content)
                except json.JSONDecodeError:
                    history = []
    history.insert(0, entry)
    with open(HISTORY_FILE, "w") as f:
        json.dump(history, f, indent=2)
