from flask import Flask, render_template, request, jsonify
from openai import OpenAI
import os

app = Flask(__name__)

# Set your OpenAI API key
# client = OpenAI(
  # api_key=os.environ['OPENAI_API_KEY'],  # this is also the default, it can be omitted
# )

# Function to start a thread and get a response from OpenAI
def generate_response(user_input):
    try:
        print("Debug 1")
        client = OpenAI()
        print("Debug 2")
        completion = client.chat.completions.create(
            model="gpt-4", 
            messages=[
                {"role": "system", "content": "You are a helpful assistant"},
                {"role": "user", "content": user_input}])

        print("Debug 3")

        # completion = client.completions.create(model='gpt-4',
            # messages=[
                # {"role": "system", "content": "You are a helpful assistant."},
                # {"role": "user", "content": user_input},
            # ]
        # )

        bot_message = completion.choices[0].message.content
        return bot_message
    except Exception as e:
        print(f"Error generating response: {e}")
        return f"Sorry, something went wrong! {e}."

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('input')
    if not user_input:
        return jsonify({"response": "No input provided"}), 400

    bot_response = generate_response(user_input)
    return jsonify({"response": bot_response})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8087, debug=True)
