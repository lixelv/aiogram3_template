import json


class Lexer:
    def __init__(self):
        with open("lexicon.json", "r", encoding="utf-8") as f:
            self.lexicon = json.load(f)

    def __getitem__(self, lang):
        return self.lexicon[lang] if lang in self.lexicon else self.lexicon["en"]
