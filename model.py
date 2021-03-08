import json

# Don't use this is in a real production setting

def load_db():
    with open("flashcards_db.json") as f:
        return json.load(f)

def save_db():
    with open("flashcards_db.json", 'w') as f:
        return json.dump(db, f)

db = load_db()