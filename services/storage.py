import os, json, random

DATA_FILE = "data/participants.json"
HISTORY_FILE = "data/history.json"

def load_participants():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_participants(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f)

def add_to_history(entry):
    history = []
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r") as f:
            history = json.load(f)
    history.insert(0, entry)
    with open(HISTORY_FILE, "w") as f:
        json.dump(history, f)