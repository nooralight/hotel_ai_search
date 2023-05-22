import openai
import os
from dotenv import load_dotenv
load_dotenv()
openai.api_key = os.getenv('OPENAI_TOKEN')

class Gpt_API:
    def __init__(self,prompt):
        self.prompt = prompt
        print("Prompt is ",prompt)

    def get_result(self):
        completion = openai.ChatCompletion.create(model="gpt-3.5-turbo",messages=[{"role": "user", "content": self.prompt}],max_tokens=2000,temperature=0.2)
        text = completion['choices'][0]['message']['content']
        return text
