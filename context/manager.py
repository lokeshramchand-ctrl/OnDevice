class ContextManager:
    def __init__(self, max_minutes):
        self.max_minutes = max_minutes
        self.recent = []
        self.decisions = []
        self.actions = []
        self.questions = []

    def add_transcript(self, text):
        self.recent.append(text)

    def trim(self, max_items=10):
        self.recent = self.recent[-max_items:]

    def build_prompt_context(self):
        return {
            "recent_transcript": self.recent,
            "decisions": self.decisions,
            "actions": self.actions,
            "questions": self.questions
        }

    def extract(self, text):
        if "decide" in text.lower():
            self.decisions.append(text)
        if "todo" in text.lower() or "action" in text.lower():
            self.actions.append(text)
        if "?" in text:
            self.questions.append(text)
