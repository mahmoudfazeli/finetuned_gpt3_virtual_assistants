import os
import json
import openai
from flask import Flask, render_template, request

app = Flask(__name__)
openai.api_key = os.environ["OPENAI_API_KEY"]

# Create a global variable to store the previous response
prev_response = ""

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_prompt', methods=['POST'])
def send_prompt():
    global prev_response
    prompt = json.loads(request.data)['prompt']
    # Append the previous response to the prompt
    prompt = prev_response + prompt
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=2048,
        n=1,
        stop=None,
        temperature=0.7,
    )
    # Update the previous response to be the current response
    prev_response = response["choices"][0]["text"]
    return prev_response

if __name__ == '__main__':
    app.run()
