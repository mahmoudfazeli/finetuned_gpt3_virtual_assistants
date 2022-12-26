import openai
from flask import Flask, render_template, request

# Create an instance of the Flask class
app = Flask(__name__)

# Read the API key from the api_key.txt file
with open("api_key.txt", "r") as f:
    openai.api_key = f.read()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/query", methods=["POST"])
def query():
    # Read the model and prompt values from the request form
    model = request.form["model"]
    prompt = request.form["prompt"]

    # Select the appropriate model engine based on the model value
    if model == "normal":
        model_engine = "text-davinci-002"
    else:
        model_engine = "YOUR_FINETUNED_MODEL_NAME"  # Replace with the name of your fine-tuned model

    # Generate a response to the prompt using the selected model
    completions = openai.Completion.create(
        engine=model_engine, prompt=prompt, max_tokens=1024, n=1, stop=None, temperature=0.5
    )
    message = completions.choices[0].text

    # Return the response to the client
    return message

# Start the Flask web server
if __name__ == "__main__":
    app.run()
