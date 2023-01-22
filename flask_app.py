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
        model=model,
        prompt=prompt,
        temperature=0.7,
        max_tokens=60,
        top_p=0.3,
        frequency_penalty=0.5,
        presence_penalty=0,
        n=1,
        stop=None
    )   
    # Update the previous response to be the current response
    prev_response = response["choices"][0]["text"]
    return prev_response

if __name__ == '__main__':
    # Define a list of valid model names
    valid_models = ["text-davinci-003", "text-curie-001", "text-babbage-001", "text-ada-001"]

    # Prompt the user for a model name
    while True:
        print("Please select a model:")
        for i, model_name in enumerate(valid_models):
            print(f"{i+1}. {model_name}")
        print("4. Enter custom model name")
        choice = input("Enter the number of your choice: ")
        if choice == "4":
            model = input("Enter a custom model name: ")
            break
        elif int(choice) in range(1,4):
            model = valid_models[int(choice)-1]
            break
        else:
            print("Invalid choice. Please try again.")
    app.run()
