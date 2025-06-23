class ChatSession:
    def __init__(self):
        self.history = []

    def add(self, role, message):
        self.history.append({"role": role, "message": message})

    def get_context(self):
        return "\n".join([f"{x['role'].capitalize()}: {x['message']}" for x in self.history])
