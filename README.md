# Finetuned GPT-3 Virtual Assistant

"Finetuned GPT-3 Virtual Assistant" is a chatbot that uses the "**OpenAI GPT-3 language model**" to provide assistance to users. It can be customized through "**fine-tuning**" and accessed through a web interface. Users can select between a normal or finetuned model and ask the chatbot any questions. Implemented using "Flask".

## Requirements

* Python 3.6 or higher
* OpenAI API key (sign up for one at https://beta.openai.com/)
* The following Python packages:
    ```bash
    - openai
    - flask
    ```

## File Structure

```bash
finetuned_gpt3_virtual_assistants/
├── api_key.txt
├── flask_app.py
├── requirements.txt
└── templates/
    └── index.html
```

## API Key

To use the OpenAI API, you will need an API key. You can sign up for a free API key at https://beta.openai.com/.

Once you have obtained your API key, create a file named api_key.txt in the root directory of the project and paste your API key into it. The flask_app.py script will automatically read the API key from this file.

**IMPORTANT**: Do not commit your API key to the repository. Add *api_key.txt* to your *.gitignore* file to ensure that it is not accidentally committed.

## Usage:

1. Clone this repository to your local machine:

```bash
cd finetuned_gpt3_virtual_assistants
```

2. Navigate to the project directory:

```bash
cd finetuned_gpt3_virtual_assistants
```

3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

4. Create a file named `api_key.txt` in the root directory of the project and paste your OpenAI API key into it.

5. Replace `YOUR_FINETUNED_MODEL_NAME` in `flask_app.py` with the name of your fine-tuned GPT-3 model.

6. Start the Flask web server:

```bash
python flask_app.py
```

7. Open a web browser and go to http://localhost:5000 to access the chatbot interface.

8. Select either the "Normal" or "Finetuned" model, and enter a prompt in the text input field.

9. Click the "Ask" button to receive a response from the chatbot.

## Contributions

We welcome contributions to this project! If you want to contribute, please follow these guidelines:

1. Fork the repository and create a new branch for your changes.

2. Make sure that your code follows the style guidelines of the project (e.g. PEP 8 for Python).

3. Test your changes thoroughly before submitting a pull request.

4. Make sure that your pull request includes detailed descriptions of the changes you made and why you made them.

5. We will review all pull requests and may ask you to make additional changes before merging. Thank you for your contribution!

## Contact

If you have any questions or suggestions about this project, please don't hesitate to send an email to mahmoudfazeli89@gmail.com.

## License

This project is licensed under the Apache License 2.0. See the [LICENSE](https://github.com/mahmoudfazeli/finetuned_gpt3_virtual_assistants/blob/main/LICENSE) file for details.