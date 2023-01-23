import os
import configargparse
import json
import openai
from flask import Flask, render_template, request

app = Flask(__name__)
openai.api_key = os.environ["OPENAI_API_KEY"]

def load_config():
    parser = configargparse.ArgParser(default_config_files=['assistant_config.ini'])
    parser.add('-c', '--config', is_config_file=True, help='config file path')
    parser.add('--assistant_name', default=None, help='Name of the assistant')
    parser.add('--identity', default=None, help='Identity of the assistant')
    return parser.parse_args()


@app.route('/')
def index():
    return render_template('index.html',
                            assistant_name=config.assistant_name,
                            identity=config.identity
                            )

@app.route('/send_prompt', methods=['POST'])
def send_prompt():
    assistant_name = config.assistant_name
    identity = config.identity
    start_sequence = "\nUser-> "
    restart_sequence = "\n"+assistant_name+"-> "
    conversation = identity + "\n\n"
    prompt = json.loads(request.data)['prompt']
    # Append the prompt to the conversation
    conversation = conversation + start_sequence + prompt + restart_sequence
    response = openai.Completion.create(
        model=model,
        prompt=conversation,
        temperature=0.9,
        max_tokens=150,
        top_p=1,
        presence_penalty=0,
        frequency_penalty=0.6,
        n=1,
        #stop=[" User:", " AI:"]
        stop=[" User->", " "+assistant_name+"->"]
    )   
    # Update the conversation
    conversation = conversation + response["choices"][0]["text"]
    print (conversation)
    return response["choices"][0]["text"]

if __name__ == '__main__':
    config=load_config()

    # Define a list of valid model names
    valid_models = ["text-davinci-003", "text-curie-001", "text-babbage-001", "text-ada-001", "davinci:ft-personal-2023-01-11-15-48-39"]

    # Prompt the user for a model name
    while True:
        print("Please select a model:")
        for i, model_name in enumerate(valid_models):
            print(f"{i+1}. {model_name}")
        custom_model_num = len(valid_models) + 1
        print(f"{custom_model_num}. Enter custom model name")
        choice = input("Enter the number of your choice: ")
        if choice == str(custom_model_num):
            model = input("Enter a custom model name: ")
            break
        elif int(choice) in range(1, custom_model_num):
            model = valid_models[int(choice)-1]
            break
        else:
            print("Invalid choice. Please try again.")
    app.run()
