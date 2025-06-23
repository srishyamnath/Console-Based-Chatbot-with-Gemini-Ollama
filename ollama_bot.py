import requests
import json

class OllamaBot:
    def __init__(self, model="phi3:mini"):
        self.model = model
        self.chat_history = []

    def get_response(self, user_input):
        self.chat_history.append({"role": "user", "content": user_input})
        full_response = ""

        try:
            response = requests.post(
                "http://localhost:11434/api/chat",
                json={"model": self.model, "messages": self.chat_history},
                timeout=30
            )

            print("\n🛠 DEBUG Raw Ollama Response:")
            print(response.text)  # Can comment out later

            for line in response.text.strip().splitlines():
                try:
                    data = json.loads(line)
                    if "message" in data and "content" in data["message"]:
                        full_response += data["message"]["content"]
                    if data.get("done", False):
                        break  # Stop if final chunk
                except json.JSONDecodeError:
                    continue

            if full_response:
                self.chat_history.append({"role": "assistant", "content": full_response})
                return full_response.strip()

            return "[❌ No valid response from Ollama.]"

        except Exception as e:
            return f"[❌ Error: {str(e)}]"
