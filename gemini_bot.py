import google.generativeai as genai
from google.api_core.exceptions import ResourceExhausted

class GeminiBot:
    def __init__(self, api_key):
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-1.5-flash')
        self.chat = self.model.start_chat(history=[])

    def get_response(self, user_input):
        try:
            response = self.chat.send_message(user_input)
            return response.text.strip()
        except ResourceExhausted as e:
            return (
                "❌ You’ve hit the usage limit for the Gemini free tier.\n\n"
                "✅ Tips:\n"
                "- Wait for your quota to reset (daily/minute limit)\n"
                "- Reduce the frequency of queries\n"
                "- Upgrade your plan for more usage\n\n"
                "🔗 Docs: https://ai.google.dev/gemini-api/docs/rate-limits"
            )
        except Exception as e:
            return f"❌ Error: {str(e)}"

