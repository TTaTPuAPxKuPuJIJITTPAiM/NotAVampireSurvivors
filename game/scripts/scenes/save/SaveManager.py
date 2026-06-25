import json
import os

class SaveManager:
    def __init__(self, filename="save_data.json"):
        self.filename = filename
        self.default_data = {
            "high_score": 0,
            "gold": 0
        }

    def load_game(self):
        if not os.path.exists(self.filename):
            self.save_game(self.default_data)
            return self.default_data.copy()
        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                return json.load(file)
        except:
            return self.default_data.copy()

    def save_game(self, data):
        try:
            with open(self.filename, "w", encoding="utf-8") as file:
                json.dump(data, file, indent=4, ensure_ascii=False)
        except Exception as e:
            print(f"Save error: {e}")