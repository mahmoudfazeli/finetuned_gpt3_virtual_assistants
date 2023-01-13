import os
import json
import openai
from flask import Flask, render_template, request

app = Flask(__name__)
openai.api_key = os.environ["OPENAI_API_KEY"]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_prompt', methods=['POST'])
def send_prompt():
    prompt = json.loads(request.data)['prompt']
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=2048,
        n=1,
        stop=None,
        temperature=0.7,
    )
    return response["choices"][0]["text"]

if __name__ == '__main__':
    app.run()