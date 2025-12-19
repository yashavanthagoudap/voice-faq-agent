class Transcript:
    def __init__(self):
        self.lines = []

    def add_user(self, text):
        self.lines.append(f"Customer: {text}")

    def add_agent(self, text):
        self.lines.append(f"Agent: {text}")

    def full_text(self):
        return "\n".join(self.lines)
