from flask import Flask, render_template, request, jsonify
import openai
from openai import OpenAI
import os
import logging

# import ptvsd
# ptvsd.enable_attach(address=('0.0.0.0', 5678))

logging.basicConfig(level=logging.INFO)
logging.info("Running app.py.....")

app = Flask(__name__)

# Initialize the OpenAI client with the API key
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("No OpenAI API key found in environment variables")

client = OpenAI(
    api_key = api_key
)

system_prompt = """You are a helpful assistant who desperately wants to help people to use Maptek products. 
    Your job is to help the user use Maptek hardware, software and services. Maptek products will help 
    the user make better decisions for their mine.  You answer in short sentences. You talk about Maptek's products
    whenever you can and evangelise them and dont mention the competition.  Also, ask the user about their role and other interests in mining
    so you can give them more specific help. Address the user as Master."""

assists = client.beta.assistants.list( order="desc", limit="20",)

a_index = 0

print(assists.data)

threads = []
# Loop through each assistant in assists and create a thread for each one
for assistant in assists.data:
    thread = client.beta.threads.create()  # Create a new thread
    threads.append(thread)  # Add the thread to the list

logging.info("Assistant id = " + assists.data[a_index].id)
logging.info("Thread id = " + threads[a_index].id)

def get_assistant_index_by_name(target_name):
    for index, assistant in enumerate(assists.data):
        if assistant.name == target_name:
            return index
    return None

def get_assistant_id_by_name(target_name):
    for assistant in assists.data:
        if assistant.name == target_name:
            return assistant.id
    return None

def generate_assistant_response(user_input):
    global a_index
    try:
        logging.info(f"Getting a response from name: {assists.data[a_index].name} ({assists.data[a_index].id}) in thread:{threads[a_index].id}")
        message=client.beta.threads.messages.create(
            thread_id=threads[a_index].id,
            role="user",
            content=user_input
        )
        run = client.beta.threads.runs.create_and_poll(
            thread_id=threads[a_index].id,
            assistant_id=assists.data[a_index].id,
            instructions=system_prompt
        )
        response = "Nothing"
        if run.status == 'completed':
            messages = client.beta.threads.messages.list(
                thread_id=threads[a_index].id
            )

            if messages.data:
                all_responses = []
                for message in messages.data:
                    if message.content:
                        content_block = message.content[0]
                        text_value = content_block.text.value
                        all_responses.append(text_value)
                # Combine all message contents into one string
                combined_responses = " ".join(all_responses)
                response = assists.data[a_index].name + ": " + all_responses[0]
            else:
                response = "All messages empty"
        else:
            response = "Messages is empty"
        return response
    except Exception as e:
        print(f"Error generating response: {e}")
        return f"Sorry, something went wrong! ERROR={e},RUN={run},MESSAGES={messages}."

def generate_response(user_input):
    try:
        completion = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a helpful assistant"},
                {"role": "user", "content": user_input},
            ]
        )
        bot_message = completion.choices[0].message.content
        return bot_message
    except Exception as e:
        print(f"Error generating response: {e}")
        return f"Sorry, something went wrong! {e}."

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/get_test_keys', methods=['GET'])
def get_keys():
    keys = ["key1", "key2", "key3", "key4"]  # Define your keys here
    return jsonify(keys)


@app.route('/get_keys', methods=['GET'])
def get_assistants():
    try:
        # Fetch the list of assistants from OpenAI API
        assistants_data = [assistant.name for assistant in assists.data]
        logging.info(f"assistants: {assistants_data}")
        
        return jsonify(assistants_data)
    except Exception as e:
        logging.error(f"Error fetching assistants: {e}")
        return jsonify({"error": "Failed to retrieve assistants"}), 500


@app.route('/set_key', methods=['POST'])
def set_key():
    global selected_key
    global a_index
    data = request.json
    selected_key = data.get('selected_key')
    logging.info(f"Selected key received: {selected_key}")
    a_index = get_assistant_index_by_name(selected_key)
    return jsonify({"status": "success", "selected_key": selected_key})

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('input')
    if not user_input:
        return jsonify({"response": "No input provided"}), 400

    bot_response = generate_assistant_response(user_input)
    return jsonify({"response": bot_response})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=51645, debug=True)
